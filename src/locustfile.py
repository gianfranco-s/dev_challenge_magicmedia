import json
from typing import List

from dotenv import dotenv_values
from locust import HttpUser, task

from grpc_handlers import create_channel, vacancy_test, user_signin

VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')


class VacancyUser(HttpUser):
    wait_time = 30
    host = VACANCY_SERVER_URL

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = create_channel(self.host)
        self.users = self._load_users()

    @task
    def vacancy_flow_test(self):
        for user in self.users:
            user_signin(self.channel, **user, verbose=True)
            vacancy_test(self.channel, verbose=True)

    @staticmethod
    def _load_users(users_filename: str = 'test_users.json') -> List[dict]:
        with open(users_filename, 'r') as f:
            return json.load(f)
