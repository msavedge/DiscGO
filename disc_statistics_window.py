import DiscGO as dg
import PySimpleGUI as sg


# get number of _type (putter, midrange, fairway, distance) disc in inventory
import popup_by_type


def get_count_by_disc_type(_type):
    sql = f'''
        SELECT
            count(*),
            disc.type
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
            count(*),
            disc.type
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
            count(*),
            brand
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
            count(*),
            speed
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
            count(*),
            mold
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
           count(turn),
           turn + fade as stability
        from 
            inventory
        group by 
            stability
        order by 
            stability desc
    '''
    rows = dg.db_query_all(sql)
    return rows


def get_count_disc_by_weight():
    sql = '''
        select
           count(turn),
           weight
        from 
            inventory
        group by 
            weight
        order by 
            weight desc
    '''
    rows = dg.db_query_all(sql)
    return rows


# logic code above
# GUI code below
def get_table_count_discs_by_type():
    _headings = ['COUNT', 'TYPE']
    table = [sg.Table(headings=_headings,
                      values=get_count_disc_by_type(),
                      justification='right',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=4,
                      enable_click_events=False,
                      enable_events=True,
                      key='-tbl_disc_by_type-',
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_brand():
    _headings = ['COUNT', 'BRAND']
    _values = get_count_disc_by_brand()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='right',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=len(_values),
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_speed():
    _headings = ['COUNT', 'SPEED']
    _values = get_count_disc_by_speed()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='right',
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
    _headings = ['COUNT', 'MOLD']
    _values = get_count_disc_by_mold()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='right',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=10,
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_stability():
    _headings = ['COUNT', 'STABILITY']
    _values = get_count_disc_by_stability()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='right',
                      alternating_row_color='#666666',
                      row_height=25,
                      num_rows=10,
                      pad=((20, 10), (10, 10)))]
    return table


def get_table_count_discs_by_weight():
    _headings = ['COUNT', 'WEIGHT']
    _values = get_count_disc_by_weight()
    table = [sg.Table(headings=_headings,
                      values=_values,
                      justification='right',
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


def get_frame_disc_by_weight():
    frame = [sg.Frame("WEIGHT in grams", [get_table_count_discs_by_weight()])]
    return frame


def get_col1():
    return sg.Column([get_frame_disc_by_type(), get_frame_disc_by_brand()])


def get_col2():
    return sg.Column([get_frame_disc_by_mold()])


def get_col3():
    return sg.Column([get_frame_disc_by_speed()])


def get_col4():
    return sg.Column([get_frame_disc_by_stability()])


def get_col5():
    return sg.Column([get_frame_disc_by_weight()])


def get_layout():
    layout = [
        [get_col1(), get_col2(), get_col3(), get_col4(), get_col5()]
    ]
    return layout


def show(layout):
    window = sg.Window('DISC COLLECTION STATISTICS', layout)
    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(f'event: {event}')
        print('')
        print(f'values: {values}')

        if event == sg.WIN_CLOSED:
            print(f'CLOSED WINDOW')
            window.close()
            break

        # elif event == '-tbl_disc_by_type-':
            # row = values["-tbl_disc_by_type-"][0]
            # # print(f'row clicked: {row}')
            # disc_type = window["-tbl_disc_by_type-"].get()[row][0]
            # # print(f'disc type: {disc_type}')
            # popup_by_type.show(popup_by_type.get_layout(disc_type), disc_type)



if __name__ == '__main__':
    show(get_layout())
