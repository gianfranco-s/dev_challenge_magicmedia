from dataclasses import dataclass, asdict
from enum import Enum

from grpc import Channel

import proto_py.rpc_create_vacancy_pb2 as rpc__create__vacancy__pb2
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


def create_vacancy(vacancy_item: VacancyCreate, channel: Channel) -> str:
    vacancy_stub = VacancyServiceStub(channel)
    create_vacancy_request = rpc__create__vacancy__pb2.CreateVacancyRequest(**asdict(vacancy_item))
    response = vacancy_stub.CreateVacancy(create_vacancy_request)

    return response.vacancy.Id


def read_vacancy(vacancy_id: str, channel: Channel) -> Vacancy:
    vacancy_stub = VacancyServiceStub(channel)
    vacancy_request = vacancy__service__pb2.VacancyRequest(Id=vacancy_id)
    response = vacancy_stub.GetVacancy(vacancy_request)

    return response.vacancy
