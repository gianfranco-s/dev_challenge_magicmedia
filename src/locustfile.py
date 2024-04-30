import json

from typing import List

from dotenv import dotenv_values
from locust import HttpUser, task, between

from vacancy_handler import DIVISION, VacancyCreate, VacancyHandler, VacancyUpdate
from user_signin import user_signin

VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')


class VacancyUser(HttpUser):
    wait_time = between(30, 60)

    def __init__(self, server_address: str = VACANCY_SERVER_URL):
        self.vacancy_handler = VacancyHandler(server_address)

    @task
    def recurring_flow_(self):
        users = self.load_users()
        self.login(users[0].get('email'), users[0].get('password'))

        while True:
            self.single_test()

    def single_test(self):
        vacancy_item = VacancyCreate(Title='Tlön, Uqbar',
                                     Description='Orbis Tertius',
                                     Division=DIVISION.SALES.value,
                                     Country='Axaxaxas-mlö')

        vacancy_id = self.vacancy_handler.create_vacancy(vacancy_item)

        print(f'Created vacancy wih Id: {vacancy_id}\n')

        vacancy_data = self.vacancy_handler.read_vacancy(vacancy_id)
        print(f'{vacancy_data=}\n')

        vacancies = self.vacancy_handler.read_vacancies()
        print(f'Current vacancy Ids: {vacancies}\n')

        updated_vacancy = self.vacancy_handler.update_vacancy(VacancyUpdate(Id=vacancy_id, Country='Ookbar-yay!'))
        print(f'{updated_vacancy=}\n')

        is_deleted = self.vacancy_handler.delete_vacancy(vacancy_id=vacancy_id)
        print(f'Vacancy Id={vacancy_id} is deleted: {is_deleted}\n')

    def load_users(self, users_filename: str = 'test_users.json') -> List[dict]:
        with open(users_filename, 'r') as f:
            return json.load(f)

    def login(self, user_name: str, user_email: str, user_pwd: str) -> None:
        channel = self.vacancy_handler.channel
        is_user_signed_in = user_signin(user_email, user_pwd, channel)
        print(f'User {user_name} is signed in: {is_user_signed_in}\n')
