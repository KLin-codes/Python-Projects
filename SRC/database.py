import sqlite3
from get_data import get_data
connection = sqlite3.connect('HDB.db')      # create a connection (make a file to store the data)

df = get_data()

df.to_sql(
    'resale_transactions',
    connection,
    if_exists = 'replace',
    index = False
)                                       # Push the df to the table (named resale_transactions)

cursor = connection.cursor()            # connect to the database
