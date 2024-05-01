from locust_vacancy_user import VacancyUser
from grpc_handlers import create_channel

class VacancyUserOne(VacancyUser):
    def on_start(self) -> None:
        self.flow_init(0)


class VacancyUserTwo(VacancyUser):
    def on_start(self) -> None:
        self.flow_init(1)


class VacancyUserThree(VacancyUser):
    def on_start(self) -> None:
        self.flow_init(2)