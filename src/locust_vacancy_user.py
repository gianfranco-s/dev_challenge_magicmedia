import gevent

from locust import constant, task, User
from locust.env import Environment
from locust.user.users import UserMeta

from grpc_handlers import create_grpc_channel, read_vacancies_idlist, vacancy_crud, user_signin, Channel

VACANCY_WAIT_SECONDS = 10
BACKGROUND_RETRIEVE_VACANCIES_SECONDS = 15


class VacancyUser(User):
    abstract = True
    wait_time = constant(VACANCY_WAIT_SECONDS)
    user_credentials = None
    channel = None

    def __init__(self, environment: Environment, credentials_idx: int) -> None:
        super().__init__(environment)
        self.user_credentials = self.credentials_init(environment.user_classes[credentials_idx])

    def on_start(self) -> None:
        self.channel = self.create_channel(self.host)
        gevent.spawn(self._on_background, self.channel)

    @task
    def vacancy_flow_test(self) -> None:
        if self.user_credentials is not None:
            user_signin(self.channel, **self.user_credentials, verbose=True)
        vacancy_crud(self.channel, verbose=True)

    @staticmethod
    def credentials_init(user_classes_data: UserMeta) -> dict:
        """Initializes user credentials given in environment.user_classes"""
        return {
            'name': user_classes_data.name,
            'email': user_classes_data.email,
            'password': user_classes_data.password,
        }
        # print(self.user_credentials)

    @staticmethod
    def _on_background(channel: Channel, interval_seconds: int = BACKGROUND_RETRIEVE_VACANCIES_SECONDS) -> None:
        while True:
            gevent.sleep(interval_seconds)
            read_vacancies_idlist(channel, verbose=True)

    @staticmethod
    def create_channel(server_address: str) -> Channel:
        return create_grpc_channel(server_address)
