import PySimpleGUI as sg

# layouts for PySimpleGUI windows
import inventory_window as iw
import disc_list_window as dlw


def show_inventory_window():
    iw.show(iw.get_layout())


def show_mold_database():
    dlw.show(dlw.get_layout())


# def show_disc_not_found():
#     sg.popup('DISC NOT FOUND')


# def get_inventory_layout():
#     return iw.get_layout()


# def get_mold_list_layout():
#     return dlw.get_layout()
