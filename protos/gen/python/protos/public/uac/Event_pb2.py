# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/Event.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uac/Event.proto',
  package='ai.verta.uac',
  syntax='proto3',
  serialized_options=b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac',
  serialized_pb=b'\n\x0fuac/Event.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x14uac/UACService.proto\x1a\x19google/protobuf/any.proto\"\x80\x01\n\x12\x43reateEventRequest\x12\x12\n\nevent_uuid\x18\x01 \x01(\t\x12\x12\n\nevent_type\x18\x02 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x03 \x01(\x04\x12,\n\x0e\x65vent_metadata\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"w\n\x07Webhook\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x03 \x01(\x04\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x15\n\rmutual_secret\x18\x05 \x01(\t\x12\x13\n\x0b\x65vent_types\x18\x06 \x03(\t\"{\n\x12\x46indWebhookRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\x12\r\n\x05names\x18\x02 \x03(\t\x12\x14\n\x0cworkspace_id\x18\x03 \x03(\x04\x1a\x33\n\x08Response\x12\'\n\x08webhooks\x18\x01 \x03(\x0b\x32\x15.ai.verta.uac.Webhook\"\x8c\x01\n\x14\x43reateWebhookRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x02 \x01(\x04\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x15\n\rmutual_secret\x18\x04 \x01(\t\x12\x13\n\x0b\x65vent_types\x18\x05 \x03(\t\x12\x12\n\nall_events\x18\x06 \x01(\x08\"\xb6\x01\n\x14UpdateWebhookRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x14\n\x0cnew_location\x18\x02 \x01(\t\x12\x15\n\rmutual_secret\x18\x03 \x01(\t\x12\x17\n\x0f\x61\x64\x64_event_types\x18\x04 \x03(\t\x12\x1a\n\x12\x64\x65lete_event_types\x18\x05 \x03(\t\x12\x16\n\x0eset_all_events\x18\x06 \x01(\x08\x12\x18\n\x10\x63lear_all_events\x18\x07 \x01(\x08\"#\n\x14\x44\x65leteWebhookRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\"\xb5\x01\n\x0bWebhookCall\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x12\n\nwebhook_id\x18\x02 \x01(\x04\x12\x12\n\nevent_uuid\x18\x03 \x01(\t\x12\x30\n\x06status\x18\x04 \x01(\x0e\x32 .ai.verta.uac.WebhookCall.Status\"@\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\"\xb7\x01\n\x16\x46indWebhookCallRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\x12\x13\n\x0bwebhook_ids\x18\x02 \x03(\x04\x12\x13\n\x0b\x65vent_uuids\x18\x03 \x03(\t\x12\x30\n\x06status\x18\x04 \x03(\x0e\x32 .ai.verta.uac.WebhookCall.Status\x1a\x34\n\x08Response\x12(\n\x05\x63\x61lls\x18\x01 \x03(\x0b\x32\x19.ai.verta.uac.WebhookCall\".\n\x1bRetriggerWebhookCallRequest\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\x04\x32\xdb\x06\n\x0c\x45ventService\x12\x66\n\x0b\x63reateEvent\x12 .ai.verta.uac.CreateEventRequest\x1a\x13.ai.verta.uac.Empty\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/event/createEvent:\x01*\x12n\n\rcreateWebhook\x12\".ai.verta.uac.CreateWebhookRequest\x1a\x15.ai.verta.uac.Webhook\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/event/createWebhook:\x01*\x12n\n\rupdateWebhook\x12\".ai.verta.uac.UpdateWebhookRequest\x1a\x15.ai.verta.uac.Webhook\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/event/updateWebhook:\x01*\x12|\n\x0b\x66indWebhook\x12 .ai.verta.uac.FindWebhookRequest\x1a).ai.verta.uac.FindWebhookRequest.Response\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/event/findWebhook:\x01*\x12l\n\rdeleteWebhook\x12\".ai.verta.uac.DeleteWebhookRequest\x1a\x13.ai.verta.uac.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x17/v1/event/deleteWebhook:\x01*\x12\x8c\x01\n\x0f\x66indWebhookCall\x12$.ai.verta.uac.FindWebhookCallRequest\x1a-.ai.verta.uac.FindWebhookCallRequest.Response\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/event/findWebhookCall:\x01*\x12\x87\x01\n\x14retriggerWebhookCall\x12).ai.verta.uac.RetriggerWebhookCallRequest\x1a\x19.ai.verta.uac.WebhookCall\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/event/retriggerWebhookCall:\x01*B>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,uac_dot_UACService__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])



