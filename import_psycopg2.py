import psycopg2

conn = psycopg2.connect(database = 'friday',\
                        user = 'postgres', \
                        password = '1234', 
                        host = '127.0.0.1',
                        port='5432')
cursor = conn.cursor()
sql = 'select version()'
cursor.execute(sql)
data = cursor.fetchone()
print('database version : %s ' % data)
conn.commit()
conn.close()


