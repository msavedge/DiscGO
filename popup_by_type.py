import PySimpleGUI as sg
import DiscGO as dg


def get_disc_type_info(disc_type):
    sql = f'''
        SELECT
            count(*) as count,
            inventory.mold, 
            inventory.speed, 
            inventory.glide, 
            inventory.turn, 
            inventory.fade,
            (inventory.turn + inventory.fade) as stability
        FROM
            inventory
        JOIN
            disc
            on
            disc.mold like inventory.mold
        WHERE
            disc.type like '{disc_type}'
        group by
            inventory.mold
        order by
            count desc
        '''
    rows = dg.db_query_all(sql)
    return rows


def get_layout(type):
    _headings = ['COUNT', 'MOLD']
    #_headings = ['COUNT', 'MOLD', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'STABILITY']
    _values = get_disc_type_info(type)

    layout = [[sg.Table(headings=_headings,
                        values=_values,
                        justification='left',
                        alternating_row_color='#666666',
                        row_height=20,
                        num_rows=len(_values),
                        auto_size_columns=True,
                        pad=((20, 10), (10, 10)))]
    ]
    return layout


def show(layout, type):
    window = sg.Window(f'{type.upper()} LIST', layout)
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        print(f'CLOSED WINDOW')
        window.close()


if __name__ == '__main__':
    show(get_layout('putter'), 'putter')
