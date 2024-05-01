import gevent

from locust_vacancy_user import VacancyUser

class VacancyUserOne(VacancyUser):
    def on_start(self) -> None:
        self.channel = self.create_channel(self.host)
        gevent.spawn(self._on_background, self.channel)
        self.credentials_init(0)

class VacancyUserTwo(VacancyUser):
    def on_start(self) -> None:
        self.channel = self.create_channel(self.host)
        gevent.spawn(self._on_background, self.channel)
        self.credentials_init(1)


class VacancyUserThree(VacancyUser):
    def on_start(self) -> None:
        self.channel = self.create_channel(self.host)
        gevent.spawn(self._on_background, self.channel)
        self.credentials_init(2)
