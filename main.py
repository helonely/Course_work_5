from src.vacancy import HHParser

hh = HHParser()  # Класс получает данные по работодателям и вакансиям
print(hh.get_vacancies_data())  # данные по вакансиям
print(hh.get_employers_data())  # данные по работодателям
