from locust import User, task, constant

from grpc_handlers import create_channel, vacancy_crud, user_signin


class VacancyUser(User):
    abstract = True
    wait_time = constant(30)
    user_credentials = None

    def on_start(self) -> None:
        self.channel = create_channel(self.host)

    @task
    def vacancy_flow_test(self) -> None:
        if self.user_credentials is not None:
            user_signin(self.channel, **self.user_credentials, verbose=True)
        vacancy_crud(self.channel, verbose=True)

