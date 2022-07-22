import DiscGO as dg
import PySimpleGUI as sg

# sg.theme('Dark Blue 3')


def get_layout(disc_list):
    values = disc_list
    disc = values[0]

    print(f'GET LAYOUT TABLE VALUES <edit window>:\n{values}')

    headings = [f'{"TYPE" : ^8}',
                f'{"BRAND" : ^15}',
                f'{"MOLD" : ^20}',
                f'{"SPEED" : ^5}',
                f'{"GLIDE" : ^5}',
                f'{"TURN" : ^5}',
                f'{"FADE" : ^5}']

    layout = [[sg.Table(headings=headings,
                        values=values,
                        num_rows=1,
                        key='-tbl_inv-',
                        enable_events=True,
                        enable_click_events=False,
                        justification='left',
                        hide_vertical_scroll=True,
                        header_text_color='#CC3333',
                        row_height=35)],
              [sg.Text('PLASTIC',
                       pad=((5, 50), (10, 10))),
               sg.Text('WEIGHT',
                       pad=((20, 50), (10, 10))),
               sg.Text('COLOR')],
              [sg.Input(disc[7],
                        size=14,
                        pad=((5, 27), (0, 10)),
                        enable_events=True,
                        key='-plastic-'),
               sg.In(disc[8],
                     size=4,
                     pad=((5, 65), (0, 10)),
                     enable_events=True,
                     key='-weight-'),
              sg.ColorChooserButton('SELECT', target='-color-'),
               sg.In(disc[9], size=8, enable_events=True, key='-color-'),
               sg.DummyButton('', size=(15, 1), button_color=(disc[9], disc[9]), disabled=True, key='-swatch-')],
              [sg.In('', visible=False, key='-secret-color-')],
              [sg.Text('NOTES')],
              [sg.In(disc[10],
                     size=30,
                     key='-notes-'),
               sg.Button('DELETE DISC',
                         pad=((80, 120), (10, 10)),
                         key='btn-delete',
                         button_color=('#CC3333', 'white')),
               sg.Button('SAVE',
                         size=11,
                         pad=((10, 10), (10, 10)),
                         key='btn-save',
                         disabled=False)]
              ]
    return layout


def show():
    # fdf should be single row if we got this far
    disc_id = dg.eat_pickle('disc_id.pkl')
    # turn into a [list] because it's a single row & sg.Table only reads enumerables
    disc_list = [dg.get_disc_from_collection(disc_id)]

    layout = get_layout(disc_list)
    frame = [[sg.Frame('', layout)]]
    window = sg.Window('EDIT DISC', frame, background_color='#CC3333')

    while True:
        event, values = window.read()
        print(f'event: {event}\nvalues: {values}')

        if event == sg.WIN_CLOSED:
            window.close()
            break

        # form validation - require plastic, weight and color to activate 'add' button
        if len(values['-plastic-']) >= 2 and len(values['-weight-']) == 3 and len(values['-color-']) > 5:
            window['btn-save'].update(disabled=False)
        else:
            window['btn-save'].update(disabled=True)

        if event == '-color-':
            if values['-color-'] != 'None':  # value returned if user hits cancel button
                color = values['-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-secret-color-'].update(values['-color-'])
            else:
                color = values['-secret-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-color-'].update(values['-secret-color-'])

        if event == 'btn-save':
            # first & only element in list:
            disc = disc_list[0]
            # pull the mold name out of the disc:
            mold = disc[2]
            plastic = values['-plastic-']
            weight = values['-weight-']
            color = values['-color-']
            notes = values['-notes-']

            disc_id = dg.eat_pickle('disc_id.pkl')

            # print(f'DISC:\n{disc}')
            # print(f'MOLD:\n{mold}')

            disc = {'mold': mold,
                    'plastic': plastic,
                    'weight': weight,
                    'color': color,
                    'notes': notes,
                    'id': disc_id}

            dg.update_disc_in_collection(disc)
#           # popup confirming successful add
            window.close()
            # sg.theme('BrightColors')
            # sg.PopupOK('DISC SAVED', background_color='#283B5B')
            # sg.theme('Default')
            break

        elif event == 'btn-delete':
            # first & only element in list:
            disc = disc_list[0]
            # pull the mold name out of the disc:
            mold = disc[2]

            yes_no = sg.popup_yes_no("DO YOU REALLY WANT TO",
                                     f"DELETE THIS {mold}?",
                                     '',
                                     "THIS OPERATION CANNOT",
                                     "BE UNDONE.",
                                     "", background_color='#CC3333')
            if yes_no == 'Yes':
                disc_id = dg.eat_pickle('disc_id.pkl')
                print(f'deleting disc {disc_id}')
                dg.remove_disc_from_collection(disc_id)
                window.close()
                sg.PopupOK('DISC DELETED', background_color='#283B5B')
                break


if __name__ == '__main__':
    show()

