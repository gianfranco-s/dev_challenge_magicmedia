# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc_signin_user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15rpc_signin_user.proto\x12\x02pb\"2\n\x0fSignInUserInput\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"Q\n\x12SignInUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\tB\x14Z\x12\x63yrex/vacancies/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_signin_user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022cyrex/vacancies/pb'
  _globals['_SIGNINUSERINPUT']._serialized_start=29
  _globals['_SIGNINUSERINPUT']._serialized_end=79
  _globals['_SIGNINUSERRESPONSE']._serialized_start=81
  _globals['_SIGNINUSERRESPONSE']._serialized_end=162
# @@protoc_insertion_point(module_scope)
