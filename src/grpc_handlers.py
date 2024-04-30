import json
import random

from dataclasses import dataclass, asdict
from enum import Enum
from typing import List

from grpc import insecure_channel, Channel
from grpc._channel import _InactiveRpcError
from google.protobuf.timestamp_pb2 import Timestamp

import proto_py.rpc_create_vacancy_pb2 as rpc__create__vacancy__pb2
import proto_py.rpc_signin_user_pb2 as rpc__signin__user__pb2
import proto_py.rpc_update_vacancy_pb2 as rpc__update__vacancy__pb2
import proto_py.vacancy_service_pb2 as vacancy__service__pb2

from proto_py.auth_service_pb2_grpc import AuthServiceStub
from proto_py.vacancy_pb2 import Vacancy
from proto_py.vacancy_service_pb2_grpc import VacancyServiceStub


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

    @classmethod
    def generate_random(cls) -> 'VacancyCreate':
        """Generates a VacancyCreate object with random values."""
        titles = ['Tlön, Uqbar', 'Funes', 'Titus', 'Labyrinth']
        descriptions = ['Orbis Tertius', 'The Library', 'Why so Sirius?']
        divisions = list(DIVISION)
        countries = ['Axaxaxas-mlö', 'Babylonia', 'Atlantis']

        return cls(
            Title=random.choice(titles),
            Description=random.choice(descriptions),
            Division=random.choice(divisions).value,
            Country=random.choice(countries)
        )


@dataclass
class VacancyUpdate:
    Id: str
    Title: str = None
    Description: str = None
    Views: int = None
    Division: DIVISION = None
    Country: str = None


@dataclass
class VacancyFull:
    Id: str
    Title: str = None
    Description: str = None
    Views: int = None
    Division: DIVISION = None
    Country: str = None
    created_at: Timestamp = None
    updated_at: Timestamp = None

    def __repr__(self):
        division_name = self.Division.name if self.Division else None
        return f"VacancyFull(\n\
                 Id='{self.Id}',\n\
                 Title='{self.Title}',\n\
                 Description='{self.Description}',\n\
                 Views={self.Views},\n\
                 Division='{division_name}',\n\
                 Country='{self.Country}',\n\
                 created_at=(seconds: {self.created_at.seconds}, nanos: {self.created_at.nanos}),\n\
                 updated_at=(seconds: {self.updated_at.seconds}, nanos: {self.updated_at.nanos})\n\
                 )"


def create_channel(server_url: str) -> Channel:
    return insecure_channel(server_url)


def user_signin(channel: Channel, name: str, email: str, password: str, verbose: bool = False) -> bool:
    """ Sign-in valid user. If log in is successful, returns True. """
    auth_stub = AuthServiceStub(channel)

    sign_in_request = rpc__signin__user__pb2.SignInUserInput(email=email, password=password)

    try:
        response = auth_stub.SignInUser(sign_in_request)
        is_user_signed_in = response.status == 'success'
    except _InactiveRpcError as e:
        print(e._state.details)
        print(e._state.code)
        is_user_signed_in = False

    if verbose:
        print(f'User {name} is signed in: {is_user_signed_in}\n')

    return is_user_signed_in


class VacancyHandler:
    def __init__(self, channel: Channel, verbose: bool = False) -> None:
        self.vacancy_stub = VacancyServiceStub(channel)
        self.verbose = verbose

    def create_vacancy(self, vacancy_item: VacancyCreate) -> str:
        """After successful creation returns Id"""
        create_vacancy_request = rpc__create__vacancy__pb2.CreateVacancyRequest(**asdict(vacancy_item))
        response = self.vacancy_stub.CreateVacancy(create_vacancy_request)

        vacancy_id = response.vacancy.Id
        if self.verbose:
            print(f'Created vacancy wih Id: {vacancy_id}\n')

        return vacancy_id

    def read_vacancy(self, vacancy_id: str) -> VacancyFull:
        """Returns Vacancy item"""
        vacancy_request = vacancy__service__pb2.VacancyRequest(Id=vacancy_id)
        response = self.vacancy_stub.GetVacancy(vacancy_request)

        retrieved_vacancy_data = self.unpack_vacancy(response.vacancy)

        if self.verbose:
            print(f'{retrieved_vacancy_data=}\n')

        return retrieved_vacancy_data

    def read_vacancies(self) -> List[str]:
        """Returns list of Id for existing vacancies"""
        vacancies_request = vacancy__service__pb2.GetVacanciesRequest()
        response = self.vacancy_stub.GetVacancies(vacancies_request)

        vacancies = []
        for vacancy in response:
            if self.verbose:
                print(vacancy)
            vacancies.append(vacancy.Id)

        return vacancies

    def delete_vacancy(self, vacancy_id: str) -> bool:
        """Returns status as bool"""
        vacancy_request = vacancy__service__pb2.VacancyRequest(Id=vacancy_id)
        response = self.vacancy_stub.DeleteVacancy(vacancy_request)

        is_deleted = response.success

        if self.verbose:
            print(f'Vacancy Id={vacancy_id} is deleted: {is_deleted}\n')

        return is_deleted

    def update_vacancy(self, vacancy_item: VacancyUpdate) -> VacancyFull:
        """Returns Vacancy item"""
        update_vacancy_request = rpc__update__vacancy__pb2.UpdateVacancyRequest(**asdict(vacancy_item))
        response = self.vacancy_stub.UpdateVacancy(update_vacancy_request)

        updated_vacancy = self.unpack_vacancy(response.vacancy)
        if self.verbose:
            print(f'{updated_vacancy=}\n')

        return updated_vacancy
    
    @staticmethod
    def unpack_vacancy(vacancy: Vacancy) -> VacancyFull:
        return VacancyFull(Id=vacancy.Id,
                           Title=vacancy.Title,
                           Description=vacancy.Description,
                           Views=vacancy.Views,
                           Division=DIVISION(vacancy.Division),
                           Country=vacancy.Country,
                           created_at=vacancy.created_at,
                           updated_at=vacancy.updated_at)


def vacancy_test(channel: Channel, verbose: bool) -> None:
    """Manual test of all VacancyHandler methods"""

    vacancy_handler = VacancyHandler(channel, verbose=verbose)
    vacancy_item = VacancyCreate.generate_random()

    vacancy_id = vacancy_handler.create_vacancy(vacancy_item)

    retrieved_vacancy_data = vacancy_handler.read_vacancy(vacancy_id)

    vacancies = vacancy_handler.read_vacancies()

    updated_vacancy = vacancy_handler.update_vacancy(VacancyUpdate(Id=vacancy_id, Country=f'NEW_{retrieved_vacancy_data.Country}_NEW'))

    is_deleted = vacancy_handler.delete_vacancy(vacancy_id=vacancy_id)


if __name__ == '__main__':
    from dotenv import dotenv_values

    VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')

    verbose = True
    
    channel = create_channel(VACANCY_SERVER_URL)
    with open('test_users.json', 'r') as f:
        registered_user = json.load(f)[0]

    is_user_signed_in = user_signin(channel, **registered_user, verbose=verbose)

    vacancy_test(channel, verbose=verbose)
