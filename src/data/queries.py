import psycopg2
from config import config

# select_all(cursor)tällä voi kutsua connectia



def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        
        updateperson(30, 2, cursor)
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            
            
def select(SQL, cursor):
    SQL 
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
        
        
def insert(serti, id, cursor):
    SQL = "INSERT INTO certificates (name, person_id) VALUES (%s, %s);"
    data = (f"{serti}", id)
    cursor.execute(SQL, data)
    
def updateperson(age, id, cursor):
    SQL = "UPDATE person SET age = %s WHERE id = %s;"
    data = (age, id)
    cursor.execute(SQL, data)
    

        
if __name__ == '__main__':
    connect()