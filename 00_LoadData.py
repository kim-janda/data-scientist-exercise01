import sqlite3
import pandas as pd
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def main():
    #set db name
    database = "exercise01.sqlite"

    # create a database connection
    conn = create_connection(database)

    print("Query all records")
    #write query
    q = """SELECT R.*, W.name as workclass, E.name as educlevel, M.name as maritalstatus, O.name as occup,
           A.name as race, S.name as sex, C.name as country
        FROM records R 
           LEFT JOIN workclasses W on R.workclass_id = W.id    --add work classes
           LEFT JOIN education_levels E on R.education_level_id = E.id    --education level
           LEFT JOIN marital_statuses M on R.marital_status_id = M.id   --marital status
           LEFT JOIN occupations O on R.occupation_id = O.id   --occupation
           LEFT JOIN races A on R.race_id = A.id    --race
           LEFT JOIN sexes S on R.sex_id = S.id      -sex
           LEFT JOIN countries C on R.country_id = C.id   --country
           """
    df = pd.read_sql_query(q, conn)

    return df


if __name__ == '__main__':
    output_df = main()

    print("First 5 rows:")
    print(output_df.head())
    print("Colnames:")
    print(list(output_df.columns))
    print("Dimensions:")
    print(output_df.shape)

    print("Export DF")
    output_df.to_csv("fullrecords.csv", index = False)
