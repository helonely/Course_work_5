from src.db_connection import DBConnection
from src.vacancy import HHParser


def create_tables(db_conn):  # Принимает подключение
    """С помощью sql запроса создаем таблицы с колонками для компании и вакансий"""
    with db_conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                url VARCHAR(255) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vacancies (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                url VARCHAR(255) NOT NULL,
                company_id INT NOT NULL REFERENCES companies(id),
                salary_min INT,
                salary_max INT
            );
        """)

        db_conn.commit()


def insert_vacancies(db_conn, vacancies_data):
    """Заполняет данные по вакансиям"""
    with db_conn.cursor() as cursor:
        for vacancy in vacancies_data:
            cursor.execute(
                """
                INSERT INTO vacancies(id, name, url, company_id, salary_min, salary_max)
                VALUES(%s,%s,%s,%s,%s,%s);
                """, (
                    vacancy['id'],  # id вакансии
                    vacancy['name'],  # название
                    vacancy['url'],  # ссылка
                    vacancy['employer']['id'],  # id компании
                    vacancy['salary']['from'],  # зп минимальная
                    vacancy['salary']['to'],  # зп максимальная
                )
            )
            db_conn.commit()


def insert_employers(db_conn, employers_data):
    """Заполняет данные по компаниям"""
    with db_conn.cursor() as cursor:
        for employer in employers_data:
            cursor.execute(
                """
                INSERT INTO companies(id, name, url)
                VALUES(%s,%s,%s);
                """, (
                    employer['id'],  # id компании
                    employer['name'],  # название
                    employer['url'],  # ссылка
                )
            )
            db_conn.commit()


def truncate_table(db_conn):
    """Удаляет все строки из таблицы для перезаписи"""
    with db_conn.cursor() as cursor:
        cursor.execute(
            """
            TRUNCATE TABLE companies RESTART IDENTITY CASCADE;
            """
        )
        cursor.execute(
            """
            TRUNCATE TABLE vacancies RESTART IDENTITY;
            """
        )
        db_conn.commit()
