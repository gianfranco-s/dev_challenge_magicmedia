from locust_vacancy_user import VacancyUser
from grpc_handlers import create_channel

class VacancyUserOne(VacancyUser):
    def on_start(self) -> None:
        self.channel = create_channel(self.host)
        self.user_credentials = {
            'name': self.environment.user_classes[0].name,
            'email': self.environment.user_classes[0].email,
            'password': self.environment.user_classes[0].password,
        }
        print(self.user_credentials)


class VacancyUserTwo(VacancyUser):
    def on_start(self) -> None:
        self.channel = create_channel(self.host)
        self.user_credentials = {
            'name': self.environment.user_classes[1].name,
            'email': self.environment.user_classes[1].email,
            'password': self.environment.user_classes[1].password,
        }
        print(self.user_credentials)


class VacancyUserThree(VacancyUser):
    def on_start(self) -> None:
        self.channel = create_channel(self.host)
        self.user_credentials = {
            'name': self.environment.user_classes[2].name,
            'email': self.environment.user_classes[2].email,
            'password': self.environment.user_classes[2].password,
        }
        print(self.user_credentials)
