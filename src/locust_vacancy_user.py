import gevent

from locust import constant, task, User

from grpc_handlers import create_grpc_channel, read_vacancies_idlist, vacancy_crud, user_signin, Channel


VACANCY_WAIT_SECONDS = 30
BACKGROUND_RETRIEVE_VACANCIES_SECONDS = 45


class VacancyUser(User):
    abstract = True
    wait_time = constant(VACANCY_WAIT_SECONDS)
    user_credentials = None
    channel = None

    def on_start(self) -> None:
        self.channel = self.create_channel(self.host)
        gevent.spawn(self._on_background, self.channel)
        # self.credentials_init(0)

    @task
    def vacancy_flow_test(self) -> None:
        if self.user_credentials is not None:
            user_signin(self.channel, **self.user_credentials, verbose=True)
        vacancy_crud(self.channel, verbose=True)

    def credentials_init(self, credentials_idx: int) -> None:
        """Initializes user credentials given in environment.user_classes"""

        self.user_credentials = {
            'name': self.environment.user_classes[credentials_idx].name,
            'email': self.environment.user_classes[credentials_idx].email,
            'password': self.environment.user_classes[credentials_idx].password,
        }
        print(self.user_credentials)

    @staticmethod
    def _on_background(channel: Channel, interval_seconds: int = BACKGROUND_RETRIEVE_VACANCIES_SECONDS) -> None:
        while True:
            gevent.sleep(interval_seconds)
            read_vacancies_idlist(channel, verbose=True)

    @staticmethod
    def create_channel(server_address: str) -> Channel:
        return create_grpc_channel(server_address)
