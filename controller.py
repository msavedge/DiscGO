import DiscGOgui as dgg
import PySimpleGUI as sg


def get_main_layout():
    layout = [
        [sg.Text(f'Data And Number Crunching Experiment'.upper())],
        [sg.Text('')],
        [sg.Button('DISC INVENTORY'), sg.Text('', size=2), sg.Button('MOLD DATABASE')],
        [sg.Text('')],
        [sg.Button('BAG STATS', visible=False), sg.Text('', size=30), sg.Button('EXIT')],
        [sg.Text('')]
    ]
    return layout


if __name__ == '__main__':
    # app flow:
    #   show main window (one-shot)
    main_layout = get_main_layout()
    main_window = sg.Window('MAIN APPLICATION WINDOW', get_main_layout())

    while True:
        main_event, main_values = main_window.read()
        print(f'MAIN EVENT: {main_event}')
        print(f'MAIN VALUES: {main_values}')

        if main_event == sg.WIN_CLOSED or main_event == 'EXIT':
            print("WINDOW CLOSED")
            main_window.close()
            break

        elif main_event == 'DISC INVENTORY':
            print('showing disc inventory')

            dgg.show_inventory_window()

        elif main_event == 'MOLD DATABASE':
            print('showing mold database')

            dgg.show_mold_database()

