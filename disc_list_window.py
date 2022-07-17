import DiscGO as dg
import PySimpleGUI as sg


# initialize arrays for table contents
import disc_add_edit_window


def get_layout(disc_list):
    _headings = ['MOLD', 'MANUFACTURER']

    layout = [
        [sg.Table(headings=_headings,
                  values=disc_list,
                  num_rows=12,
                  key='-tbl_list-',
                  enable_events=True,
                  enable_click_events=False,
                  justification='left',
                  alternating_row_color='#666666',
                  row_height=25)],
        [sg.Text(' ', size=20), sg.Button('CLOSE WINDOW')]
    ]
    return layout


def show():
    restart = True
    disc_list = dg.get_all_discs()

    layout = get_layout(disc_list)

    window = sg.Window('MOLD LIST', layout)
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'CLOSE WINDOW':
        print(f'CLOSED WINDOW')
        restart = False
        # window.close()

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

        disc_add_edit_window.show(disc_add_edit_window.get_add_disc_layout(mold))

    if restart:
        show()
    else:
        window.close()


if __name__ == '__main__':
    show()
