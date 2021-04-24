from database_connection import get_database_connection

class StockRepository:
    def __init__(self, connection):
        self._connection = connection
        self._result = {}
        self._userlist = {}

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from stocks')
        rows = cursor.fetchall()
        self._result = {}
        for row in rows:
            self._result[row[1]] = []
            self._result[row[1]].append(str(row[2]))
            self._result[row[1]].append(str(row[3]))
            self._result[row[1]].append(str(row[4]))
        return self._result

    def get_stocks_by_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from stocks where user = ?',
            (user,)
        )
        rows = cursor.fetchall()
        self._userlist = {}
        for row in rows:
            self._userlist[row[1]] = []
            self._userlist[row[1]].append(str(row[2]))
            self._userlist[row[1]].append(str(row[3]))
            self._userlist[row[1]].append(str(row[4]))
        return self._userlist


    def create(self, user, ticker, name, price, date):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into stocks (user, ticker, name, price, date) values (?, ?, ?, ?, ?)',
            (user, ticker, name, price, date)
        )
        self._connection.commit()
        return

    def update(self, user, ticker, price, date):
        cursor = self._connection.cursor()
        cursor.execute(
            'update stocks set price = ?, date = ? where user = ? and ticker = ?',
            (price, date, user, ticker)
        )
        self._connection.commit()
        return

    def remove(self, user, ticker):
        cursor = self._connection.cursor()
        cursor.execute(
            'delete from stocks where user = ? and ticker = ?',
            (user, ticker)
        )
        self._connection.commit()
        return

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from stocks')
        self._connection.commit()

stock_repository = StockRepository(get_database_connection())
