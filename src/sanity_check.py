import grpc

from dotenv import dotenv_values
from proto_py.vacancy_service_pb2_grpc import VacancyServiceStub

VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')


def server_check(server_address: str) -> bool:
    channel = grpc.insecure_channel(server_address)

    stub = VacancyServiceStub(grpc.channel_ready_future(channel).result())

    try:
        response = stub.GetVacancies()
        print("Server connection successful! Version:", response.version)
    except Exception as e:
        print("Error connecting to server:", e)

    # Close the channel to release resources
    channel.close()


if __name__ == '__main__':
    server_check(VACANCY_SERVER_URL)
