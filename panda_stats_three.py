import DiscGO as dg
import PySimpleGUI as sg
import pandas as pd

conditions = {'type': '',
              'brand': '',
              'mold': '',
              'speed': '',
              'stability': '',
              'plastic': '',
              'weight': ''}


def get_data_frame():
    sql = '''
         SELECT 
            inventory.mold,
            inventory.brand,
            inventory.speed,
            inventory.glide,
            inventory.turn,
            inventory.fade,
            (inventory.turn + inventory.fade) as stability,
            inventory.plastic,
            inventory.weight,
            inventory.color,
            inventory.notes,
            disc.type,
            inventory.id
        FROM 
            INVENTORY
        JOIN
            disc
            on
            disc.mold like inventory.mold
        ORDER BY
            brand, inventory.mold
        '''
    df = pd.read_sql_query(sql, dg.db_connect())
    return df


def update_tables_by_type(TYPE, window):
    df = get_data_frame()
    if TYPE == 'All':
        new_df = df
    else:
        new_df = df[df.type == TYPE]

    type_data = new_df.pivot_table(index="type", values="brand", aggfunc="count", margins=True).to_dict()[
        'brand'].items()
    mold_data = new_df.pivot_table(index="mold", values="brand", aggfunc="count", margins=True).to_dict()[
        'brand'].items()
    brand_data = new_df.pivot_table(index="brand", values="mold", aggfunc="count", margins=True).to_dict()[
        "mold"].items()
    speed_data = new_df.pivot_table(index="speed", values="mold", aggfunc="count", margins=True).to_dict()[
        "mold"].items()
    stability_data = new_df.pivot_table(index="stability", values="mold", aggfunc="count", margins=True).to_dict()[
        "mold"].items()
    weight_data = new_df.pivot_table(index="weight", values="mold", aggfunc="count", margins=True).to_dict()[
        "mold"].items()

    # window['-tbl_type-'].update(values=type_data)
    window['-tbl_mold-'].update(values=mold_data)
    window["-tbl_brand-"].update(values=brand_data)
    window["-tbl_speed-"].update(values=speed_data)
    window["-tbl_stability-"].update(values=stability_data)
    window["-tbl_weight-"].update(values=weight_data)


def get_filtered_dataframe(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT):
    # start with full data frame, then apply filters
    df = get_data_frame()
    print(df)

    if TYPE != 'All':
        print(f'FILTER TYPE: {TYPE}')
        df = df[df.type == TYPE]  # here's where the magic happens?

    if MOLD != 'All':
        print(f'FILTER MOLD: {MOLD}')
        df = df[df.mold == MOLD]  # here's where the magic happens?

    if SPEED != 'All':
        print(f'FILTER SPEED: {SPEED}')
        df = df[df.speed == SPEED]  # here's where the magic happens?

    if BRAND != 'All':
        print(f'FILTER BRAND: {BRAND}')
        df = df[df.brand == BRAND]  # here's where the magic happens?

    if STABILITY != 'All':
        print(f'FILTER STAB: {STABILITY}')
        df = df[df.stability == STABILITY]  # here's where the magic happens?

    if WEIGHT != 'All':
        print(f'FILTER WEIGHT: {WEIGHT}')
        df = df[df.weight == WEIGHT]  # here's where the magic happens?

    print(f'FILTERED DataFrame: {df}')

    return df


