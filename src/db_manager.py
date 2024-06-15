from src.db_connection import DBConnection


class DBManager:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        with self.db_conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT company_id, COUNT(vacancies) as vacancies_count
                FROM vacancies group by company_id;
                """
            )
            return cursor.fetchall()

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
         """
        with self.db_conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT c.name AS company_name, v.name AS vacancy_name, v.salary_min, v.salary_max, v.url
                FROM vacancies v
                JOIN companies c ON v.company_id = c.id;
                """
            )
            return cursor.fetchall()

    def get_avg_salary(self):
        """Вычисляем среднюю зп по вакансиям"""
        with self.db_conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT AVG(salary_min + salary_max) / 2 AS avg_salary FROM vacancies;
                """
            )
            return cursor.fetchall()

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям
        """
        with self.db_conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM vacancies
                WHERE (salary_min + salary_max) / 2 > (SELECT AVG((salary_min + salary_max) / 2)
                FROM vacancies);
                """
            )
            return cursor.fetchall()

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова,
        например Специалист
        """
        with self.db_conn.cursor() as cursor:
            keyword = 'Специалист'
            cursor.execute(
                """
                SELECT c.name AS company_name, v.name AS vacancy_name, v.salary_min, v.salary_max, v.url
                FROM vacancies v
                JOIN companies c ON v.company_id = c.id
                WHERE v.name ILIKE %s;
                """, ('%' + keyword + '%',))
            return cursor.fetchall()
