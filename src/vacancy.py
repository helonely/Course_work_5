from abc import ABC, abstractmethod
import requests
from config import hh_api_config


class ABCParser(ABC):

    @abstractmethod
    def get_vacancies_data(self, *args, **kwargs):
        pass


class HHParser(ABCParser):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'page': 0,
            'employer_id': hh_api_config.get('employer_ids'),
            'only_with_salary': hh_api_config.get('only_with_salary'),
            'per_page': hh_api_config.get('vacation_per_page'),
            'area': hh_api_config.get('area')
        }

    def get_vacancies_data(self) -> list[dict]:
        """Получаем данные по вакансиям"""
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.json()['items']

    def get_employers_data(self) -> list[dict]:
        """Получаем данные по работодателям"""
        employers_data = []
        for employer in hh_api_config.get('employer_ids'):
            url = f'https://api.hh.ru/employers/{employer}'
            response = requests.get(url, headers=self.headers)
            employer_data = {
                'id': response.json()['id'],
                'name': response.json()['name'],
                'url': response.json()['alternate_url']
            }
            employers_data.append(employer_data)
        return employers_data


if __name__ == '__main__':
    hh = HHParser()
    print(hh.get_vacancies_data())
    print(hh.get_employers_data())