def update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window):
    print(f'type: {TYPE}, brand: {BRAND}, mold: {MOLD}, speed: {SPEED}, stability: {STABILITY}, weight: {WEIGHT}')

    fdf = get_filtered_dataframe(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT)

    type_data = fdf.pivot_table(index="type", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    mold_data = fdf.pivot_table(index="mold", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    brand_data = fdf.pivot_table(index="brand", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    speed_data = fdf.pivot_table(index="speed", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    stability_data = fdf.pivot_table(index="stability", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    weight_data = fdf.pivot_table(index="weight", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()

    window['-tbl_type-'].update(values=type_data)
    window['-tbl_mold-'].update(values=mold_data)
    window["-tbl_brand-"].update(values=brand_data)
    window["-tbl_speed-"].update(values=speed_data)
    window["-tbl_stability-"].update(values=stability_data)
    window["-tbl_weight-"].update(values=weight_data)

    window['-frm_type-'].update(TYPE)
    window['-frm_mold-'].update(MOLD)
    window["-frm_brand-"].update(BRAND)
    window["-frm_speed-"].update(SPEED)
    window["-frm_stability-"].update(STABILITY)
    window["-frm_weight-"].update(WEIGHT)
    ### end update_tables()


def get_disc_count_by_filter(_filter):
    print(f'filter: {_filter}')
    df = get_data_frame()
    if _filter == 'mold':
        pivot = df.pivot_table(index="mold", values="brand", aggfunc="count", margins=True)
        rows = pivot.to_dict()['brand'].items()
    else:
        pivot = df.pivot_table(index=_filter, values="mold", aggfunc="count", margins=True)
        rows = pivot.to_dict()['mold'].items()
    return rows


# logic code above
# GUI code below
def get_table_by_filter(_filter):  # filter = type, brand, speed, etc.
    _headings = [f'{_filter.upper()}', 'COUNT']
    _values = get_disc_count_by_filter(_filter)
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='right',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=min(13, len(_values)),
                      enable_click_events=False,
                      enable_events=True,
                      header_text_color='#CC3333',
                      key=f"-tbl_{_filter.lower()}-",
                      pad=((20, 10), (10, 10)))]
    return table


def get_frame_by_filter(_filter):
    frame = [sg.Frame('', [[sg.Text('ALL', key=f"-frm_{_filter.lower()}-")], get_table_by_filter(_filter)])]
    return frame


def get_col1():
    return sg.Column([get_frame_by_filter('type')])


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
    layout = [sg.vtop([get_col1(), get_col2(), get_col3(), get_col4(), get_col5(), get_col6()])
    ]
    return layout


def show(layout):
    window = sg.Window('DISC COLLECTION STATISTICS', layout)
    # ------ Event Loop ------
    TYPE = 'All'
    BRAND = 'All'
    MOLD = 'All'
    SPEED = 'All'
    STABILITY = 'All'
    WEIGHT = 'All'

    while True:
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
        if event == '-tbl_type-':
            print(f'TBL_TYPE EVENT VALUES: {values}')
            # row number stored in values['-tbl-key-'][0]
            if values['-tbl_type-']:
                row = values["-tbl_type-"][0]

                # print(f'ROW: {row}')
                table_data = window["-tbl_type-"].get()
                df = pd.DataFrame(table_data)
                TYPE = df.iloc[row].tolist()[0]
                # print(f'TYPE: {TYPE}')

        if event == '-tbl_brand-':
            if values['-tbl_brand-']:
                row = values["-tbl_brand-"][0]
                # print(f'ROW: {row}')
                table_data = window["-tbl_brand-"].get()
                df = pd.DataFrame(table_data)
                BRAND = df.iloc[row].tolist()[0]
                # print(f'BRAND: {BRAND}')

        if event == '-tbl_mold-':
            if values['-tbl_mold-']:
                row = values["-tbl_mold-"][0]
                # print(f'ROW: {row}')
                table_data = window["-tbl_mold-"].get()
                df = pd.DataFrame(table_data)
                MOLD = df.iloc[row].tolist()[0]
                # print(f'MOLD: {MOLD}')

        if event == '-tbl_speed-':
            if values['-tbl_speed-']:
                row = values["-tbl_speed-"][0]
                # print(f'ROW: {row}')
                table_data = window["-tbl_speed-"].get()
                df = pd.DataFrame(table_data)
                SPEED = df.iloc[row].tolist()[0]

        if event == '-tbl_stability-':
            if values['-tbl_stability-']:
                row = values["-tbl_stability-"][0]
                # print(f'ROW: {row}')
                table_data = window["-tbl_stability-"].get()
                df = pd.DataFrame(table_data)
                STABILITY = df.iloc[row].tolist()[0]

        update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window)


def main_loop():
    # df = get_data_frame()
    show(get_layout())


if __name__ == '__main__':
    main_loop()
