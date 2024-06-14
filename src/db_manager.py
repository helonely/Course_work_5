from src.db_connection import DBConnection


class DBManager:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        """Вычисляем среднюю зп по вакансиям"""
        with self.db_conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT AVG(salary_min)
                FROM vacancies;
                """
            )
            return cursor.fetchall()

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass


if __name__ == '__main__':
    db_conn = DBConnection(
        name='cw5',
        host='localhost',
        port=5432,
        user='postgres',
        password='ravil1211'
    ).conn
    db_manager = DBManager(db_conn)
    print(db_manager.get_avg_salary())

