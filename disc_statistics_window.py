import DiscGO as dg
import PySimpleGUI as sg


# get number of _type (putter, midrange, fairway, distance) disc in inventory
def get_count_by_disc_type(_type):
    sql = f'''
        SELECT
            disc.type,
            count(*)
        FROM
            inventory
        JOIN
            disc
            ON
            inventory.mold like disc.mold
        WHERE
            disc.type like '{_type}'
        '''
    row = dg.db_query_one(sql)
    print(f"COUNT of type {_type} = {row[1]}")
    return row[1]


def get_count_disc_by_type():
    sql = '''
        SELECT
            disc.type,
            count(*)
        FROM
            inventory
        join
            disc on inventory.mold like disc.mold
        group by
            disc.type
        order by count(*) desc
        '''
    rows = dg.db_query_all(sql)
    return rows


def get_count_disc_by_brand():
    sql = '''
        SELECT
            brand,
            count(*)
        FROM
            inventory
        group by
            brand
        order by count(*) desc
        '''
    rows = dg.db_query_all(sql)
    return rows


def get_count_disc_by_speed():
    sql = '''
        SELECT
            speed,
            count(*)
        FROM
            inventory
        group by
            speed
        order by 
            speed
    '''
    rows = dg.db_query_all(sql)
    return rows


def get_count_disc_by_mold():
    sql = '''
        SELECT
            mold,
            count(*)
        FROM
            inventory
        group by
            mold
        order by
            count(*) desc
    '''
    rows = dg.db_query_all(sql)
    return rows


def get_count_disc_by_stability():
    sql = '''
        select
            turn + fade as stability,
            count(turn)
        from inventory
        group by stability
        order by stability desc
    '''
    rows = dg.db_query_all(sql)
    return rows


# logic code above
# GUI code below
def get_table_count_discs_by_type():
    _headings = ['TYPE', 'COUNT']
    table = [sg.Table(headings=_headings,
                      values=get_count_disc_by_type(),
                      justification='left',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=4,
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_brand():
    _headings = ['BRAND', 'COUNT']
    _values = get_count_disc_by_brand()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='left',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=len(_values),
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_speed():
    _headings = ['SPEED', 'COUNT']
    _values = get_count_disc_by_speed()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='left',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=len(_values),
                      pad=((20, 10), (10, 10)))]
    return table


def get_layout_discs_by_type():
    num_putters = get_count_by_disc_type('putter')
    num_midrange = get_count_by_disc_type('midrange')
    num_fairway = get_count_by_disc_type('fairway')
    num_distance = get_count_by_disc_type('distance')
    _layout = [
        [sg.Text('DISCS BY TYPE')],
        [sg.Text('putter: '), sg.Text(num_putters)],
        [sg.Text('midrange: '), sg.Text(num_midrange)],
        [sg.Text('fairway: '), sg.Text(num_fairway)],
        [sg.Text('distance: '), sg.Text(num_distance)],
    ]
    return _layout


def get_table_count_discs_by_mold():
    _headings = ['MOLD', 'COUNT']
    _values = get_count_disc_by_mold()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='left',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=10,
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_stability():
    _headings = ['STABILITY', 'COUNT']
    _values = get_count_disc_by_stability()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='left',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=10,
                      pad=((20, 10), (10, 10)))]
    return table


def get_frame_disc_by_type():
    frame = [sg.Frame("TYPE", [get_table_count_discs_by_type()])]
    return frame


def get_frame_disc_by_brand():
    frame = [sg.Frame("BRAND", [get_table_count_discs_by_brand()])]
    return frame


def get_frame_disc_by_speed():
    frame = [sg.Frame("SPEED", [get_table_count_discs_by_speed()])]
    return frame


def get_frame_disc_by_mold():
    frame = [sg.Frame("MOLD", [get_table_count_discs_by_mold()])]
    return frame


def get_frame_disc_by_stability():
    frame = [sg.Frame("STABILITY = turn + fade", [get_table_count_discs_by_stability()])]
    return frame


def get_col1():
    return sg.Column([get_frame_disc_by_type(), get_frame_disc_by_brand()])


def get_col2():
    return sg.Column([get_frame_disc_by_mold()])


def get_col3():
    return sg.Column([get_frame_disc_by_speed()])


def get_col4():
    return sg.Column([get_frame_disc_by_stability()])


def get_layout():
    layout = [
        [get_col1(), get_col2(), get_col3(), get_col4()]
    ]
    return layout


def show(layout):
    window = sg.Window('DISC COLLECTION STATISTICS', layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            layout = None
            break


if __name__ == '__main__':
    show(get_layout())
