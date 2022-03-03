import psycopg2
import config

# select_all(cursor)tällä voi kutsua connectia

def connect():
    con = None
    try:
        con = psycopg2.connect(**config.config())
        cursor = con.cursor()
        select_certs(cursor)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            
            
def select_all(cursor):
    SQL = 'SELECT * FROM certificates'
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
        
def select_columns(cursor):
    SQL = "SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'certificate'"
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
        
def select_certs(cursor):
    SQL = "SELECT person.name, person.id, certificates.name FROM certificates, person WHERE certificates.person_id = person.id ;"
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
        
if __name__ == '__main__':
    connect()