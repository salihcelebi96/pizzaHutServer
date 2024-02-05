# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/context.proto
"""Generated protocol buffer code."""
from cloudsdk.google.protobuf import descriptor as _descriptor
from cloudsdk.google.protobuf import message as _message
from cloudsdk.google.protobuf import reflection as _reflection
from cloudsdk.google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/context.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\014ContextProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x18google/api/context.proto\x12\ngoogle.api"1\n\x07\x43ontext\x12&\n\x05rules\x18\x01 \x03(\x0b\x32\x17.google.api.ContextRule"D\n\x0b\x43ontextRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x11\n\trequested\x18\x02 \x03(\t\x12\x10\n\x08provided\x18\x03 \x03(\tBn\n\x0e\x63om.google.apiB\x0c\x43ontextProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3',
)


_CONTEXT = _descriptor.Descriptor(
    name="Context",
    full_name="google.api.Context",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="rules",
            full_name="google.api.Context.rules",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=40,
    serialized_end=89,
)


_CONTEXTRULE = _descriptor.Descriptor(
    name="ContextRule",
    full_name="google.api.ContextRule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="selector",
            full_name="google.api.ContextRule.selector",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="requested",
            full_name="google.api.ContextRule.requested",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="provided",
            full_name="google.api.ContextRule.provided",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=91,
    serialized_end=159,
)

_CONTEXT.fields_by_name["rules"].message_type = _CONTEXTRULE
DESCRIPTOR.message_types_by_name["Context"] = _CONTEXT
DESCRIPTOR.message_types_by_name["ContextRule"] = _CONTEXTRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType(
    "Context",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTEXT,
        "__module__": "google.api.context_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Context)
    },
)
_sym_db.RegisterMessage(Context)

ContextRule = _reflection.GeneratedProtocolMessageType(
    "ContextRule",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTEXTRULE,
        "__module__": "google.api.context_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ContextRule)
    },
)
_sym_db.RegisterMessage(ContextRule)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
