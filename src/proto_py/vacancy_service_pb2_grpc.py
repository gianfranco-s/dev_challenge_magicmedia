# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto_py.rpc_create_vacancy_pb2 as rpc__create__vacancy__pb2
import proto_py.rpc_update_vacancy_pb2 as rpc__update__vacancy__pb2
import proto_py.vacancy_pb2 as vacancy__pb2
import proto_py.vacancy_service_pb2 as vacancy__service__pb2


class VacancyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateVacancy = channel.unary_unary(
                '/pb.VacancyService/CreateVacancy',
                request_serializer=rpc__create__vacancy__pb2.CreateVacancyRequest.SerializeToString,
                response_deserializer=vacancy__pb2.VacancyResponse.FromString,
                )
        self.GetVacancy = channel.unary_unary(
                '/pb.VacancyService/GetVacancy',
                request_serializer=vacancy__service__pb2.VacancyRequest.SerializeToString,
                response_deserializer=vacancy__pb2.VacancyResponse.FromString,
                )
        self.GetVacancies = channel.unary_stream(
                '/pb.VacancyService/GetVacancies',
                request_serializer=vacancy__service__pb2.GetVacanciesRequest.SerializeToString,
                response_deserializer=vacancy__pb2.Vacancy.FromString,
                )
        self.UpdateVacancy = channel.unary_unary(
                '/pb.VacancyService/UpdateVacancy',
                request_serializer=rpc__update__vacancy__pb2.UpdateVacancyRequest.SerializeToString,
                response_deserializer=vacancy__pb2.VacancyResponse.FromString,
                )
        self.DeleteVacancy = channel.unary_unary(
                '/pb.VacancyService/DeleteVacancy',
                request_serializer=vacancy__service__pb2.VacancyRequest.SerializeToString,
                response_deserializer=vacancy__service__pb2.DeleteVacancyResponse.FromString,
                )


class VacancyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVacancies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVacancy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VacancyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVacancy,
                    request_deserializer=rpc__create__vacancy__pb2.CreateVacancyRequest.FromString,
                    response_serializer=vacancy__pb2.VacancyResponse.SerializeToString,
            ),
            'GetVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVacancy,
                    request_deserializer=vacancy__service__pb2.VacancyRequest.FromString,
                    response_serializer=vacancy__pb2.VacancyResponse.SerializeToString,
            ),
            'GetVacancies': grpc.unary_stream_rpc_method_handler(
                    servicer.GetVacancies,
                    request_deserializer=vacancy__service__pb2.GetVacanciesRequest.FromString,
                    response_serializer=vacancy__pb2.Vacancy.SerializeToString,
            ),
            'UpdateVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateVacancy,
                    request_deserializer=rpc__update__vacancy__pb2.UpdateVacancyRequest.FromString,
                    response_serializer=vacancy__pb2.VacancyResponse.SerializeToString,
            ),
            'DeleteVacancy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVacancy,
                    request_deserializer=vacancy__service__pb2.VacancyRequest.FromString,
                    response_serializer=vacancy__service__pb2.DeleteVacancyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.VacancyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VacancyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.VacancyService/CreateVacancy',
            rpc__create__vacancy__pb2.CreateVacancyRequest.SerializeToString,
            vacancy__pb2.VacancyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.VacancyService/GetVacancy',
            vacancy__service__pb2.VacancyRequest.SerializeToString,
            vacancy__pb2.VacancyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVacancies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pb.VacancyService/GetVacancies',
            vacancy__service__pb2.GetVacanciesRequest.SerializeToString,
            vacancy__pb2.Vacancy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.VacancyService/UpdateVacancy',
            rpc__update__vacancy__pb2.UpdateVacancyRequest.SerializeToString,
            vacancy__pb2.VacancyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteVacancy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.VacancyService/DeleteVacancy',
            vacancy__service__pb2.VacancyRequest.SerializeToString,
            vacancy__service__pb2.DeleteVacancyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
