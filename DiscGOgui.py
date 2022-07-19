import PySimpleGUI as sg

# layouts for PySimpleGUI windows
import inventory_window as iw
import disc_list_window as dlw
import disc_statistics_window as dsw
import main_window as mw
import mold_selection_window as msw
import mold_comparison_matrix as mcm
import disc_add_window as daw


def run_window(window):
    if window == 'main_window':
        mw.show()

    if window == 'mold_selection_window':
        msw.show()

    if window == 'disc_statistics_window':
        dsw.show()

    if window == 'mold_comparison_matrix':
        mcm.show()

    if window == 'disc_add_window':
        daw.show()


def show_inventory_window():
    iw.show(iw.get_layout())


def show_mold_database():
    dlw.show()


def show_collection_data():
    dsw.show(dsw.get_layout())
