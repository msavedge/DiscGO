import DiscGO as dg
import PySimpleGUI as sg

layout = [
    [sg.Text('Your Message Here')],
]


def show(_layout):
    window = sg.Window('WINDOW TITLE', _layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            break


if __name__ == '__main__':
    show(layout)
