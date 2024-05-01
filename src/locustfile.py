from locust.env import Environment

from locust_vacancy_user import VacancyUser

class VacancyUserOne(VacancyUser):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment, 0)

class VacancyUserTwo(VacancyUser):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment, 1)


class VacancyUserThree(VacancyUser):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment, 2)
