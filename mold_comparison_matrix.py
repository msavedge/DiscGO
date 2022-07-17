import sqlite3
import pandas as pd
import DiscGO as dg
import PySimpleGUI as sg
import pickle


def get_csv_data_frame():
    return pd.read_csv('./mold_master_list.csv')


def get_fdf():  # filtered data frame - this is the comparison matrix
    return pd.read_pickle('fdf.pkl')


gray = '#FFFFFF'
red = '#CC3333'


def get_layout():
    _df = pd.read_pickle('fdf.pkl')
    _data = _df.values.tolist()
    print(f'data: {_data}')
    # pad header text to set min column widths for table - keeps filter flags from shifting as much
    header_list = [' TYPE ', '     BRAND     ', '    MOLD    ', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'STABILITY']
    print(f'header_list: {header_list}')

    row_count = _df.shape[0]
    if row_count > 10:
        row_count = 10

    _layout = [[sg.Text('ALL',
                        text_color=gray,
                        key='type-reset',
                        pad=((40, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='brand-reset',
                        pad=((65, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='mold-reset',
                        pad=((105, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='speed-reset',
                        pad=((60, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='glide-reset',
                        pad=((10, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='turn-reset',
                        pad=((5, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='fade-reset',
                        pad=((10, 10), (5, 0))),
                sg.Text('ALL',
                        text_color=gray,
                        key='stability-reset',
                        pad=((20, 10), (5, 0))),
                ],
               [sg.Table(headings=header_list,
                         values=_data,
                         justification='right',
                         alternating_row_color='#666666',
                         row_height=30,
                         num_rows=min(len(_data), 10),
                         enable_click_events=True,
                         enable_events=False,
                         header_border_width=2,
                         header_text_color=red,
                         key="-tbl_main-",
                         pad=((20, 10), (10, 10)))],
               [sg.Button('RESET', pad=((20, 450), (5, 10))), sg.Button('ADD DISC', pad=(20, 5))]]
    return _layout


conditions = {'type': '',
              'brand': '',
              'mold': '',
              'speed': '',
              'glide': '',
              'turn': '',
              'fade': '',
              'stability': ''}

file = open('mcm_cond.pkl', 'wb')
pickle.dump(conditions, file)
file.close()

# file = open('mcm_cond.pkl', 'rb')
# conditions = pickle.load(file)
# file.close()

print(f'UNPICKLED CONDITIONS: {conditions}')


def get_filtered_dataframe(conditions):
        # reset dataframe, then filter
        df = get_fdf()
        # convert these to list comprehensions?
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

        if conditions["glide"] != '':
            print('FILTERING ON GLIDE')
            df = df[df["glide"] == conditions["glide"]]

        if conditions["turn"] != '':
            print('FILTERING ON TURN')
            df = df[df["turn"] == conditions["turn"]]

        if conditions["fade"] != '':
            print('FILTERING ON FADE')
            df = df[df["fade"] == conditions["fade"]]

        if conditions["stability"] != '':
            print('FILTERING ON STABILITY')
            df = df[df["stability"] == conditions["stability"]]

        print(f'FILTERED DF: {df}')
        return df

def show(layout):
    window = sg.Window("MOLD COMPARISON MATRIX", layout)

    file = open('mcm_cond.pkl', 'rb')
    conditions = pickle.load(file)
    file.close()

    while True:
        event, values = window.read()
        print(f'event: {event}, \nvalues: {values}')

        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            break

        if event == 'RESET':
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
                    window['type-reset'].update('ALL')
                    window['type-reset'].update(text_color=gray)
                else:
                    # add condition
                    conditions.update({'type': cell_data})
                    window['type-reset'].update('      ')
                    window['type-reset'].update(text_color=red)

            if col == 1: # brand
                if row == -1: # reset
                    conditions.update({'brand': ''})
                    window['brand-reset'].update('ALL')
                    window['brand-reset'].update(text_color=gray)
                else:
                    conditions.update({'brand': cell_data})
                    window['brand-reset'].update('      ')
                    window['brand-reset'].update(text_color=red)

            if col == 2: # mold
                if row == -1: # reset
                    conditions.update({'mold': ''})
                    window['mold-reset'].update('ALL')
                    window['mold-reset'].update(text_color=gray)
                else:
                    conditions.update({'mold': cell_data})
                    window['mold-reset'].update('      ')
                    window['mold-reset'].update(text_color=red)

            if col == 3: # speed
                if row == -1: # reset
                    conditions.update({'speed': ''})
                    window['speed-reset'].update('ALL')
                    window['speed-reset'].update(text_color=gray)
                else:
                    conditions.update({'speed': cell_data})
                    window['speed-reset'].update('      ')
                    window['speed-reset'].update(text_color=red)

            if col == 4:  # glide
                if row == -1:  # reset
                    conditions.update({'glide': ''})
                    window['glide-reset'].update('ALL')
                    window['glide-reset'].update(text_color=gray)
                else:
                    conditions.update({'glide': cell_data})
                    window['glide-reset'].update('      ')
                    window['glide-reset'].update(text_color=red)

            if col == 5:  # turn
                if row == -1:  # reset
                    conditions.update({'turn': ''})
                    window['turn-reset'].update('ALL')
                    window['turn-reset'].update(text_color=gray)
                else:
                    conditions.update({'turn': cell_data})
                    window['turn-reset'].update('      ')
                    window['turn-reset'].update(text_color=red)

            if col == 6:  # fade
                if row == -1:  # reset
                    conditions.update({'fade': ''})
                    window['fade-reset'].update('ALL')
                    window['fade-reset'].update(text_color=gray)
                else:
                    conditions.update({'fade': cell_data})
                    window['fade-reset'].update('      ')
                    window['fade-reset'].update(text_color=red)

            if col == 7:  # stability
                if row == -1:  # reset
                    conditions.update({'stability': ''})
                    window['stability-reset'].update('ALL')
                    window['stability-reset'].update(text_color=gray)
                else:
                    conditions.update({'stability': cell_data})
                    window['stability-reset'].update('   ')
                    window['stability-reset'].update(text_color=red)

            # save filter conditions:
            file = open('mcm_cond.pkl', 'wb')
            pickle.dump(conditions, file)
            file.close()

        fdf = get_filtered_dataframe(conditions)
        # update table with (un)filtered data
        window['-tbl_main-'].update(values=fdf.values.tolist())


if __name__ == '__main__':
    # create pickle called fdf.pkl (filtered data frame)
    df = get_csv_data_frame()
    df.to_pickle('fdf.pkl')
    show(get_layout())
