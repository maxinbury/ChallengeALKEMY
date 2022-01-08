import pandas as pd
from main import session

cursor = session.bind.raw_connection().cursor()
def query(sql,inf):
    cursor.execute(sql)
    for row in cursor:
        print(row)
    
sql = "SELECT * FROM info_cines;"
inf = "información procesada de cines"
query((sql),(inf))

