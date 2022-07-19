import DiscGO as dg
import PySimpleGUI as sg

import mold_info_window


def get_layout():
    fdf = dg.eat_pickle('fdf.pkl')
    print(f'GET_LAYOUT: \n{fdf.values.tolist()}')

    values = fdf.values.tolist()
    headings = [f'{"TYPE" : ^8}',
                f'{"BRAND" : ^15}',
                f'{"MOLD" : ^20}',
                f'{"SPEED" : ^5}',
                f'{"GLIDE" : ^5}',
                f'{"TURN" : ^5}',
                f'{"FADE" : ^5}']

    color = '#CC3333'
    plastics = ['DX', 'Star', 'Champion']
    plastic = 'choose'
    weight = '175'
    notes = ''

    layout = [[sg.Table(headings=headings,
                        values=values,
                        num_rows=1,
                        key='-tbl_inv-',
                        enable_events=True,
                        enable_click_events=False,
                        justification='left',
                        alternating_row_color='#283B5B',
                        header_text_color='#CC3333',
                        row_height=35)],
              [sg.Text('PLASTIC',
                       pad=((5, 50), (10, 10))),
               sg.Text('WEIGHT',
                       pad=((20, 50), (10, 10))),
               sg.Text('COLOR')],
              [sg.Combo(values=plastics,
                        default_value=plastic,
                        size=12,
                        pad=((5, 27), (0, 10)),
                        key='-plastic-'),
               sg.In(weight,
                     size=4,
                     pad=((5, 65), (0, 10)),
                     key='-weight-'),
              sg.ColorChooserButton('SELECT', target='-color-'),
               sg.In(color, size=8, enable_events=True, key='-color-'),
               sg.DummyButton('', size=(11, 2), button_color=(color, color), disabled=True, key='-swatch-')],
              [sg.In(color, visible=False, key='-secret-color-')],
              [sg.Text('NOTES')],
              [sg.In(notes,
                     size=30,
                     key='-notes-'),
               sg.Button('ADD DISC',
                         pad=((320, 10), (10, 10)),
                         key='btn-add',
                         disabled_button_color=('white', '#64778D'),
                         disabled=True)]
              ]
    return layout


def show():
    layout = get_layout()

    window = sg.Window('ADD DISC', layout)

    while True:
        event, values = window.read()
        print(f'event: {event}\nvalues: {values}')

        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == '-color-':
            if values['-color-'] != 'None':
                color = values['-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-secret-color-'].update(values['-color-'])
            else:
                color = values['-secret-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-color-'].update(values['-secret-color-'])


if __name__ == '__main__':
    # dg.create_db()
    # disc_list = dg.get_disc_inventory()
    show()

