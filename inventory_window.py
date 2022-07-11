import DiscGO as dg
import PySimpleGUI as sg
import DiscGOgui as dgg

import disc_add_edit_window


def get_layout():
    _headings = ['MOLD', 'MANUFACTURER', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'PLASTIC', 'WEIGHT', 'COLOR', 'NOTES']
    _values = dg.get_disc_inventory()
    layout = [
        [sg.Button('ADD DISC')],
        [sg.Table(headings=_headings,
                  values=_values,
                  num_rows=12,
                  key='-tbl_inv-',
                  enable_events=True,
                  enable_click_events=True,
                  justification='left',
                  alternating_row_color='#666666',
                  row_height=25)],
        [sg.Button('GO TO BAG'), sg.Button('CLOSE WINDOW', pad=((485, 10), (10, 10)))]
    ]
    return layout


def show(_layout):
    disc_list = dg.get_disc_inventory()
    window = sg.Window('DISC COLLECTION', _layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == 'CLOSE WINDOW':
            print(f'CLOSED WINDOW')
            window.close()
            break

        elif event == '-tbl_inv-':
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

            # disc_form_window.show(disc_form_window.get_layout(mold))
            disc_add_edit_window.show(disc_add_edit_window.get_edit_disc_layout(disc_id))
            # refresh table rows after saving disc / closing edit window
            # HOW??
            print(f'DISC LIST: {dg.get_disc_inventory()}')

        elif event == 'ADD DISC':
            dgg.show_mold_database()

        else:
            pass


if __name__ == '__main__':
    show(get_layout())
