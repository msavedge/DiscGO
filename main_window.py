import DiscGO as dg
import PySimpleGUI as sg
import DiscGOgui as dgg

# sg.theme_previewer()
sg.theme("Brown Blue")

def get_layout(disc_list):
    values = disc_list

    headings = [f'{"TYPE" : ^8}',
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

    layout = [[sg.Button('DISC COLLECTION DATA'),
               sg.Button('ADD DISC', pad=((850, 10), (10, 10)))],
              [sg.Table(headings=headings,
                        values=values,
                        num_rows=12,
                        key='-tbl_inv-',
                        enable_events=True,
                        enable_click_events=False,
                        justification='left',
                        alternating_row_color='#7a7a7a',
                        header_text_color='#CC3333',
                        row_height=35)],
              [sg.Button('GO TO BAG',
                         key='btn-bag',
                         disabled=True),
              sg.Button('THROW INFO',
                        key='btn-throw',
                        disabled=True,
                        pad=((200, 200), (10, 10)))]]
    return layout


def show():
    df = dg.eat_pickle('collection.pkl')
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

                disc_id = disc[12]
                dg.make_pickle(disc_id, 'disc_id.pkl')

                ### HERE IS WHERE WE NEED TO WORK:
                #       make new add_edit form (or two forms like DSW & MCM)
                #       make it work with mold (or mold.mold) vs. disc_id
                #       look up info from SQL DB, based on mold.mold & populate form
                # # disc_id saved in pickle file, rather than being passed around
                dgg.run_window('disc_edit_window')

                # refresh table rows after saving disc / closing edit window
                df = dg.eat_pickle('collection.pkl')
                disc_list = df.values.tolist()

                window['-tbl_inv-'].update(values=disc_list)

        elif event == 'ADD DISC':
            dgg.run_window('mold_selection_window')

        elif event == 'DISC COLLECTION DATA':
            dgg.run_window('disc_statistics_window')

        # update window
        df = dg.eat_pickle('collection.pkl')
        disc_list = df.values.tolist()

        window['-tbl_inv-'].update(values=disc_list)


if __name__ == '__main__':
    dg.create_db()
    # disc_list = dg.get_disc_inventory()
    show()
