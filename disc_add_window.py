import DiscGO as dg
import PySimpleGUI as sg


def get_layout(disc_list):
    values = disc_list

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
                        alternating_row_color='#283B5B',
                        header_text_color='#CC3333',
                        row_height=35)],
              [sg.Text('PLASTIC',
                       pad=((5, 50), (10, 10)),
                       background_color='#7a7a7a'),
               sg.Text('WEIGHT',
                       pad=((20, 50), (10, 10)),
                       background_color='#7a7a7a'),
               sg.Text('COLOR',
                       background_color='#7a7a7a')],
              [sg.Input('',
                        size=14,
                        pad=((5, 27), (0, 10)),
                        enable_events=True,
                        key='-plastic-'),
               sg.In('',
                     size=4,
                     pad=((5, 65), (0, 10)),
                     enable_events=True,
                     key='-weight-'),
              sg.ColorChooserButton('SELECT', target='-color-'),
               sg.In('', size=8, enable_events=True, key='-color-'),
               sg.DummyButton('', size=(15, 1), button_color=('#64778D', '#64778D'), disabled=True, key='-swatch-')],
              [sg.In('', visible=False, key='-secret-color-')],
              [sg.Text('NOTES',
                       background_color='#7a7a7a')],
              [sg.In('',
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
    # fdf should be single row if we got this far
    fdf = dg.eat_pickle('fdf.pkl')

    disc_list = fdf.values.tolist()

    layout = get_layout(disc_list)
    frame = [[sg.Frame('', layout)]]

    window = sg.Window('ADD DISC', frame, background_color='#63926C')

    while True:
        event, values = window.read()
        print(f'event: {event}\nvalues: {values}')

        if event == sg.WIN_CLOSED:
            window.close()
            break

        # form validation - require plastic, weight and color to activate 'add' button
        if len(values['-plastic-']) >= 2 and len(values['-weight-']) == 3 and len(values['-color-']) == 7:
            window['btn-add'].update(disabled=False)
        else:
            window['btn-add'].update(disabled=True)

        if event == '-color-':
            if values['-color-'] != 'None':  # value returned if user hits cancel button
                color = values['-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-secret-color-'].update(values['-color-'])
            else:
                color = values['-secret-color-']
                window['-swatch-'].update(button_color=(color, color))
                window['-color-'].update(values['-secret-color-'])

        if event == 'btn-add':

            disc = {'mold': fdf['mold'].tolist()[0],
                    'plastic': values['-plastic-'],
                    'weight': values['-weight-'],
                    'color': values['-color-'],
                    'notes': values['-notes-']}

            dg.add_disc_to_collection(disc)
#           # popup confirming successful add
            window.close()
            sg.PopupOK('DISC ADDED', background_color='#63926C')
            break


if __name__ == '__main__':
    show()

