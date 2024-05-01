from locust.env import Environment

from locust_vacancy_user import VacancyUser

class VacancyUserOne(VacancyUser):
    def __init__(self, environment: Environment, credentials_idx: int = 0) -> None:
        super().__init__(environment, credentials_idx)


class VacancyUserTwo(VacancyUser):
    def __init__(self, environment: Environment, credentials_idx: int = 1) -> None:
        super().__init__(environment, credentials_idx)


class VacancyUserThree(VacancyUser):
    def __init__(self, environment: Environment, credentials_idx: int = 2) -> None:
        super().__init__(environment, credentials_idx)
