from src.db_manager import DBManager
from src.db_connection import DBConnection


def main():
    # Создание экземпляра DBManager с параметрами подключения к базе данных
    db_conn = DBConnection(
        name='cw5',
        host='localhost',
        port=5432,
        user='postgres',
        password='ravil1211'
    ).conn
    db_manager = DBManager(db_conn)

    # Получение списка всех компаний и количества вакансий у каждой компании
    companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
    print("ID Компании и количество вакансий:")
    for row in companies_and_vacancies_count:
        print(f'{row[0]} - {row[1]}')

    # Получение списка всех вакансий с указанием названия компании, названия вакансии и зарплаты
    all_vacancies = db_manager.get_all_vacancies()
    print("\nВсе вакансии:")
    for vacancy in all_vacancies:
        print(vacancy)

    # Получение средней зарплаты по вакансиям
    avg_salary = db_manager.get_avg_salary()
    print(f"\nСредняя зарплата по вакансиям: {avg_salary}")

    # Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям
    high_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
    print("\nВакансии с зарплатой выше средней:")
    for vacancy in high_salary_vacancies:
        print(vacancy)

    # Получение списка всех вакансий, в названии которых содержатся переданные в метод слова, например python
    keyword = 'Специалист'
    vacancies_with_keyword = db_manager.get_vacancies_with_keyword()
    print(f"\nВакансии с ключевым словом '{keyword}':")
    for vacancy in vacancies_with_keyword:
        print(vacancy)


if __name__ == "__main__":
    main()
