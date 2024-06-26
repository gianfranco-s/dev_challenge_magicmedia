import gevent

from types import new_class

from locust import constant, task, User
from locust.env import Environment
from locust.user.users import UserMeta

from grpc_handlers import create_grpc_channel, read_vacancies_idlist, vacancy_crud, user_signin, Channel

VACANCY_WAIT_SECONDS = 30
BACKGROUND_RETRIEVE_VACANCIES_SECONDS = 45


class VacancyUser(User):
    abstract = True
    wait_time = constant(VACANCY_WAIT_SECONDS)
    user_credentials = None
    channel = None

    def __init__(self, environment: Environment, credentials_idx: int) -> None:
        super().__init__(environment)
        self.user_credentials = self._load_credentials(environment.user_classes[credentials_idx])

    def on_start(self) -> None:
        self.channel = self.create_channel(self.host)
        gevent.spawn(self._on_background, self.channel)

    @task
    def vacancy_flow_test(self) -> None:
        if self.user_credentials is not None:
            user_signin(self.channel, **self.user_credentials, verbose=True)
        vacancy_crud(self.channel, verbose=True)

    @staticmethod
    def _load_credentials(user_classes_data: UserMeta) -> dict:
        """Initializes user credentials given in environment.user_classes"""
        if user_classes_data is not None:
            return {
                'name': user_classes_data.name,
                'email': user_classes_data.email,
                'password': user_classes_data.password,
            }

    @staticmethod
    def _on_background(channel: Channel, interval_seconds: int = BACKGROUND_RETRIEVE_VACANCIES_SECONDS) -> None:
        while True:
            gevent.sleep(interval_seconds)
            read_vacancies_idlist(channel, verbose=True, skip_read_vacancies=True)

    @staticmethod
    def create_channel(server_address: str) -> Channel:
        return create_grpc_channel(server_address)


def create_vacancy_user_class(class_name: str, credentials_idx: int) -> VacancyUser:
    """Dynamically creates a new class inheriting from VacancyUser"""

    VacancyUserSubclass = new_class(class_name, (VacancyUser,))

    # Define the __init__ method within the new class
    def __init__(self, environment: Environment):
        super(VacancyUserSubclass, self).__init__(environment, credentials_idx)

    VacancyUserSubclass.__init__ = __init__

    return VacancyUserSubclass
