# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='location_event.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14location_event.proto\"K\n\x14\x45ventLocationMessage\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08latitude\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\x05\x32Y\n\x14\x45ventLocationService\x12\x41\n\x11GetServerResponse\x12\x15.EventLocationMessage\x1a\x15.EventLocationMessageb\x06proto3'
)




_EVENTLOCATIONMESSAGE = _descriptor.Descriptor(
  name='EventLocationMessage',
  full_name='EventLocationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='EventLocationMessage.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='EventLocationMessage.latitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='EventLocationMessage.longitude', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['EventLocationMessage'] = _EVENTLOCATIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventLocationMessage = _reflection.GeneratedProtocolMessageType('EventLocationMessage', (_message.Message,), {
  'DESCRIPTOR' : _EVENTLOCATIONMESSAGE,
  '__module__' : 'location_event_pb2'
  # @@protoc_insertion_point(class_scope:EventLocationMessage)
  })
_sym_db.RegisterMessage(EventLocationMessage)



_EVENTLOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='EventLocationService',
  full_name='EventLocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=101,
  serialized_end=190,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='EventLocationService.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_EVENTLOCATIONMESSAGE,
    output_type=_EVENTLOCATIONMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTLOCATIONSERVICE)

DESCRIPTOR.services_by_name['EventLocationService'] = _EVENTLOCATIONSERVICE

# @@protoc_insertion_point(module_scope)