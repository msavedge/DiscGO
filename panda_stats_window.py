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


def get_disc_count_by_filter(_filter):
    print(f'filter: {_filter}')
    df = get_data_frame()
    if _filter == 'mold':
        pivot = df.pivot_table(index="mold", values="brand", aggfunc="count")
        rows = pivot.to_dict()['brand'].items()
    else:
        pivot = df.pivot_table(index=_filter, values="mold", aggfunc="count")
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
                      enable_events=False,
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
    while True:
        event, values = window.read()
        print(f'event: {event}')
        print('')
        print(f'values: {values}')

        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            break


if __name__ == '__main__':
    show(get_layout())
