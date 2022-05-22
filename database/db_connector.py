import MySQLdb as mariadb
from database import db_credentials
from database.db_credentials import host, user, passwd, db
# from db_credentials import host,user, passwd, db

def connect_to_database(host = host, user = user, passwd = passwd, db=db):
    
    db_connection= mariadb.connect(host, user,passwd, db)
    
    return db_connection

def execute_query(db_connection = None, query = None, query_params = ()):
    
    if not db_connection :
        print("No connection to database found")
        return None
    
    if query is None or len(query.strip()) == 0:
        print("Query is empty!")
        return None
    
    cursor = db_connection.cursor()

    cursor.execute(query, query_params)
    db_connection.commit()
    return cursor

if __name__== '__main__':
    print("Executing sample query")
    db = connect_to_database()
    query= "SELECT * FROM employees"
    results= execute_query(db,query)
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)
    