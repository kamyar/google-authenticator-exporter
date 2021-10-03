# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OtpMigration.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="OtpMigration.proto",
    package="",
    syntax="proto2",
    serialized_options=None,
    serialized_pb=b'\n\x12OtpMigration.proto"\x86\x01\n\x10MigrationPayload\x12&\n\x0eotp_parameters\x18\x01 \x03(\x0b\x32\x0e.OtpParameters\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\x12\x13\n\x0b\x62\x61tch_index\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05"\xa2\x01\n\rOtpParameters\x12\x0e\n\x06secret\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06issuer\x18\x03 \x01(\t\x12\x1d\n\talgorithm\x18\x04 \x01(\x0e\x32\n.Algorithm\x12\x1b\n\x06\x64igits\x18\x05 \x01(\x0e\x32\x0b.DigitCount\x12\x16\n\x04type\x18\x06 \x01(\x0e\x32\x08.OtpType\x12\x0f\n\x07\x63ounter\x18\x07 \x01(\x03*V\n\tAlgorithm\x12\x1e\n\x1a\x41LGORITHM_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04SHA1\x10\x01\x12\n\n\x06SHA256\x10\x02\x12\n\n\x06SHA512\x10\x03\x12\x07\n\x03MD5\x10\x04*=\n\nDigitCount\x12\x1b\n\x17\x44IGIT_COUNT_UNSPECIFIED\x10\x00\x12\x07\n\x03SIX\x10\x01\x12\t\n\x05\x45IGHT\x10\x02*7\n\x07OtpType\x12\x18\n\x14OTP_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04HOTP\x10\x01\x12\x08\n\x04TOTP\x10\x02',
)

_ALGORITHM = _descriptor.EnumDescriptor(
    name="Algorithm",
    full_name="Algorithm",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ALGORITHM_TYPE_UNSPECIFIED", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(name="SHA1", index=1, number=1, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name="SHA256", index=2, number=2, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name="SHA512", index=3, number=3, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name="MD5", index=4, number=4, serialized_options=None, type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=324,
    serialized_end=410,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHM)

Algorithm = enum_type_wrapper.EnumTypeWrapper(_ALGORITHM)
_DIGITCOUNT = _descriptor.EnumDescriptor(
    name="DigitCount",
    full_name="DigitCount",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DIGIT_COUNT_UNSPECIFIED", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(name="SIX", index=1, number=1, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name="EIGHT", index=2, number=2, serialized_options=None, type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=412,
    serialized_end=473,
)
_sym_db.RegisterEnumDescriptor(_DIGITCOUNT)

DigitCount = enum_type_wrapper.EnumTypeWrapper(_DIGITCOUNT)
_OTPTYPE = _descriptor.EnumDescriptor(
    name="OtpType",
    full_name="OtpType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="OTP_TYPE_UNSPECIFIED", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(name="HOTP", index=1, number=1, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name="TOTP", index=2, number=2, serialized_options=None, type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=475,
    serialized_end=530,
)
_sym_db.RegisterEnumDescriptor(_OTPTYPE)

OtpType = enum_type_wrapper.EnumTypeWrapper(_OTPTYPE)
ALGORITHM_TYPE_UNSPECIFIED = 0
SHA1 = 1
SHA256 = 2
SHA512 = 3
MD5 = 4
DIGIT_COUNT_UNSPECIFIED = 0
SIX = 1
EIGHT = 2
OTP_TYPE_UNSPECIFIED = 0
HOTP = 1
TOTP = 2


_MIGRATIONPAYLOAD = _descriptor.Descriptor(
    name="MigrationPayload",
    full_name="MigrationPayload",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="otp_parameters",
            full_name="MigrationPayload.otp_parameters",
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
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="MigrationPayload.version",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="batch_size",
            full_name="MigrationPayload.batch_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="batch_index",
            full_name="MigrationPayload.batch_index",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="batch_id",
            full_name="MigrationPayload.batch_id",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=23,
    serialized_end=157,
)


_OTPPARAMETERS = _descriptor.Descriptor(
    name="OtpParameters",
    full_name="OtpParameters",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="secret",
            full_name="OtpParameters.secret",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="OtpParameters.name",
            index=1,
            number=2,
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
        ),
        _descriptor.FieldDescriptor(
            name="issuer",
            full_name="OtpParameters.issuer",
            index=2,
            number=3,
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
        ),
        _descriptor.FieldDescriptor(
            name="algorithm",
            full_name="OtpParameters.algorithm",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="digits",
            full_name="OtpParameters.digits",
            index=4,
            number=5,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="OtpParameters.type",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="counter",
            full_name="OtpParameters.counter",
            index=6,
            number=7,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=160,
    serialized_end=322,
)

_MIGRATIONPAYLOAD.fields_by_name["otp_parameters"].message_type = _OTPPARAMETERS
_OTPPARAMETERS.fields_by_name["algorithm"].enum_type = _ALGORITHM
_OTPPARAMETERS.fields_by_name["digits"].enum_type = _DIGITCOUNT
_OTPPARAMETERS.fields_by_name["type"].enum_type = _OTPTYPE
DESCRIPTOR.message_types_by_name["MigrationPayload"] = _MIGRATIONPAYLOAD
DESCRIPTOR.message_types_by_name["OtpParameters"] = _OTPPARAMETERS
DESCRIPTOR.enum_types_by_name["Algorithm"] = _ALGORITHM
DESCRIPTOR.enum_types_by_name["DigitCount"] = _DIGITCOUNT
DESCRIPTOR.enum_types_by_name["OtpType"] = _OTPTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MigrationPayload = _reflection.GeneratedProtocolMessageType(
    "MigrationPayload",
    (_message.Message,),
    {
        "DESCRIPTOR": _MIGRATIONPAYLOAD,
        "__module__": "OtpMigration_pb2"
        # @@protoc_insertion_point(class_scope:MigrationPayload)
    },
)
_sym_db.RegisterMessage(MigrationPayload)

OtpParameters = _reflection.GeneratedProtocolMessageType(
    "OtpParameters",
    (_message.Message,),
    {
        "DESCRIPTOR": _OTPPARAMETERS,
        "__module__": "OtpMigration_pb2"
        # @@protoc_insertion_point(class_scope:OtpParameters)
    },
)
_sym_db.RegisterMessage(OtpParameters)


# @@protoc_insertion_point(module_scope)
