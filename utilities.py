import psycopg2

def get_password_securely():
    print("Retrieve database user password securely here")

hostname = "host"
database = "database"
username = "username"
#password = get_password_securely()

def get_db():
    if 'db' not in g:
        connection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        g.db = connection
    return g.db

def do_query(conn, query) :
    cur = conn.cursor()

    cur.execute(query)
    conn.commit()

    #Store result as a list of tuples
    try:
        result = cur.fetchall()
        return result
    except:
        pass

    cur.close()
    #Return a list with each row as a tuple
    return None