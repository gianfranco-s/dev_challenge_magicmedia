import random

from dataclasses import dataclass
from enum import Enum

from google.protobuf.timestamp_pb2 import Timestamp


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
