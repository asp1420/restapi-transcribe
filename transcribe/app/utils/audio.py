import re

from ..exceptions.apiexceptions import InvalidFile
from io import BytesIO
from base64 import b64decode


def extract(data_bytes: str, data_type: str) -> BytesIO | None:
    data = None
    rcomp = re.compile('audio|video')
    if rcomp.findall(data_type):
        encoded = data_bytes.encode('utf-8')
        data_bytes = b64decode(encoded)
        bytesio = BytesIO(data_bytes)
        data = bytesio
    else:
        raise InvalidFile
    return data
