# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vacancy.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rvacancy.proto\x12\x02pb\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa2\x02\n\x07Vacancy\x12\n\n\x02Id\x18\x01 \x01(\t\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t\x12\r\n\x05Views\x18\x04 \x01(\x05\x12&\n\x08\x44ivision\x18\x05 \x01(\x0e\x32\x14.pb.Vacancy.DIVISION\x12\x0f\n\x07\x43ountry\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"?\n\x08\x44IVISION\x12\x0f\n\x0b\x44\x45VELOPMENT\x10\x00\x12\x0c\n\x08SECURITY\x10\x01\x12\t\n\x05SALES\x10\x02\x12\t\n\x05OTHER\x10\x03\"/\n\x0fVacancyResponse\x12\x1c\n\x07vacancy\x18\x01 \x01(\x0b\x32\x0b.pb.VacancyB\x14Z\x12\x63yrex/vacancies/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vacancy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022cyrex/vacancies/pb'
  _globals['_VACANCY']._serialized_start=55
  _globals['_VACANCY']._serialized_end=345
  _globals['_VACANCY_DIVISION']._serialized_start=282
  _globals['_VACANCY_DIVISION']._serialized_end=345
  _globals['_VACANCYRESPONSE']._serialized_start=347
  _globals['_VACANCYRESPONSE']._serialized_end=394
# @@protoc_insertion_point(module_scope)
