import psycopg2
from config import config

# select_all(cursor)tällä voi kutsua connectia



def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        
        #insert("jorma", 2590, cursor)
        #updateperson(30, 2, cursor)
        #createtable(cursor)
        transaction("jorma", 200, cursor)
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
        
        
def insert(nimi, raha, cursor):
    SQL = "INSERT INTO pankki1 (name, rahat) VALUES (%s, %s);"
    data = (f"{nimi}", raha)
    cursor.execute(SQL, data)
    
def updateperson(age, id, cursor):
    SQL = "UPDATE person SET age = %s WHERE id = %s;"
    data = (age, id)
    cursor.execute(SQL, data)
    
def createtable(cursor):
    SQL = "CREATE TABLE pankki2 (PersonID SERIAL PRIMARY KEY, name varchar(255) NOT NULL, rahat INT);"
    cursor.execute(SQL)
    
def transaction(nimi, rahat, cursor):
    SQL = "BEGIN; UPDATE pankki2 SET rahat = rahat + %s WHERE name = %s; UPDATE pankki1 SET rahat = rahat - %s WHERE name = %s; COMMIT;"
    data = (rahat, f"{nimi}", rahat, f"{nimi}")
    cursor.execute(SQL, data)
if __name__ == '__main__':
    connect()