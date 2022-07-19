import sqlite3

import pandas as pd

import DiscGOdata as dgd
import pickle


# # add these methods for retrieving data from SQL database:
# # INITIALIZE:
#   delete old data frames:
#       python.os ?
#   create data frames:  # MOLD_LIST, COLLECTION
#       pandas read_sql()
#       dg.make_pickle(df)
#   load_data_frame(df_name)
#       dg.eat_pickle()
#       return df
# def get_mold_list_df()
#   pandas read_sql()
# def get_collection_df()
#   pandas read_sql()
# # def get_throw_df()
# def add_to_collection(mold, options{})
#   SQL, then reload df
# def delete_from_collection(disc_id)
#   SQL, then reload df
# def pivot_df_on(df, index, values)


def db_connect():
    return sqlite3.connect('./disc_db.db')


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


def make_dataframe_pickles():
    # get mold list
    sql = 'SELECT * FROM MOLD'
    df = pd.read_sql(sql, db_connect())
    make_pickle(df, 'mold_list.pkl')

    # get collection list
    sql = '''
        SELECT
            type,
            brand,
            collection.mold,
            speed,
            glide,
            turn,
            fade,
            stability,
            weight,
            plastic,
            color,
            notes,
            id
        FROM
            collection
        JOIN
            mold
            on
            mold.mold like collection.mold
        '''
    df = pd.read_sql(sql, db_connect())
    make_pickle(df, 'collection.pkl')


def make_pickle(obj, file):
    # pickle object
    f = open(file, 'wb')
    pickle.dump(obj, f)
    f.close()


def eat_pickle(file):
    f = open(file, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj


def get_filtered_dataframe(df, conditions):
    # k is filter, v is condition
    for key, val in conditions.items():
        if val not in ('', 'All'):
            print(key, val)
            df = df[df[f'{key}'] == val]
    print("FILTERED DATA BELOW")
    return df


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


def add_disc_to_collection(disc):
    # disc = {'mold': fdf.mold,
    #         'plastic': values['-plastic-'],
    #         'weight': values['-weight-'],
    #         'color': values['-color-'],
    #         'notes': values['-notes-']}
    sql = f'''
        INSERT INTO collection
            (mold,
            plastic,
            weight,
            color,
            notes)
        VALUES
            ("{disc['mold']}",
            "{disc['plastic']}",
            "{disc['weight']}",
            "{disc['color']}",
            "{disc['notes']}")
        '''
    # print(f'SQL:\n{sql}')
    db_execute(sql)
    # refresh data used by app
    make_dataframe_pickles()


def update_disc_in_collection(disc):
    sql = f'''
        UPDATE
            collection
        SET
            plastic = '{disc['plastic']}',
            weight = '{disc['weight']}',
            color = '{disc['color']}',
            notes = '{disc['notes']}'
        WHERE
            id = {disc['id']}
        '''
    db_execute(sql)
    make_dataframe_pickles()


def get_disc_from_collection(disc_id):
    sql = f'''
        SELECT
            type,
            brand,
            collection.mold,
            speed,
            glide,
            turn,
            fade,
            plastic,
            weight,
            color,
            notes
        FROM
            collection
        JOIN
            mold
            on
            mold.mold like collection.mold
        WHERE
            id = {disc_id}
        '''
    # print(f'SQL:\n{sql}')
    return db_query_one(sql)


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
