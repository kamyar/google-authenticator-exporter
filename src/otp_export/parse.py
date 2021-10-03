"""
Code adapted from https://github.com/qistoph/otp_export
Thank you Chris van Marle
"""

import sys
from base64 import b32encode, b64decode
from typing import List, NamedTuple
from urllib.parse import parse_qs, urlparse

from . import OtpMigration_pb2 as otp


class OTP(NamedTuple):
    secret: str
    name: str
    issuer: str
    algorithm: str
    digits: str
    type: str
    counter: str


def parse_data(data) -> List[OTP]:
    url = urlparse(data)

    if url.scheme != b"otpauth-migration":
        print("Only otpauth-migration URLs can be parsed")
        sys.exit(2)

    qs = parse_qs(url.query)

    if b"data" not in qs:
        print("Missing 'data' field in query string")
        sys.exit(3)

    data = b64decode(qs[b"data"][0])  # type: ignore
    payload = otp.MigrationPayload.FromString(data)  # type: ignore

    for params in payload.otp_parameters:
        yield OTP(
            secret=b32encode(params.secret).decode(),
            name=params.name,
            issuer=params.issuer,
            algorithm=otp.Algorithm.Name(params.algorithm),
            digits=otp.DigitCount.Name(params.digits),
            type=otp.OtpType.Name(params.type),
            counter=params.counter,
        )
