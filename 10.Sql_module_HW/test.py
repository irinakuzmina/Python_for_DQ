import pyodbc
import NewsToDB

connection = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'Direct=True;'
                            'Database=news.db;'
                            'String Types= Unicode', autocommit=True)

cursor = connection.cursor()

cursor.execute('select * from NEWS')
result = cursor.fetchall()
print(result)
print(type(result))
print(result[1])

# db = NewsToDB.NewsToDB('news.db')
# db.print_db_tables()
