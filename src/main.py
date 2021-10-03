import os
import time
from typing import List

import cv2
import pyotp
import qrcode
from pyzbar.pyzbar import Decoded, decode

from .otp_export.parse import OTP, parse_data

QRS_EXPORT_DIRECTORY = "qrs"

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)


def get_one_qr_code() -> List[Decoded]:
    rval = True
    while rval:
        rval, frame = vc.read()
        cv2.imshow("preview", frame)
        # TODO: only look for qr codes
        qr_code_data = decode(frame)
        if qr_code_data:
            return qr_code_data
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
        time.sleep(0.1)
    return []


def export():
    qr1 = get_one_qr_code()

    otps: List[OTP] = parse_data(qr1[0].data)
    for otp in otps:
        data = pyotp.totp.TOTP(otp.secret).provisioning_uri(name=otp.name, issuer_name=otp.issuer)
        print(data)
        img = qrcode.make(data)
        if not os.path.exists(QRS_EXPORT_DIRECTORY):
            os.mkdir(QRS_EXPORT_DIRECTORY)
        img.save(f"{QRS_EXPORT_DIRECTORY}/{otp.name}-{otp.issuer}.png")
