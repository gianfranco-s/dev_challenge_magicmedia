import proto_py.rpc_signin_user_pb2 as rpc__signin__user__pb2

from grpc import Channel
from grpc._channel import _InactiveRpcError

from proto_py.auth_service_pb2_grpc import AuthServiceStub


def user_signin(user_email: str, user_pwd: str, channel: Channel) -> bool:
    """ Sign-in valid user. If log in is successful, returns True. """
    auth_stub = AuthServiceStub(channel)

    sign_in_request = rpc__signin__user__pb2.SignInUserInput(email=user_email, password=user_pwd)

    try:
        response = auth_stub.SignInUser(sign_in_request)
        is_user_signed_in = response.status == 'success'
    except _InactiveRpcError as e:
        print(e._state.details)
        print(e._state.code)
        is_user_signed_in = False

    return is_user_signed_in
