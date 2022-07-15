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


def update_data_frame(_df):
    df = _df

def get_filtered_data_frame(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT):
    print(f'type: {TYPE}, brand: {BRAND}, mold: {MOLD}, speed: {SPEED}, stability: {STABILITY}, weight: {WEIGHT}')

    df = get_data_frame()
    # print(df)

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

    new_df = df
    print(f'NEW DataFrame: {new_df}')

    return new_df


def update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window, event):
    new_df = get_filtered_data_frame(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT)

    type_data = new_df.pivot_table(index="type", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    mold_data = new_df.pivot_table(index="mold", values="brand", aggfunc="count", margins=True).to_dict()['brand'].items()
    brand_data = new_df.pivot_table(index="brand", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    speed_data = new_df.pivot_table(index="speed", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    stability_data = new_df.pivot_table(index="stability", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()
    weight_data = new_df.pivot_table(index="weight", values="mold", aggfunc="count", margins=True).to_dict()["mold"].items()

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
    # print(f'filter: {_filter}')
    # df = get_data_frame()
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


def get_frame_by_filter(_filter):
    frame = [sg.Frame(_filter.upper(), [get_table_by_filter(_filter)])]
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
    layout = [
        [get_col1(), get_col2(), get_col3(), get_col4(), get_col5(), get_col6()]
    ]
    return layout


def show(layout):
    window = sg.Window('DISC COLLECTION STATISTICS', layout)
    while True:
        event, values = window.read()
        print(f'event: {event}')
        print(f'values: {values}')

        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            break

        if event == '-tbl_type-':
            row = values["-tbl_type-"][0]
            # print(f'ROW: {row}')
            table_data = window["-tbl_type-"].get()
            df = pd.DataFrame(table_data)
            TYPE = df.iloc[row].tolist()[0]
        else:
            TYPE = 'All'

        if event == '-tbl_brand-':
            row = values["-tbl_brand-"][0]
            # print(f'ROW: {row}')
            table_data = window["-tbl_brand-"].get()
            df = pd.DataFrame(table_data)
            BRAND = df.iloc[row].tolist()[0]
        else:
            BRAND = 'All'

        if event == '-tbl_mold-':
            row = values["-tbl_mold-"][0]
            # print(f'ROW: {row}')
            table_data = window["-tbl_mold-"].get()
            df = pd.DataFrame(table_data)
            MOLD = df.iloc[row].tolist()[0]
        else:
            MOLD = 'All'

    # update_tables(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT, window, event)
    df = get_filtered_data_frame(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT)
    # update_data_frame(new_df)
    # main_loop()
# ----------------------------------------------------------------------------------


TYPE = 'All'
BRAND = 'All'
MOLD = 'All'
SPEED = 'All'
STABILITY = 'All'
WEIGHT = 'All'
df = get_filtered_data_frame(TYPE, BRAND, MOLD, SPEED, STABILITY, WEIGHT)
print(f'STARTING DATAFRAME: {df}')


def main_loop():
    # print(f"DATA FRAME: {df}")
    # exit()
    show(get_layout())


if __name__ == '__main__':
    main_loop()