_WEBHOOKCALL_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ai.verta.uac.WebhookCall.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=972,
  serialized_end=1036,
)
_sym_db.RegisterEnumDescriptor(_WEBHOOKCALL_STATUS)


_CREATEEVENTREQUEST = _descriptor.Descriptor(
  name='CreateEventRequest',
  full_name='ai.verta.uac.CreateEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_uuid', full_name='ai.verta.uac.CreateEventRequest.event_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='ai.verta.uac.CreateEventRequest.event_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='ai.verta.uac.CreateEventRequest.workspace_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_metadata', full_name='ai.verta.uac.CreateEventRequest.event_metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=113,
  serialized_end=241,
)


_WEBHOOK = _descriptor.Descriptor(
  name='Webhook',
  full_name='ai.verta.uac.Webhook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.uac.Webhook.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ai.verta.uac.Webhook.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='ai.verta.uac.Webhook.workspace_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='ai.verta.uac.Webhook.location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutual_secret', full_name='ai.verta.uac.Webhook.mutual_secret', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_types', full_name='ai.verta.uac.Webhook.event_types', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=243,
  serialized_end=362,
)


_FINDWEBHOOKREQUEST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.FindWebhookRequest.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='webhooks', full_name='ai.verta.uac.FindWebhookRequest.Response.webhooks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=436,
  serialized_end=487,
)

_FINDWEBHOOKREQUEST = _descriptor.Descriptor(
  name='FindWebhookRequest',
  full_name='ai.verta.uac.FindWebhookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='ai.verta.uac.FindWebhookRequest.ids', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='names', full_name='ai.verta.uac.FindWebhookRequest.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='ai.verta.uac.FindWebhookRequest.workspace_id', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDWEBHOOKREQUEST_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=487,
)


_CREATEWEBHOOKREQUEST = _descriptor.Descriptor(
  name='CreateWebhookRequest',
  full_name='ai.verta.uac.CreateWebhookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ai.verta.uac.CreateWebhookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='ai.verta.uac.CreateWebhookRequest.workspace_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='ai.verta.uac.CreateWebhookRequest.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutual_secret', full_name='ai.verta.uac.CreateWebhookRequest.mutual_secret', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_types', full_name='ai.verta.uac.CreateWebhookRequest.event_types', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_events', full_name='ai.verta.uac.CreateWebhookRequest.all_events', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=490,
  serialized_end=630,
)


_UPDATEWEBHOOKREQUEST = _descriptor.Descriptor(
  name='UpdateWebhookRequest',
  full_name='ai.verta.uac.UpdateWebhookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.uac.UpdateWebhookRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_location', full_name='ai.verta.uac.UpdateWebhookRequest.new_location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutual_secret', full_name='ai.verta.uac.UpdateWebhookRequest.mutual_secret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_event_types', full_name='ai.verta.uac.UpdateWebhookRequest.add_event_types', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_event_types', full_name='ai.verta.uac.UpdateWebhookRequest.delete_event_types', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_all_events', full_name='ai.verta.uac.UpdateWebhookRequest.set_all_events', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_all_events', full_name='ai.verta.uac.UpdateWebhookRequest.clear_all_events', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=633,
  serialized_end=815,
)


_DELETEWEBHOOKREQUEST = _descriptor.Descriptor(
  name='DeleteWebhookRequest',
  full_name='ai.verta.uac.DeleteWebhookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='ai.verta.uac.DeleteWebhookRequest.ids', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=817,
  serialized_end=852,
)


_WEBHOOKCALL = _descriptor.Descriptor(
  name='WebhookCall',
  full_name='ai.verta.uac.WebhookCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.uac.WebhookCall.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webhook_id', full_name='ai.verta.uac.WebhookCall.webhook_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_uuid', full_name='ai.verta.uac.WebhookCall.event_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.uac.WebhookCall.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WEBHOOKCALL_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=1036,
)


