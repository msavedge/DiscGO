import DiscGO as dg
import PySimpleGUI as sg
import pandas as pd
import DiscGOgui as dgg


def get_csv_data_frame():
    df = pd.read_csv('./mold_master_list.csv')
    # print(df.head())
    return df


def update_tables(fdf, conditions, window):
    for k, v in conditions.items():
        if k in ("glide", "turn", "fade"):
            break
        if k in ("type", "mold"):
            pivot = fdf.pivot_table(index=k, values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
        else:
            pivot = fdf.pivot_table(index=k, values="mold", aggfunc="count", margins=True).to_dict()['mold'].items()
        # update table row data
        window[f'-tbl_{k}-'].update(values=pivot)
        # update frame titles
        window[f'-frm_{k}-'].update(conditions[k])

        # clear string so it is not displayed above column
        if v in ("", "All", "ALL"):
            v = ''
        # update column header
        window[f'-tbl_{k}-'].update(values=pivot)
        # update frame title
        window[f'-frm_{k}-'].update(v)


def get_disc_count_by_filter(_filter):
    print(f'filter: {_filter}')
    df = get_csv_data_frame()
    print(f'CSV DATA: {df}')

    if _filter == 'mold':
        pivot = df.pivot_table(index="mold", values="brand", aggfunc="count", margins=True)
        rows = pivot.to_dict()['brand'].items()
    else:
        pivot = df.pivot_table(index=_filter, values="mold", aggfunc="count", margins=True)
        rows = pivot.to_dict()['mold'].items()
    return rows


# logic code above
# GUI code below
def get_table_by_filter(filter):  # filter = type, brand, speed, etc.
    headings = [f'{filter.upper()}', 'COUNT']
    values = get_disc_count_by_filter(filter)
    table = [sg.Table(headings=headings,
                      values=values,
                      justification='right',
                      alternating_row_color='#FDFFFC',
                      row_height=25,
                      num_rows=min(13, len(values)),
                      enable_click_events=True,
                      enable_events=False,
                      header_text_color='#CC3333',
                      key=f"-tbl_{filter.lower()}-",
                      pad=((20, 10), (10, 10)))]
    return table


def get_frame_by_filter(_filter):
    frame = [sg.Frame('', [[sg.Text('ALL', key=f"-frm_{_filter.lower()}-")],
                           get_table_by_filter(_filter)])]
    return frame


def get_col1():
    return sg.Column([get_frame_by_filter('type'),
                      [sg.Button('RESET FILTERS',
                                 key='btn-reset',
                                 disabled=True)],
                      [sg.Button('COMPARE MOLDS',
                                 key='btn-compare',
                                 disabled=True)],
                      [sg.Button('ADD MOLD',
                                 key='btn-add',
                                 disabled=True)]
                      ])


def get_col2():
    return sg.Column([get_frame_by_filter('brand')])


def get_col3():
    return sg.Column([get_frame_by_filter('mold')])


def get_col4():
    return sg.Column([get_frame_by_filter('speed')])


def get_col5():
    return sg.Column([get_frame_by_filter('stability')])


def get_col6():
    return sg.Column([get_frame_by_filter('weight')])


def get_layout():
    layout = [
                [sg.Text('Click on a row to filter molds by that category.', pad=((20, 10), (10, 10))),
                 sg.Text('Click on a white header to remove the filter.')],
                [sg.vtop([get_col1(), get_col2(), get_col3(), get_col4(), get_col5()])]
              ]
    return layout


def show():
    layout = get_layout()
    window = sg.Window('MOLD SELECTION', layout, titlebar_text_color='#CC3333')
    # ------ Event Loop ------
    conditions = {'type': '',
                  'brand': '',
                  'mold': '',
                  'speed': '',
                  'stability': ''}

    while True:
        enable_reset_button = False

        event, values = window.read()
        print(f'event: {event}')
        print('')
        print(f'values: {values}')

        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            break

        # to filter: click on a row in any table
        #   onclick(): 'tighten' dataframe and re-run pivot tables to regenerate data in all other tables
        # if event == clicked on 'TYPE' row 0 (first row in table)
        #   get type of disc to filter on
        if event[0] == '-tbl_type-':
            # print(f'TBL_TYPE EVENT VALUES: {values}')
            row = event[2][0]
            print(f'ROW: {row}')
            if row == -1:
                TYPE = ''
            else:
                table_data = window["-tbl_type-"].get()
                # print(f'TABLE DATA: \n{table_data}')
                # [print(i) for i in table_data]
                df = pd.DataFrame(table_data)
                TYPE = df.iloc[row].tolist()[0]
                # print(f'TYPE: {TYPE}')
            conditions.update({'type': TYPE})

        elif event[0] == '-tbl_brand-':
            row = event[2][0]
            if row == -1:
                BRAND = ''
            else:
                table_data = window["-tbl_brand-"].get()
                df = pd.DataFrame(table_data)
                BRAND = df.iloc[row].tolist()[0]
            conditions.update({'brand': BRAND})

        elif event[0] == '-tbl_mold-':
            row = event[2][0]
            if row == -1:
                MOLD = ''
            else:
                table_data = window["-tbl_mold-"].get()
                df = pd.DataFrame(table_data)
                MOLD = df.iloc[row].tolist()[0]
            conditions.update({'mold': MOLD})

        elif event[0] == '-tbl_speed-':
            row = event[2][0]
            if row == -1:
                SPEED = ''
            else:
                table_data = window["-tbl_speed-"].get()
                df = pd.DataFrame(table_data)
                SPEED = df.iloc[row].tolist()[0]
            conditions.update({'speed': SPEED})

        elif event[0] == '-tbl_stability-':
            row = event[2][0]
            if row == -1:
                STABILITY = ''
            else:
                table_data = window["-tbl_stability-"].get()
                df = pd.DataFrame(table_data)
                STABILITY = df.iloc[row].tolist()[0]
            conditions.update({'stability': STABILITY})

        elif event == 'btn-reset':
            conditions = {'type': '',
                          'brand': '',
                          'mold': '',
                          'speed': '',
                          'stability': ''}

        df = dg.eat_pickle('mold_list.pkl')
        fdf = dg.get_filtered_dataframe(df, conditions)

        # print(f'FILTERED DATA FRAME: {fdf}')

        update_tables(fdf, conditions, window)

        if event == 'btn-compare' or event == 'btn-add':
            # instead of sending df to MCM as variable:
            # to_pickle() here
            # read_pickle() from mold comparison matrix
            fdf.to_pickle('fdf.pkl')

            if event == 'btn-compare':
                # show mold comparison matrix
                dgg.run_window('mold_comparison_matrix')
            elif event == 'btn-add':
                dgg.run_window('disc_add_window')

        # turn buttons on/off as needed
        for k, v in conditions.items():
            if v not in ('', 'All'):
                enable_reset_button = True

        if enable_reset_button:
            window['btn-reset'].update(disabled=False)
            window['btn-compare'].update(disabled=False)
        else:
            window['btn-reset'].update(disabled=True)
            window['btn-compare'].update(disabled=True)
        # if only one mold selected, enable add button, disable compare button
        if fdf.shape[0] == 1:
            window['btn-add'].update(disabled=False)
            window['btn-compare'].update(disabled=True)
        else:
            window['btn-add'].update(disabled=True)


if __name__ == '__main__':
    show()
