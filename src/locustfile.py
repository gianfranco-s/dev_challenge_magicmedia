import json
import random

from typing import List

from locust import HttpUser, task, constant

from grpc_handlers import create_channel, vacancy_crud, user_signin


class VacancyUser(HttpUser):
    wait_time = constant(30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = create_channel(self.host)
        self.user = self._load_random_user()

    @task
    def vacancy_flow_test(self):
        user_signin(self.channel, **self.user, verbose=True)
        vacancy_crud(self.channel, verbose=True)

    @staticmethod
    def _load_random_user(users_filename: str = 'test_users.json') -> List[dict]:
        with open(users_filename, 'r') as f:
            return random.choice(json.load(f))
