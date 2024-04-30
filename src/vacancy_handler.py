from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum

from grpc import Channel

import proto_py.rpc_create_vacancy_pb2 as rpc__create__vacancy__pb2
from proto_py.vacancy_service_pb2_grpc import VacancyServiceStub


@dataclass
class DIVISION(Enum):
    DEVELOPMENT = 0
    SECURITY = 1
    SALES = 2
    OTHER = 3


@dataclass
class Vacancy:
    Title: str
    Description: str
    Division: DIVISION
    Country: str


def create_vacancy(vacancy_item: Vacancy, channel: Channel) -> str:
    vacancy_stub = VacancyServiceStub(channel)
    create_vacancy_request = rpc__create__vacancy__pb2.CreateVacancyRequest(**asdict(vacancy_item))
    response = vacancy_stub.CreateVacancy(create_vacancy_request)

    return response.vacancy.Id
