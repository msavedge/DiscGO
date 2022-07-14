import sqlite3
import pandas as pd
import DiscGO as dg
import PySimpleGUI as sg


def db_connect():
    return sqlite3.connect('./disc_db.db')


# rows = dg.get_disc_inventory()

# df = pd.DataFrame(rows)

sql = '''
     SELECT 
        inventory.mold,
        inventory.brand,
        inventory.speed,
        inventory.glide,
        inventory.turn,
        inventory.fade,
        inventory.plastic,
        inventory.weight,
        inventory.color,
        inventory.notes,
        disc.type,
        inventory.id
    FROM 
        INVENTORY
    JOIN
        disc
        on
        disc.mold like inventory.mold
    ORDER BY
        brand, inventory.mold
    '''

df = pd.read_sql_query(sql, db_connect())

print('df:')
print(df)

# make new column from existing columns
df['stability'] = df['turn'] + df['fade']
# print(df.stability)

# print(df.describe())

# print(df['type'].unique()) # returns list of types - Putter, Midrange, Fairway, Distance
print(df.type == 'Putter') # returns True or False if field matches 'Putter'

print(df[df.type == 'Putter']) # returns all columns for rows matching 'Putter'

# headers = ['mold', 'brand']
# data = df[df.type == 'Putter'].values.tolist()
#
# layout = [
#     [sg.Table(headings=headers,
#               values=data)]
# ]
#
# window = sg.Window("Putters", layout)
#
# event, values = window.read()
# if event == sg.WIN_CLOSED:
#     print(f'CLOSED WINDOW')
#     window.close()




# print(df.groupby(['type']).count())
#
# print(df.groupby(['brand']).count())
#
# print(df.groupby(['mold']).count())
#
# print(df.groupby(['speed']).count())
#
# print(df.groupby(['stability']).count())
#
# print(df.groupby(['weight']).count())
#
# weight_data = df.groupby(['weight']).count()
# print(f'weight_data:\n{weight_data["mold"]}')


# df = pd.read_sql_query(sql, db_connect())

# print('df:')
# print(df)

# print(df.head())
# print(df.columns)
# print(df.id)
# df.drop(['color', 'notes'], axis=1, inplace=True)
# print(df.columns)
# print(df.describe())
# print(df.describe(include=object))

# plot = df.weight.plot.hist(bins=5)
# fig = plot.get_figure()
# fig.savefig('demo-plot.png')

# df.to_csv('csv_disc_stats.csv', index=False)

# pivot = df.pivot_table(index='type', values='mold', aggfunc='count')
#
# print(f'pivot: {pivot}')


header_list = ['MOLD', 'BRAND', 'SPEED', 'GLIDE', 'TURN', 'FADE', 'PLASTIC', 'WEIGHT', 'COLOR', 'NOTES', 'TYPE', 'ID']
print(f'header_list: {header_list}')

data = df.values.tolist()
print(f'data: {data}')


layout = [[sg.Text('PANDAS test')],
          [sg.Table(headings=header_list,
                    values=data)]]

window = sg.Window("Panda test window", layout)

event, values = window.read()
if event == sg.WIN_CLOSED:
    print(f'CLOSED WINDOW')
    window.close()



