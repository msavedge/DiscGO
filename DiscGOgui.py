# layouts for PySimpleGUI windows
import disc_collection_window as dsw
import main_window as mw
import mold_selection_window as msw
import mold_comparison_matrix as mcm
import disc_add_window as daw
import disc_edit_window as dew


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

    if window == 'disc_edit_window':
        dew.show()


def show_collection_data():
    dsw.show(dsw.get_layout())
