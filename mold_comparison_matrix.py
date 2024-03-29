import sqlite3
import pandas as pd
import DiscGO as dg
import DiscGOgui as dgg
import PySimpleGUI as sg
import pickle


conditions = {'type': '',
              'brand': '',
              'mold': '',
              'speed': '',
              'glide': '',
              'turn': '',
              'fade': '',
              'stability': ''}
dg.make_pickle(conditions, 'mcm_cond.pkl')

gray = '#FFFFFF'
red = '#CC3333'


def get_csv_data_frame():
    return pd.read_csv('./mold_master_list.csv')


# def get_fdf():  # filtered data frame - this is the comparison matrix
#     return pd.read_pickle('fdf.pkl')


def get_layout():
    df = dg.eat_pickle('fdf.pkl')
    data = df.values.tolist()
    print(f'data: {data}')
    # pad header text to set min column widths for table - keeps filter flags from shifting as much
    header_list = [' TYPE ', '     BRAND     ', '      MOLD      ', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'STABILITY']
    print(f'header_list: {header_list}')

    row_count = df.shape[0]
    if row_count > 10:
        row_count = 10

    layout = [[sg.Text('Click on a row to filter molds by that category.', pad=((20, 10), (10, 10))),
               sg.Text('Click on a white header to remove the filter.')],
              [sg.Table(headings=header_list,
                         values=data,
                         justification='right',
                         alternating_row_color='#FDFFFC',
                         row_height=30,
                         num_rows=min(len(data), 10),
                         enable_click_events=True,
                         enable_events=False,
                         header_border_width=2,
                         header_text_color=red,
                         key="-tbl_main-",
                         pad=((20, 10), (10, 10)))],
               [sg.Button('RESET',
                          pad=((20, 450), (5, 10)),
                          disabled=True,
                          key='btn-reset'),
                sg.Button('ADD DISC',
                          pad=(20, 5),
                          disabled=True,
                          visible=False,
                          key='btn-add')]]
    return layout


def show():
    layout = get_layout()
    frame = [[sg.Frame('', layout)]]
    window = sg.Window("MOLD COMPARISON MATRIX", frame, background_color='#283B5B')

    conditions = dg.eat_pickle('mcm_cond.pkl')

    while True:
        event, values = window.read()
        print(f'event: {event}, \nvalues: {values}')

        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            break

        if event == 'btn-reset':
            # reset filter conditions
            conditions = {'type': '',
                          'brand': '',
                          'mold': '',
                          'speed': '',
                          'glide': '',
                          'turn': '',
                          'fade': '',
                          'stability': ''}

        if event[0] == '-tbl_main-':
            row = event[2][0]
            print(f'ROW: {row}')
            col = event[2][1]
            print(f'COL: {col}')

            table_data = window["-tbl_main-"].get()
            local_df = pd.DataFrame(table_data)
            cell_data = local_df.iloc[row].tolist()[col]

            print(f'CELL DATA: {cell_data}')
            # print(f'PRE-FILTERED DF: {df}')

            if col == 0: # type
                if row == -1: # header => reset
                    # remove condition
                    conditions.update({'type': ''})
                    # lowlight_header(window, 'type')
                else:
                    # add condition
                    conditions.update({'type': cell_data})
                    # highlight_header(window, 'type')

            if col == 1: # brand
                if row == -1: # reset
                    conditions.update({'brand': ''})
                    # lowlight_header(window, 'brand')
                else:
                    conditions.update({'brand': cell_data})
                    # highlight_header(window, 'brand')

            if col == 2: # mold
                if row == -1: # reset
                    conditions.update({'mold': ''})
                    # lowlight_header(window, 'mold')
                else:
                    conditions.update({'mold': cell_data})
                    # highlight_header(window, 'mold')

            if col == 3: # speed
                if row == -1: # reset
                    conditions.update({'speed': ''})
                    # lowlight_header(window, 'speed')
                else:
                    conditions.update({'speed': cell_data})
                    # highlight_header(window, 'speed')

            if col == 4:  # glide
                if row == -1:  # reset
                    conditions.update({'glide': ''})
                    # lowlight_header(window, 'glide')
                else:
                    conditions.update({'glide': cell_data})
                    # highlight_header(window, 'glide')

            if col == 5:  # turn
                if row == -1:  # reset
                    conditions.update({'turn': ''})
                    # lowlight_header(window, 'turn')
                else:
                    conditions.update({'turn': cell_data})
                    # highlight_header(window, 'turn')

            if col == 6:  # fade
                if row == -1:  # reset
                    conditions.update({'fade': ''})
                    # lowlight_header(window, 'fade')
                else:
                    conditions.update({'fade': cell_data})
                    # highlight_header(window, 'fade')

            if col == 7:  # stability
                if row == -1:  # reset
                    conditions.update({'stability': ''})
                    # lowlight_header(window, 'stability')
                else:
                    conditions.update({'stability': cell_data})
                    # highlight_header(window, 'stability')

            # save filter conditions:
            dg.make_pickle(conditions, 'mcm_cond.pkl')

        df = dg.eat_pickle('fdf.pkl')
        fdf = dg.get_filtered_dataframe(df, conditions)

        # save newly filtered data frame
        dg.make_pickle(fdf, 'fdf.pkl')

        # update table with (un)filtered data
        window['-tbl_main-'].update(values=fdf.values.tolist())

        # turn buttons on/off as needed:
        if fdf.shape[0] == 1:
            print(f'FDF COLUMNS:\n{fdf.columns.tolist()}\n')
            columns = fdf.columns.tolist()
            if 'id' not in columns:
                window['btn-add'].update(disabled=False)
                window['btn-add'].update(visible=True)
        else:
            window['btn-add'].update(disabled=True)
            window['btn-add'].update(visible=False)

        enable_reset_button = False
        for k, v in conditions.items():
            if v not in ('', 'All'):
                enable_reset_button = True

        if enable_reset_button:
            window['btn-reset'].update(disabled=False)
        else:
            window['btn-reset'].update(disabled=True)

        if event == 'btn-add':
            dgg.run_window('disc_add_window')


if __name__ == '__main__':
    # create pickle called fdf.pkl (filtered data frame)
    df = get_csv_data_frame()
    df.to_pickle('fdf.pkl')
    show()
