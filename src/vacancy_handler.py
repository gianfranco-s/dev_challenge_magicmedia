from dataclasses import dataclass, asdict
from enum import Enum
from typing import List

from grpc import insecure_channel

import proto_py.rpc_create_vacancy_pb2 as rpc__create__vacancy__pb2
import proto_py.rpc_update_vacancy_pb2 as rpc__update__vacancy__pb2
import proto_py.vacancy_service_pb2 as vacancy__service__pb2
from proto_py.vacancy_service_pb2_grpc import VacancyServiceStub
from proto_py.vacancy_pb2 import Vacancy


@dataclass
class DIVISION(Enum):
    DEVELOPMENT = 0
    SECURITY = 1
    SALES = 2
    OTHER = 3


@dataclass
class VacancyCreate:
    Title: str
    Description: str
    Division: DIVISION
    Country: str


@dataclass
class VacancyUpdate:
    Id: str
    Title: str = None
    Description: str = None
    Views: int = None
    Division: DIVISION = None
    Country: str = None


class VacancyHandler:
    def __init__(self, server_url: str) -> None:
        self.channel = insecure_channel(server_url)
        self.vacancy_stub = VacancyServiceStub(self.channel)

    def create_vacancy(self, vacancy_item: VacancyCreate) -> str:
        """After successful creation returns Id"""
        create_vacancy_request = rpc__create__vacancy__pb2.CreateVacancyRequest(**asdict(vacancy_item))
        response = self.vacancy_stub.CreateVacancy(create_vacancy_request)

        return response.vacancy.Id

    def read_vacancy(self, vacancy_id: str) -> Vacancy:
        """Returns Vacancy item"""
        vacancy_request = vacancy__service__pb2.VacancyRequest(Id=vacancy_id)
        response = self.vacancy_stub.GetVacancy(vacancy_request)

        return response.vacancy

    def read_vacancies(self) -> List[str]:
        """Returns list of Id for existing vacancies"""
        vacancies_request = vacancy__service__pb2.GetVacanciesRequest()
        response = self.vacancy_stub.GetVacancies(vacancies_request)

        vacancies = []
        for vacancy in response:
            vacancies.append(vacancy.Id)

        return vacancies

    def delete_vacancy(self, vacancy_id: str) -> bool:
        """Returns status as bool"""
        vacancy_request = vacancy__service__pb2.VacancyRequest(Id=vacancy_id)
        response = self.vacancy_stub.DeleteVacancy(vacancy_request)

        return response.success

    def update_vacancy(self, vacancy_item: VacancyUpdate) -> Vacancy:
        """Returns Vacancy item"""
        update_vacancy_request = rpc__update__vacancy__pb2.UpdateVacancyRequest(**asdict(vacancy_item))
        response = self.vacancy_stub.UpdateVacancy(update_vacancy_request)

        return response.vacancy


if __name__ == '__main__':
    import json

    from dotenv import dotenv_values
    from user_signin import user_signin

    VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')

    with open('test_users.json', 'r') as f:
        registered_user = json.load(f)[0]

    vacancy_handler = VacancyHandler(VACANCY_SERVER_URL)
    channel = vacancy_handler.channel

    is_user_signed_in = user_signin(registered_user['email'], registered_user['password'], channel)
    print(f'User {registered_user["name"]} is signed in: {is_user_signed_in}\n')

    vacancy_item = VacancyCreate(Title='Tlön, Uqbar',
                                 Description='Orbis Tertius',
                                 Division=DIVISION.SALES.value,
                                 Country='Axaxaxas-mlö')
    vacancy_id = vacancy_handler.create_vacancy(vacancy_item)

    print(f'Created vacancy wih Id: {vacancy_id}\n')

    vacancy_data = vacancy_handler.read_vacancy(vacancy_id)
    print(f'{vacancy_data=}\n')

    vacancies = vacancy_handler.read_vacancies()
    print(f'Current vacancy Ids: {vacancies}\n')

    updated_vacancy = vacancy_handler.update_vacancy(VacancyUpdate(Id=vacancy_id, Country='Ookbar-yay!'))
    print(f'{updated_vacancy=}\n')

    is_deleted = vacancy_handler.delete_vacancy(vacancy_id=vacancy_id)
    print(f'Vacancy Id={vacancy_id} is deleted: {is_deleted}\n')
