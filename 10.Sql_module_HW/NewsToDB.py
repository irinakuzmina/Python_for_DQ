# set and declare class to work with database
class NewsToDB:
    # class attributes
    dbName = ''

    # class constructor
    def __init__(self, db_name=''):
        self.dbName = db_name

    # private method to create connection with database
    def __connection(self, db_name=''):
        import pyodbc
        con = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                             'Direct=True;'
                             'Database=news.db;'
                             'String Types=Unicode')
        with con as self.connection:
            self.cursor = self.connection.cursor()

    # method to create tables
    def db_tables_create(self):
        self.__connection(self.dbName)
        try:
            # create NEWS table
            self.cursor.execute('CREATE TABLE NEWS ('
                                'id INT PRIMARY KEY, '
                                'text TEXT,'
                                'city TEXT,'
                                'news_date TEXT)')
            self.connection.commit()
        except:
            self.connection.rollback()
        try:
            # create Ad table
            self.cursor.execute('CREATE TABLE AD ('
                                'id INT PRIMARY KEY, '
                                'text TEXT,'
                                'exp_date TEXT,'
                                'days_left INT)')
            self.connection.commit()
        except:
            self.connection.rollback()
        try:
            # create event table
            self.cursor.execute('CREATE TABLE EVENT ('
                                'id INT PRIMARY KEY, '
                                'text TEXT,'
                                'city TEXT,'
                                'news_date TEXT)')
            self.connection.commit()
        except:
            self.connection.rollback()

    # set and declare method to set last record id
    def set_id(self, table_name):
        try:
            self.cursor.execute(f'SELECT MAX(ID) FROM {table_name}')
            id = int(self.cursor.fetchall()[0][0]) + 1
        except:
            id = 1
        return id

    # method to insert content in the NEWS table
    # ''.format() is using to shielding ' (for example in input file exist 'it's')
    def insert_news(self, text, city, news_date):
        self.__connection()
        id = self.set_id('NEWS')
        self.cursor.execute("SELECT COUNT(*) FROM NEWS WHERE text = ? AND city = ? ".format(), (text, city))
        if self.cursor.fetchall()[0][0] == 0:
            try:
                self.cursor.execute("INSERT INTO NEWS VALUES (?,?,?,?)".format(), (id, text, city, news_date))
                self.connection.commit()
            except:
                self.connection.rollback()
                self.cursor.close()
        else:
            print(
                '\n---------------------------------------DUPLICATE ROW'
                '--------------------------------------------------\n')
            print('-----Duplicate row. Was not recorded into database:----- \n', 'News: ' + text, ' \n',
                  'City: ' + city + '\n')
            self.connection.rollback()
            self.cursor.close()

    # method to insert text in the AD table
    # ''.format() is using to shielding ' (for example in input file exist 'it's')
    def insert_ad(self, text, exp_date, days_left):
        self.__connection()
        id = self.set_id('AD')
        self.cursor.execute("SELECT COUNT(*) FROM AD WHERE text = ? AND exp_date = ?".format(),
                            (text, exp_date))
        if self.cursor.fetchall()[0][0] == 0:
            try:
                self.cursor.execute("INSERT INTO AD VALUES (?,?,?,?)".format(), (id, text, exp_date, days_left))
                self.connection.commit()
            except:
                self.connection.rollback()
                self.cursor.close()
        else:
            print(
                '\n---------------------------------------DUPLICATE ROW'
                '--------------------------------------------------\n')
            print('-----Duplicate row. Was not recorded into database:-----\n', 'Ad: ' + text, ' \n',
                  'Expired date: ' + exp_date + '\n')
            self.connection.rollback()
            self.cursor.close()

    # method to insert content in the EVENT table
    # ''.format() is using to shielding ' (for example in input file exist 'it's')
    def insert_event(self, text, city, news_date):
        self.__connection()
        id = self.set_id('EVENT')
        self.cursor.execute("SELECT COUNT(*) FROM EVENT WHERE text = ? AND city = ? ".format(), (text, city))
        if self.cursor.fetchall()[0][0] == 0:
            try:
                self.cursor.execute("INSERT INTO EVENT VALUES (?,?,?,?)".format(),
                                    (id, text, city, news_date))
                self.connection.commit()
            except:
                self.connection.rollback()
                self.cursor.close()
        else:
            print(
                '\n---------------------------------------DUPLICATE ROW'
                '--------------------------------------------------\n')
            print('-----Duplicate row. Was not recorded into database:----- \n', 'Event: ' + text, ' \n',
                  'Publish date: ' + news_date + '\n')
            self.connection.rollback()
            self.cursor.close()