_FINDWEBHOOKCALLREQUEST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.FindWebhookCallRequest.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='calls', full_name='ai.verta.uac.FindWebhookCallRequest.Response.calls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1170,
  serialized_end=1222,
)

_FINDWEBHOOKCALLREQUEST = _descriptor.Descriptor(
  name='FindWebhookCallRequest',
  full_name='ai.verta.uac.FindWebhookCallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='ai.verta.uac.FindWebhookCallRequest.ids', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webhook_ids', full_name='ai.verta.uac.FindWebhookCallRequest.webhook_ids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_uuids', full_name='ai.verta.uac.FindWebhookCallRequest.event_uuids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.uac.FindWebhookCallRequest.status', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDWEBHOOKCALLREQUEST_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1039,
  serialized_end=1222,
)


_RETRIGGERWEBHOOKCALLREQUEST = _descriptor.Descriptor(
  name='RetriggerWebhookCallRequest',
  full_name='ai.verta.uac.RetriggerWebhookCallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_id', full_name='ai.verta.uac.RetriggerWebhookCallRequest.call_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1224,
  serialized_end=1270,
)

_CREATEEVENTREQUEST.fields_by_name['event_metadata'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FINDWEBHOOKREQUEST_RESPONSE.fields_by_name['webhooks'].message_type = _WEBHOOK
_FINDWEBHOOKREQUEST_RESPONSE.containing_type = _FINDWEBHOOKREQUEST
_WEBHOOKCALL.fields_by_name['status'].enum_type = _WEBHOOKCALL_STATUS
_WEBHOOKCALL_STATUS.containing_type = _WEBHOOKCALL
_FINDWEBHOOKCALLREQUEST_RESPONSE.fields_by_name['calls'].message_type = _WEBHOOKCALL
_FINDWEBHOOKCALLREQUEST_RESPONSE.containing_type = _FINDWEBHOOKCALLREQUEST
_FINDWEBHOOKCALLREQUEST.fields_by_name['status'].enum_type = _WEBHOOKCALL_STATUS
DESCRIPTOR.message_types_by_name['CreateEventRequest'] = _CREATEEVENTREQUEST
DESCRIPTOR.message_types_by_name['Webhook'] = _WEBHOOK
DESCRIPTOR.message_types_by_name['FindWebhookRequest'] = _FINDWEBHOOKREQUEST
DESCRIPTOR.message_types_by_name['CreateWebhookRequest'] = _CREATEWEBHOOKREQUEST
DESCRIPTOR.message_types_by_name['UpdateWebhookRequest'] = _UPDATEWEBHOOKREQUEST
DESCRIPTOR.message_types_by_name['DeleteWebhookRequest'] = _DELETEWEBHOOKREQUEST
DESCRIPTOR.message_types_by_name['WebhookCall'] = _WEBHOOKCALL
DESCRIPTOR.message_types_by_name['FindWebhookCallRequest'] = _FINDWEBHOOKCALLREQUEST
DESCRIPTOR.message_types_by_name['RetriggerWebhookCallRequest'] = _RETRIGGERWEBHOOKCALLREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateEventRequest = _reflection.GeneratedProtocolMessageType('CreateEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEEVENTREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.CreateEventRequest)
  })
_sym_db.RegisterMessage(CreateEventRequest)

Webhook = _reflection.GeneratedProtocolMessageType('Webhook', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOK,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.Webhook)
  })
_sym_db.RegisterMessage(Webhook)

FindWebhookRequest = _reflection.GeneratedProtocolMessageType('FindWebhookRequest', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FINDWEBHOOKREQUEST_RESPONSE,
    '__module__' : 'uac.Event_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.FindWebhookRequest.Response)
    })
  ,
  'DESCRIPTOR' : _FINDWEBHOOKREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.FindWebhookRequest)
  })
_sym_db.RegisterMessage(FindWebhookRequest)
_sym_db.RegisterMessage(FindWebhookRequest.Response)

CreateWebhookRequest = _reflection.GeneratedProtocolMessageType('CreateWebhookRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWEBHOOKREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.CreateWebhookRequest)
  })
_sym_db.RegisterMessage(CreateWebhookRequest)

