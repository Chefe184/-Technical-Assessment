import psycopg2

def insert_data_to_db(table, data):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="companydata",
            user="admin",
            password="admin",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        insert_query = f"INSERT INTO {table} (columns) VALUES (%s, %s, ...)"
        cursor.executemany(insert_query, data)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
