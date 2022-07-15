import DiscGO as dg
import PySimpleGUI as sg
import DiscGOgui as dgg

import disc_add_edit_window


def get_layout():
    _layout = []
    _layout.append([sg.Button('DISC COLLECTION DATA'), sg.Button('ADD DISC', pad=((450, 10), (10, 10)))])

    _headings = ['MOLD', 'MANUFACTURER', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'PLASTIC', 'WEIGHT', 'COLOR', 'NOTES']
    _values = dg.get_disc_inventory()
    _layout.append(get_inventory_table_layout(_headings, _values))

    _layout.append([sg.Button('GO TO BAG'), sg.Button('THROW INFO', pad=((200, 200), (10, 10))), sg.Button('CLOSE WINDOW')])
    return _layout


def get_inventory_table_layout(_headings, _values):
    _layout = [
        [sg.Table(headings=_headings,
                  values=_values,
                  num_rows=12,
                  key='-tbl_inv-',
                  enable_events=True,
                  enable_click_events=False,
                  justification='left',
                  alternating_row_color='#666666',
                  row_height=25)]
        ]
    return _layout


def show(_layout):
    restart = True
    disc_list = dg.get_disc_inventory()

    window = sg.Window('DiscGO - Disc Golf Data And Number Crunching Experiment', _layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        #event, values = window.read(timeout=15000)
        print(event, values)

        if event == sg.WIN_CLOSED or event == 'CLOSE WINDOW':
            restart = False
            print(f'CLOSED WINDOW')
            window.close()
            break

        if event == '-tbl_inv-':
            # print(f'tbl_list: {values["-tbl_list-"][0]}')
            row = values['-tbl_inv-'][0]
            print(f'row: {row}')

            disc = disc_list[row]

            mold = disc[0]
            brand = disc[1]
            speed = disc[2]
            glide = disc[3]
            turn = disc[4]
            fade = disc[5]
            disc_id = disc[10]

            disc_add_edit_window.show(disc_add_edit_window.get_edit_disc_layout(disc_id))
            # refresh table rows after saving disc / closing edit window
            # HOW??
            print(f'DISC LIST: {dg.get_disc_inventory()}')
            window.close()
            break

        elif event == 'ADD DISC':
            dgg.show_mold_database()
            window.close()
            break

        elif event == 'DISC COLLECTION DATA':
            dgg.show_collection_data()
            break

        print("UH OH - HOW DID WE GET HERE???")

    if restart:
        window.close()
        main_loop()


def main_loop():
    print('RUNNING MAIN LOOP')
    show(get_layout())


if __name__ == '__main__':
    dg.create_db()
    main_loop()