UpdateWebhookRequest = _reflection.GeneratedProtocolMessageType('UpdateWebhookRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEWEBHOOKREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.UpdateWebhookRequest)
  })
_sym_db.RegisterMessage(UpdateWebhookRequest)

DeleteWebhookRequest = _reflection.GeneratedProtocolMessageType('DeleteWebhookRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEWEBHOOKREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.DeleteWebhookRequest)
  })
_sym_db.RegisterMessage(DeleteWebhookRequest)

WebhookCall = _reflection.GeneratedProtocolMessageType('WebhookCall', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOKCALL,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.WebhookCall)
  })
_sym_db.RegisterMessage(WebhookCall)

FindWebhookCallRequest = _reflection.GeneratedProtocolMessageType('FindWebhookCallRequest', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FINDWEBHOOKCALLREQUEST_RESPONSE,
    '__module__' : 'uac.Event_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.FindWebhookCallRequest.Response)
    })
  ,
  'DESCRIPTOR' : _FINDWEBHOOKCALLREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.FindWebhookCallRequest)
  })
_sym_db.RegisterMessage(FindWebhookCallRequest)
_sym_db.RegisterMessage(FindWebhookCallRequest.Response)

RetriggerWebhookCallRequest = _reflection.GeneratedProtocolMessageType('RetriggerWebhookCallRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIGGERWEBHOOKCALLREQUEST,
  '__module__' : 'uac.Event_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.RetriggerWebhookCallRequest)
  })
_sym_db.RegisterMessage(RetriggerWebhookCallRequest)


DESCRIPTOR._options = None

_EVENTSERVICE = _descriptor.ServiceDescriptor(
  name='EventService',
  full_name='ai.verta.uac.EventService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1273,
  serialized_end=2132,
  methods=[
  _descriptor.MethodDescriptor(
    name='createEvent',
    full_name='ai.verta.uac.EventService.createEvent',
    index=0,
    containing_service=None,
    input_type=_CREATEEVENTREQUEST,
    output_type=uac_dot_UACService__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\032\"\025/v1/event/createEvent:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='createWebhook',
    full_name='ai.verta.uac.EventService.createWebhook',
    index=1,
    containing_service=None,
    input_type=_CREATEWEBHOOKREQUEST,
    output_type=_WEBHOOK,
    serialized_options=b'\202\323\344\223\002\034\"\027/v1/event/createWebhook:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='updateWebhook',
    full_name='ai.verta.uac.EventService.updateWebhook',
    index=2,
    containing_service=None,
    input_type=_UPDATEWEBHOOKREQUEST,
    output_type=_WEBHOOK,
    serialized_options=b'\202\323\344\223\002\034\"\027/v1/event/updateWebhook:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='findWebhook',
    full_name='ai.verta.uac.EventService.findWebhook',
    index=3,
    containing_service=None,
    input_type=_FINDWEBHOOKREQUEST,
    output_type=_FINDWEBHOOKREQUEST_RESPONSE,
    serialized_options=b'\202\323\344\223\002\032\"\025/v1/event/findWebhook:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='deleteWebhook',
    full_name='ai.verta.uac.EventService.deleteWebhook',
    index=4,
    containing_service=None,
    input_type=_DELETEWEBHOOKREQUEST,
    output_type=uac_dot_UACService__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\034*\027/v1/event/deleteWebhook:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='findWebhookCall',
    full_name='ai.verta.uac.EventService.findWebhookCall',
    index=5,
    containing_service=None,
    input_type=_FINDWEBHOOKCALLREQUEST,
    output_type=_FINDWEBHOOKCALLREQUEST_RESPONSE,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/event/findWebhookCall:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='retriggerWebhookCall',
    full_name='ai.verta.uac.EventService.retriggerWebhookCall',
    index=6,
    containing_service=None,
    input_type=_RETRIGGERWEBHOOKCALLREQUEST,
    output_type=_WEBHOOKCALL,
    serialized_options=b'\202\323\344\223\002#\"\036/v1/event/retriggerWebhookCall:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSERVICE)

DESCRIPTOR.services_by_name['EventService'] = _EVENTSERVICE

# @@protoc_insertion_point(module_scope)
