import DiscGO as dg
import PySimpleGUI as sg


# initialize arrays for table contents
import disc_add_edit_window


def get_layout():
    _headings = ['MOLD', 'MANUFACTURER']
    # _values used in table
    # disc_list used in app logic below
    _values = disc_list = dg.get_all_discs()

    layout = [
        [sg.Table(headings=_headings,
                  values=_values,
                  num_rows=12,
                  key='-tbl_list-',
                  enable_events=True,
                  enable_click_events=True,
                  justification='left',
                  alternating_row_color='#666666',
                  row_height=25)],
        [sg.Text(' ', size=20), sg.Button('CLOSE WINDOW')]
    ]
    return layout


def show(_layout):
    disc_list = dg.get_all_discs()
    window = sg.Window('MOLD LIST', _layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            break
        elif event == 'CLOSE WINDOW':
            window.close()
            break

        elif event == '-tbl_list-':
            # print(f'tbl_list: {values["-tbl_list-"][0]}')
            row = values['-tbl_list-'][0]
            disc = disc_list[row]

            mold = disc[0]
            brand = disc[1]
            speed = disc[2]
            glide = disc[3]
            turn = disc[4]
            fade = disc[5]

            disc_add_edit_window.show(disc_add_edit_window.get_add_mold_layout(mold))
            break

    window.close()
    return event, values


if __name__ == '__main__':
    show(get_layout())
