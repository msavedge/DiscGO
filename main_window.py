import DiscGO as dg
import PySimpleGUI as sg
import DiscGOgui as dgg

import disc_add_edit_window
import mold_selection_window as msw


def get_layout(disc_list):
    _values = disc_list

    _headings = [f'{"TYPE" : ^8}',
                 f'{"BRAND" : ^15}',
                 f'{"MOLD" : ^20}',
                 f'{"SPEED" : ^5}',
                 f'{"GLIDE" : ^5}',
                 f'{"TURN" : ^5}',
                 f'{"FADE" : ^5}',
                 f'{"STABILITY" : ^4}',
                 f'{"PLASTIC" : ^6}',
                 f'{"COLOR" : ^6}',
                 f'{"WEIGHT" : ^4}',
                 f'{"NOTES" : ^25}']

    _layout = [[sg.Button('DISC COLLECTION DATA'),
                sg.Button('ADD DISC', pad=((450, 10), (10, 10)))],
               [sg.Table(headings=_headings,
                         values=_values,
                         num_rows=12,
                         key='-tbl_inv-',
                         enable_events=True,
                         enable_click_events=False,
                         justification='left',
                         alternating_row_color='#7a7a7a',
                         row_height=35)],
               [sg.Button('GO TO BAG',
                          key='btn-bag',
                          disabled=True,
                          disabled_button_color=('white', '#64778D')),
                sg.Button('THROW INFO',
                          key='btn-throw',
                          disabled=True,
                          disabled_button_color=('white', '#64778D'),
                          pad=((200, 200), (10, 10)))]]
    return _layout


def show():
    df = dg.eat_pickle('mold_list.pkl')
    disc_list = df.values.tolist()

    layout = get_layout(disc_list)
    window = sg.Window('DiscGO - Disc Golf Data And Number Crunching Experiment', layout)

    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == 'CLOSE WINDOW':
            window.close()
            break

        if event == '-tbl_inv-':
            # print(f'tbl_list: {values["-tbl_list-"][0]}')
            if values['-tbl_inv-']:
                row = values['-tbl_inv-'][0]
                # print(f'row: {row}')

                disc = disc_list[row]
                print(f'DISC DEETS: {disc}')

                mold = disc[2]
                ### HERE IS WHERE WE NEED TO WORK:
                #       make new add_edit form (or two forms like DSW & MCM)
                #       make it work with mold (or mold.mold) vs. disc_id
                #       look up info from SQL DB, based on mold.mold & populate form
                disc_add_edit_window.show(disc_add_edit_window.get_edit_disc_layout(disc_id))
                # refresh table rows after saving disc / closing edit window
                print(f'DISC LIST: {dg.get_disc_inventory()}')
                window['-tbl_inv-'].update(values=dg.get_disc_inventory())

        elif event == 'ADD DISC':
            dgg.run_window('mold_selection_window')

        elif event == 'DISC COLLECTION DATA':
            dgg.run_window('disc_statistics_window')


if __name__ == '__main__':
    dg.create_db()
    disc_list = dg.get_disc_inventory()
    show()
