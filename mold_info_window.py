import DiscGO as dg
import PySimpleGUI as sg

import disc_add_edit_window


def get_layout(mold_name):
    mold_info = dg.get_mold_info(mold_name)
    print(f'mold_info: {mold_info}')
    brand = mold_info[0]
    print(f'brand: {brand}')
    mold = mold_info[1].upper()
    speed = mold_info[2]
    glide = mold_info[3]
    turn = mold_info[4]
    fade = mold_info[5]
    brand_id = mold_info[6]

    gray = '#CCCCCC'
    layout = [
        [sg.Text(mold, size=15),
         sg.Text(brand, size=15),
         sg.Button('STATS', disabled=True, visible=False)],
        [sg.In(brand, visible=False, key='-brand-')],
        [sg.Text(''),
         sg.In(mold, visible=False, key='-mold-')],
        [sg.Text(' ', size=3),
         sg.Text('SPEED', size=(6, 1), text_color=gray),
         sg.Text('GLIDE', size=(6, 1), text_color=gray),
         sg.Text('TURN', size=(6, 1), text_color=gray),
         sg.Text('FADE', size=(6, 1), text_color=gray)],
        [sg.Text(' ', size=4),
         sg.Text(speed, size=(6, 1)),
         sg.Text(glide, size=(6, 1)),
         sg.Text(turn, size=(6, 1)),
         sg.Text(fade, size=(6, 1))],
        [sg.In(speed, size=(6, 1), visible=False, key='-speed-'),
         sg.In(glide, size=(6, 1), visible=False, key='-glide-'),
         sg.In(turn, size=(6, 1), visible=False, key='-turn-'),
         sg.In(fade, size=(6, 1), visible=False, key='-fade-')],
    ]

    return layout


def add_button_row():
    _layout = [
        [sg.Text('')],
        [sg.Button('ADD TO COLLECTION'), sg.Text('', size=2), sg.Button('CLOSE WINDOW')]
    ]
    return _layout


def show(_layout):
    # _layout.append(add_button_row())
    window = sg.Window('MOLD INFO', _layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'CLOSE WINDOW':
            print(f'CLOSED WINDOW')
            break
        elif event == 'ADD TO COLLECTION':
            print('add to bag:')
            disc_add_edit_window.show(disc_add_edit_window.get_add_mold_layout(values['-mold-']))


if __name__ == '__main__':
    mold = 'pig'
    show(get_layout(mold))