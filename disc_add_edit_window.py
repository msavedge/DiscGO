import DiscGO as dg
import PySimpleGUI as sg

import mold_info_window


def get_add_mold_layout(_mold):
    print(f'ADD MOLD LAYOUT _mold: {_mold}')
    dummy_disc_id = 0
    mold = _mold

    mold_info_layout = mold_info_window.get_layout(mold)
    disc_detail_layout = get_disc_detail_layout(dummy_disc_id, mold)

    layout = []
    layout.append(mold_info_layout)
    layout.append(disc_detail_layout)
    layout.append(add_button_row())
    return layout


def get_edit_disc_layout(disc_id):
    disc = dg.get_disc_from_inventory(disc_id)
    mold = disc[0]

    mold_info_layout = mold_info_window.get_layout(mold)
    disc_detail_layout = get_disc_detail_layout(disc_id, '')

    layout = []
    layout.append(mold_info_layout)
    layout.append(disc_detail_layout)
    layout.append(edit_button_row())
    return layout


def get_disc_detail_layout(disc_id, _mold):
    # set (dummy) disc_id and mold based on conditions:
    if disc_id == 0:
        disc = dummy_disc = ('mold', 'brand', 0.0, 0.0, 0.0, 0.0, 'select', '', '#000000', '', 0)
        mold = _mold
    else:
        disc = dg.get_disc_from_inventory(disc_id)
        mold = disc[0]

    print(f'DISC INFO: {disc}')

    brand = disc[1]
    speed = disc[2]
    glide = disc[3]
    turn = disc[4]
    fade = disc[5]
    plastic = disc[6]
    weight = disc[7]
    color = disc[8]
    notes = disc[9]
    disc_id = disc[10]

    plastics = dg.get_plastics_for_mold(mold)
    print(f'FOUND SOME PLASTIC: {plastics}')

    _layout = [
        [sg.Text(' '),
         sg.In(disc_id, visible=False, key='-disc_id-'),
         sg.In(brand, visible=False, key='-brand-'),
         sg.In(speed, visible=False, key='-speed-'),
         sg.In(glide, visible=False, key='-glide-'),
         sg.In(turn, visible=False, key='-turn-'),
         sg.In(fade, visible=False, key='-fade-')],
        [sg.Text('COLOR')],
        [sg.ColorChooserButton('SELECT', target='-color-'),
         sg.In(f'{color.upper()}', size=8, enable_events=True, key='-color-'),
         sg.DummyButton('', size=(11, 1), button_color=(color, color), disabled=True, key='-swatch-')],
        [sg.In(color, visible=False, key='-secret-color-')],
        [sg.Text('PLASTIC'),
         sg.Text(' ', size=8),
         sg.Text('WEIGHT')],
        [sg.Combo(values=plastics, default_value=plastic, size=12, key='-plastic-'),
         sg.Text(' ', size=2),
         sg.In(weight, size=4, key='-weight-')],
        [sg.Text('NOTES')],
        [sg.In(notes, size=40, key='-notes-')],
        [sg.Text('')],
    ]
    return _layout


def edit_button_row():
    _layout = [
        [sg.Button('SAVE', visible=False),
         sg.Text(' ', size=2),
         sg.Button('DELETE DISC', button_color=('red', 'white')),
         sg.Text(' ', size=2),
         sg.Button('CLOSE')],
    ]
    return _layout


def add_button_row():
    _layout = [
        [sg.Button('ADD DISC'),
         sg.Text(' ', size=18),
         sg.Button('CANCEL')],
    ]
    return _layout


def show(_layout):
    window = sg.Window('DISC DETAILS', _layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'CLOSE' or event == 'CANCEL':
            print('SAVING DISC STATUS')
            disc_id = values['-disc_id-']

            plastic = values['-plastic-'][0]
            print(f'plastic: {plastic}')

            weight = values['-weight-']
            color = values['-color-']
            notes = values['-notes-']

            dg.update_disc_in_inventory(disc_id, plastic, weight, color, notes)

            print(f'CLOSED WINDOW')
            window.close()
            break

        elif event == 'CANCEL': # user decided to not add disc
            print('CANCELLED DISC ADD')
            window.close()
            break

        if event == '-color-': # clicked color picker button

            if values['-color-'] == 'None':
                print('BLACK and WHITE')
                color = values['-secret-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-color-'].update(values['-secret-color-'])
            else:
                print(f'FOUND A COLOR: {values["-color-"]}')
                color = values['-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-secret-color-'].update(values['-color-'])

        elif event == 'ADD DISC':
            # mold = disc[0]
            # brand = disc[1]
            # speed = disc[2]
            # glide = disc[3]
            # turn = disc[4]
            # fade = disc[5]
            # plastic = disc[6]
            # weight = disc[7]
            # color = disc[8]
            # notes = disc[9]
            # disc_id = disc[10]

            print('< EVENT = ADD >')

            disc_definition = {
                'mold':         values["-mold-"].upper(),
                'manufacturer': values['-brand-'].upper(),
                'speed':        values['-speed-'],
                'glide':        values['-glide-'],
                'turn':         values['-turn-'],
                'fade':         values['-fade-'],
                'plastic':      values['-plastic-'][0],
                'weight':       values['-weight-'],
                'color':        values['-color-'],
                'notes':        values['-notes-']
            }

            # print(f'MADE UP DISC: {disc}')

            # save disc details in database:
            print("saving disc info")
            dg.add_mold_to_inventory(disc_definition)
            window.close()
            sg.PopupOK(f'{values["-mold-"]} saved')
            break

        elif event == 'DELETE DISC':
            yes_no = sg.popup_yes_no("DO YOU REALLY WANT TO",
                                     f"DELETE THIS {values['-mold-']}?",
                                     '',
                                     "THIS OPERATION CANNOT",
                                     "BE UNDONE.",
                                     "")
            if yes_no == 'Yes':
                disc_id = values['-disc_id-']
                print(f'deleting disc {disc_id}')
                dg.remove_disc_from_inventory(disc_id)
                # sg.popup(f'the {values["-mold-"].upper()} has been eliminated.')
                window.close()
                break


if __name__ == '__main__':
    # show(get_add_mold_layout('kaxe'))
    # pig number one is disc_id = 2 <- DON'T DELETE IT!!
    show(get_edit_disc_layout(2))
