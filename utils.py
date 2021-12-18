import pandas as pd
import sqlite3 as sql
def make_database(path_file, name):
    '''
    Function to update the db via csv
    :Parameters: path_file(str) -> path
                 name -> name of the table
    :Return: None

    '''

    df = pd.read_csv(path_file)
    conn = sql.connect('strafovi.db')
    df.to_sql(name, conn, if_exists='replace')


    return 'DONE'