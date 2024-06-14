from src.db_connection import DBConnection


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


