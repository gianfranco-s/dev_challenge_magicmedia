import json

from dotenv import dotenv_values
from grpc import insecure_channel

from user_signin import user_signin
from vacancy_handler import create_vacancy, read_vacancy, VacancyCreate, DIVISION

VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')


def main(server_address: str) -> None:
    with open('test_users.json', 'r') as f:
        registered_user = json.load(f)[0]
    
    channel = insecure_channel(server_address)
    # user_signin(registered_user['email'], registered_user['password'], channel)
    # vacancy_item = Vacancy('60-title-60',
    #                        'test-description',
    #                        DIVISION.SALES.value,
    #                        'Uqbar',)

    # vacancy_id = create_vacancy(vacancy_item, channel=channel)
    # print(f'{vacancy_id=}')
    read_vacancy(vacancy_id='66304697cf1eb847f0f47c2a', channel=channel)


if __name__ == '__main__':
    main(VACANCY_SERVER_URL)