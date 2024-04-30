import json

import grpc
import grpc._channel
import proto_py.rpc_signin_user_pb2 as rpc__signin__user__pb2

from dotenv import dotenv_values
from proto_py.auth_service_pb2_grpc import AuthServiceStub

VACANCY_SERVER_URL = dotenv_values().get('VACANCY_SERVER_URL')


def sign_in_user(user_email: str, user_pwd: str, server_address: str = VACANCY_SERVER_URL) -> bool:
    """ Sign-in valid user. If log in is successful, returns True. """
    channel = grpc.insecure_channel(server_address)

    auth_stub = AuthServiceStub(channel)

    sign_in_request = rpc__signin__user__pb2.SignInUserInput(
        email=user_email,
        password=user_pwd
    )

    try: 
        response = auth_stub.SignInUser(sign_in_request)
        is_user_signed_in = response.status == 'success'
    except grpc._channel._InactiveRpcError as e:
        print(e._state.details)
        print(e._state.code)
        is_user_signed_in = False

    return is_user_signed_in
    

if __name__ == "__main__":
    with open('test_users.json', 'r') as f:
        test_users = json.load(f)
    
    registered_user = test_users[0]
    is_user_signed_in = sign_in_user(registered_user['email'], registered_user['password'])
    print(f'User {registered_user["name"]} is signed in: {is_user_signed_in}\n')

    unregistered_user = test_users[3]
    is_user_signed_in = sign_in_user(unregistered_user['email'], unregistered_user['password'])
    print(f'User {registered_user["name"]} is signed in: {is_user_signed_in}\n')
