import sqlite3
import pandas as pd
import DiscGO as dg
import PySimpleGUI as sg


def db_connect():
    return sqlite3.connect('./disc_db.db')


# rows = dg.get_disc_inventory()

# df = pd.DataFrame(rows)

sql = '''
     SELECT 
        disc.type,
        inventory.brand,
        inventory.mold,
        inventory.speed,
        inventory.glide,
        inventory.turn,
        inventory.fade,
        (inventory.turn + inventory.fade) as stability,
        inventory.plastic,
        inventory.weight
    FROM 
        INVENTORY
    JOIN
        disc
        on
        disc.mold like inventory.mold
    ORDER BY
        brand, inventory.mold
    '''

gray = '#999999'
red = '#993333'


def get_layout(_df):
    _data = _df.values.tolist()
    print(f'data: {_data}')
    header_list = ['TYPE', 'BRAND', 'MOLD', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'STABILITY', 'PLASTIC', 'WEIGHT']
    print(f'header_list: {header_list}')


    _layout = [[sg.Text('ALL',
                        text_color=gray,
                        key='type-reset',
                        pad=((35, 40), (5, 5))),
                sg.Text('ALL',
                        text_color=gray,
                        key='brand-reset',
                        pad=((20, 40), (5, 5))),
                sg.Text('ALL',
                        text_color=gray,
                        key='mold-reset',
                        pad=((30, 10), (5, 5))),
                sg.Text('ALL',
                        text_color=gray,
                        key='speed-reset',
                        pad=((30, 140), (5, 5))),
                sg.Text('ALL',
                        text_color=gray,
                        key='stability-reset',
                        pad=((10, 40), (5, 5))),
                ],
               [sg.Table(headings=header_list,
                         values=_data,
                         justification='right',
                         alternating_row_color='#666666',
                         row_height=30,
                         num_rows=min(13, len(_data)),
                         enable_click_events=True,
                         enable_events=False,
                         key="-tbl_main-",
                         pad=((20, 10), (10, 10)))]]
    return _layout


df = pd.read_sql_query(sql, db_connect())

print('df:')
print(df)

# make new column from existing columns
# df['stability'] = df['turn'] + df['fade']
# print(df.stability)

conditions = {'type': '',
              'brand': '',
              'mold': '',
              'speed': '',
              'stability': '',
              'plastic': '',
              'weight': ''}

window = sg.Window("Panda test window", get_layout(df))

while True:
    event, values = window.read()
    print(f'event: {event[0]}, \nvalues: {values}')

    if event == sg.WIN_CLOSED:
        print(f'CLOSED WINDOW')
        window.close()
        break

    elif event[0] == '-tbl_main-':
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
                window['type-reset'].update('ALL')
                window['type-reset'].update(text_color=gray)
            else:
                # add condition
                conditions.update({'type': cell_data})
                window['type-reset'].update(conditions['type'])
                window['type-reset'].update(text_color=red)

        if col == 1: # brand
            if row == -1: # reset
                conditions.update({'brand': ''})
                window['brand-reset'].update('ALL')
                window['brand-reset'].update(text_color=gray)
            else:
                conditions.update({'brand': cell_data})
                window['brand-reset'].update(conditions['brand'])
                window['brand-reset'].update(text_color=red)

        if col == 2: # mold
            if row == -1: # reset
                conditions.update({'mold': ''})
                window['mold-reset'].update('ALL')
                window['mold-reset'].update(text_color=gray)
            else:
                conditions.update({'mold': cell_data})
                window['mold-reset'].update(conditions['mold'])
                window['mold-reset'].update(text_color=red)

        if col == 3: # speed
            if row == -1: # reset
                conditions.update({'speed': ''})
                window['speed-reset'].update('ALL')
                window['speed-reset'].update(text_color=gray)
            else:
                conditions.update({'speed': cell_data})
                window['speed-reset'].update(conditions['speed'])
                window['speed-reset'].update(text_color=red)

        if col == 7:  # stability
            if row == -1:  # reset
                conditions.update({'stability': ''})
                window['stability-reset'].update('ALL')
                window['stability-reset'].update(text_color=gray)
            else:
                conditions.update({'stability': cell_data})
                window['stability-reset'].update(conditions['stability'])
                window['stability-reset'].update(text_color=red)

        # reset dataframe, then filter
        df = pd.read_sql_query(sql, db_connect())

        print(f'CONDITIONS: {conditions}')
        if conditions["type"] != '':
            print('FILTERING ON TYPE')
            df = df[df["type"] == conditions["type"]]

        if conditions["brand"] != '':
            print('FILTERING ON BRAND')
            df = df[df["brand"] == conditions["brand"]]

        if conditions["mold"] != '':
            print('FILTERING ON MOLD')
            df = df[df["mold"] == conditions["mold"]]

        if conditions["speed"] != '':
            print('FILTERING ON SPEED')
            df = df[df["speed"] == conditions["speed"]]

        if conditions["stability"] != '':
            print('FILTERING ON MOLD')
            df = df[df["stability"] == conditions["stability"]]

        print(f'FILTERED DF: {df}')

        # update table with (un)filtered data
        window['-tbl_main-'].update(values=df.values.tolist())

