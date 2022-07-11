import sqlite3
import DiscGOdata as dgd


def db_connect():
    return sqlite3.connect('disc_db.db')


def db_execute(sql):
    print(f'SQL:\n{sql}')
    conn = db_connect()
    conn.execute(sql)
    conn.commit()
    conn.close()
    return


def create_db():
    conn = db_connect()
    cursor = conn.executescript(dgd.sql)
    conn.commit()
    conn.close()
    return


def db_query_one(sql):
    print(f'query_one SQL:\n{sql}')
    conn = db_connect()
    cursor = conn.execute(sql)
    row = cursor.fetchone()
    conn.close()
    return row


def db_query_all(sql):
    print(f'SQL:\n{sql}')
    conn = db_connect()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_mold_info(mold):
    sql = f'''
        select 
            brand.name, 
            disc.mold,  
            disc.speed,  
            disc.glide, 
            disc.turn, 
            disc.fade,
            disc.brand_id
        from 
            disc
        inner join brand 
            on brand.id = disc.brand_id 
        where
            disc.mold like '{mold}'
    '''
    return db_query_one(sql)


def get_plastics_for_brand_id(brand_id):
    sql = f'''
        select 
            distinct plastic.name 
        from 
            plastic 
        inner join 
            disc 
            on 
            disc.brand_id = plastic.brand_id
        where 
            disc.brand_id = {brand_id}
    '''
    return db_query_all(sql)


def get_plastics_for_brand(brand):
    sql = f'''
        select 
            distinct plastic.name 
        from 
            plastic 
        inner join 
            disc 
            on 
            disc.brand_id = plastic.brand_id
        where 
            disc.brand_id = ( select id from brand where name like '{brand}' )
    '''
    return db_query_all(sql)


def get_plastics_for_mold(mold):
    sql = f'''
        select
            name 
        from 
            plastic 
        where 
            brand_id = (SELECT brand_id from disc where mold like '{mold}')
        '''
    return db_query_all(sql)


def add_disc_to_inventory(disc):
    print(f'adding disc to inventory...')
#    print(f'''
#        mold: {disc['-mold-']}
#        brand: {disc['-manufacturer-']}
#        speed: {disc['-speed-']}
#        glide: {disc['-glide-']}
#        turn: {disc['-turn-']}
#        fade: {disc['-fade-']}
#        plastic: {disc['-plastic-']}
#        weight: {disc['-weight-']}
#        color: {disc['-color-']}
#        notes: {disc['-notes-']}
#        ''')
    sql = f'''
        INSERT INTO inventory
            (mold,
             brand,
             speed,
             glide,
             turn,
             fade,
             plastic,
             weight,
             color,
             notes)
        VALUES
            ("{disc['-mold-']}",
             "{disc['-manufacturer-']}",
             "{disc['-speed-']}",
             "{disc['-glide-']}",
             "{disc['-turn-']}",
             "{disc['-fade-']}",
             "{disc['-plastic-']}",
             "{disc['-weight-']}",
             "{disc['-color-']}",
             "{disc['-notes-']}")
        '''
    # print(f'SQL:\n{sql}')
    db_execute(sql)


def add_mold_to_inventory(disc):
    # print(f'MADE UP DISC: {disc}')
    sql = f'''
        INSERT INTO inventory
            (mold,
             brand,
             speed,
             glide,
             turn,
             fade,
             plastic,
             weight,
             color,
             notes)
        VALUES
            ("{disc['mold']}",
             "{disc['manufacturer']}",
             "{disc['speed']}",
             "{disc['glide']}",
             "{disc['turn']}",
             "{disc['fade']}",
             "{disc['plastic']}",
             "{disc['weight']}",
             "{disc['color']}",
             "{disc['notes']}")
            '''
    # print(f'SQL:\n{sql}')
    db_execute(sql)


def get_disc_inventory():
    sql = '''
        SELECT 
            mold,
            brand,
            speed,
            glide,
            turn,
            fade,
            plastic,
            weight,
            color,
            notes,
            id
        FROM 
            INVENTORY
        ORDER BY
            brand, mold
        '''
    return db_query_all(sql)


def get_all_discs():
    sql = '''
        select 
            UPPER(disc.mold),  
            brand.name, 
            disc.speed,  
            disc.glide, 
            disc.turn, 
            disc.fade
        from 
            disc
        inner join brand 
            on brand.id = disc.brand_id 
        order by
            brand.name
    '''
    return db_query_all(sql)


def get_disc_from_inventory(disc_id):
    sql = f'''
        SELECT 
            mold,
            brand,
            speed,
            glide,
            turn,
            fade,
            plastic,
            weight,
            color,
            notes,
            id
        FROM 
            INVENTORY
        WHERE
            id = {disc_id}
        '''
    return db_query_one(sql)


def update_disc_in_inventory(disc_id, plastic, weight, color, notes):
    sql = f'''
        UPDATE
            inventory
        SET
            plastic = '{plastic}',
            weight = '{weight}',
            color = '{color}',
            notes = '{notes}'
        WHERE
            id = {disc_id}
    '''
    # print("sql: " + sql)
    return db_execute(sql)


def remove_disc_from_inventory(disc_id):
    sql = f'''
        DELETE FROM
            inventory
        WHERE
            id = {disc_id}
        '''
    # print(f'sql: {sql}')
    return db_execute(sql)
