import json
from typing import List

from dotenv import dotenv_values
from locust import HttpUser, task, between

from grpc_handlers import create_channel, Channel, user_signin, VacancyCreate, VacancyHandler, VacancyUpdate

VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')


class VacancyUser(HttpUser):
    wait_time = between(30, 60)

    def __init__(self, server_address: str = VACANCY_SERVER_URL):
        self.channel = create_channel(server_address)

    @task
    def recurring_flow_(self):
        users = self._load_users()
        self.login(channel=self.channel, **users[0])

        while True:
            self._single_test(self.channel)

    @staticmethod
    def _single_test(channel: Channel) -> None:
        vacancy_handler = VacancyHandler(channel)
        vacancy_item = VacancyCreate.generate_random()

        vacancy_id = vacancy_handler.create_vacancy(vacancy_item)

        print(f'Created vacancy wih Id: {vacancy_id}\n')

        retrieved_vacancy_data = vacancy_handler.read_vacancy(vacancy_id)
        print(f'{retrieved_vacancy_data=}\n')

        vacancies = vacancy_handler.read_vacancies()
        print(f'Current vacancy Ids: {vacancies}\n')

        updated_vacancy = vacancy_handler.update_vacancy(VacancyUpdate(Id=vacancy_id, Country=f'NEW_{retrieved_vacancy_data.Country}_NEW'))
        print(f'{updated_vacancy=}\n')

        is_deleted = vacancy_handler.delete_vacancy(vacancy_id=vacancy_id)
        print(f'Vacancy Id={vacancy_id} is deleted: {is_deleted}\n')

    @staticmethod
    def login(channel: Channel, user_name: str, user_email: str, user_pwd: str) -> None:
        is_user_signed_in = user_signin(user_email, user_pwd, channel)
        print(f'User {user_name} is signed in: {is_user_signed_in}\n')

    @staticmethod
    def _load_users(users_filename: str = 'test_users.json') -> List[dict]:
        with open(users_filename, 'r') as f:
            return json.load(f)
