import psycopg2


class DBConnection:
    """Модуль подключения к БД"""
    def __init__(self, name, host, port, user, password):
        self.conn = psycopg2.connect(
            database=name,
            host=host,
            port=port,
            user=user,
            password=password
        )

    def conn_close(self):
        """Закрыть подключение к БД"""
        self.conn.close()


if __name__ == '__main__':
    db_conn = DBConnection(
        name='cw5',
        host='localhost',
        port=5432,
        user='postgres',
        password='ravil1211'
    ).conn
