import DiscGO as dg
import PySimpleGUI as sg
import pandas as pd


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

    type_data = new_df.pivot_table(index="type", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    mold_data = new_df.pivot_table(index="mold", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    brand_data = new_df.pivot_table(index="brand", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    speed_data = new_df.pivot_table(index="speed", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    stability_data = new_df.pivot_table(index="stability", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    weight_data = new_df.pivot_table(index="weight", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()

    # window['-tbl_type-'].update(values=type_data)
    window['-tbl_mold-'].update(values=mold_data)
    window["-tbl_brand-"].update(values=brand_data)
    window["-tbl_speed-"].update(values=speed_data)
    window["-tbl_stability-"].update(values=stability_data)
    window["-tbl_weight-"].update(values=weight_data)



def update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window, event):
    print(f'type: {TYPE}, brand: {BRAND}, mold: {MOLD}, speed: {SPEED}, stability: {STABILITY}, weight: {WEIGHT}, event: {event}')
    df = get_data_frame()
    print(df)
    filter_count = 0
    FILTER = ''
    # _type = ''
    # _brand = ''
    # _mold = ''
    # _speed = ''
    # _stability = ''
    # _weight = ''

    if TYPE:
        _type = TYPE

    if BRAND:
        _brand = BRAND

    if SPEED:
        _speed = SPEED

    if STABILITY:
        _stability = STABILITY

    if MOLD:
        _mold = MOLD

    if WEIGHT:
        _weight = WEIGHT

    if _type != 'All':
        print(f'FILTER TYPE: {_type}')
        FILTER += f'(df.type=="{_type}") & '
        filter_count += 1
        df = df[df.type == _type] # here's where the magic happens?

    if _mold != 'All':
        print(f'FILTER MOLD: {_mold}')
        FILTER += f'(df.mold=="{_mold}") & '
        filter_count += 1
        df = df[df.mold == _mold] # here's where the magic happens?

    if _speed != 'All':
        print(f'FILTER SPEED: {_speed}')
        FILTER += f'(df.speed=="{_speed}") & '
        filter_count += 1
        df = df[df.speed == _speed] # here's where the magic happens?

    if _brand != 'All':
        print(f'FILTER BRAND: {_brand}')
        FILTER += f'(df.brand=="{_brand}") & '
        filter_count += 1
        df = df[df.brand == _brand] # here's where the magic happens?

    if _stability != 'All':
        print(f'FILTER STAB: {_stability}')
        FILTER += f'(df.stability=="{_stability}") & '
        filter_count += 1
        df = df[df.stability == _stability] # here's where the magic happens?

    if _weight != 'All':
        print(f'FILTER WEIGHT: {_weight}')
        FILTER += f'(df.weight=="{_weight}") & '
        filter_count += 1
        df = df[df.weight == _weight] # here's where the magic happens?

    print(f'FILTER: {FILTER}')
    print(f'filter count: {filter_count}')

    if filter_count > 0:
        FILTER += f'{True}'

    # FILTER = '[' + FILTER + ']'
    print(f'FILTER: "{FILTER}"')

    new_df = df
    print(f'NEW DataFrame: {new_df}')

    type_data = new_df.pivot_table(index="type", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    mold_data = new_df.pivot_table(index="mold", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    brand_data = new_df.pivot_table(index="brand", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    speed_data = new_df.pivot_table(index="speed", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    stability_data = new_df.pivot_table(index="stability", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    weight_data = new_df.pivot_table(index="weight", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    #
    if event != '-tbl_type-':
        window['-tbl_type-'].update(values=type_data)
    if event != '-tbl_mold-':
        window['-tbl_mold-'].update(values=mold_data)
    if event != '-tbl_brand-':
        window["-tbl_brand-"].update(values=brand_data)
    window["-tbl_speed-"].update(values=speed_data)
    window["-tbl_stability-"].update(values=stability_data)
    window["-tbl_weight-"].update(values=weight_data)
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
def get_table_by_filter(_filter): # filter = type, brand, speed, etc.
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
                      key=f"-tbl_{_filter.lower()}-",
                      pad=((20, 10), (10, 10)))]
    return table


def get_frame_by_filter(filter):
    frame = [sg.Frame(filter.upper(), [get_table_by_filter(filter)])]
    return frame


def get_col1():
    return sg.Column([get_frame_by_filter('type'), get_frame_by_filter('brand')])


def get_col2():
    return sg.Column([get_frame_by_filter('mold')])


def get_col3():
    return sg.Column([get_frame_by_filter('speed')])


def get_col4():
    return sg.Column([get_frame_by_filter('stability')])


def get_col5():
    return sg.Column([get_frame_by_filter('weight')])


def get_layout():
    layout = [
        [get_col1(), get_col2(), get_col3(), get_col4(), get_col5()]
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
            row = values["-tbl_type-"][0]
            # print(f'ROW: {row}')
            table_data = window["-tbl_type-"].get()
            df = pd.DataFrame(table_data)
            TYPE = df.iloc[row].tolist()[0]
            # print(f'TYPE: {TYPE}')
            # update_tables_by_type(TYPE, window)
            update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window, event)

        if event == '-tbl_brand-':
            row = values["-tbl_brand-"][0]
            # print(f'ROW: {row}')
            table_data = window["-tbl_brand-"].get()
            df = pd.DataFrame(table_data)
            BRAND = df.iloc[row].tolist()[0]
            # print(f'BRAND: {BRAND}')
            # print(f'TYPE: {TYPE}')
            update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window, event)

        if event == '-tbl_mold-':
            row = values["-tbl_mold-"][0]
            # print(f'ROW: {row}')
            table_data = window["-tbl_mold-"].get()
            df = pd.DataFrame(table_data)
            MOLD = df.iloc[row].tolist()[0]
            print(f'MOLD: {MOLD}')
            update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window, event)
        


def main_loop():
    df = get_data_frame()
    show(get_layout())


if __name__ == '__main__':
    main_loop()
