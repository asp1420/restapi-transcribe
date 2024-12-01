from .utils.logger import Logger
from .exceptions.apiexceptions import (
    InvalidFile,
    InvalidTranscription,
    InvalidModelName
)
from .utils.audio import extract
from .schemas.transcribe import RequestResponse
from .services.audioservice import AudioService


def process_data(data_bytes: str, data_type: str, filename: str) -> RequestResponse:
    details = None
    response = -1
    try:
        data = extract(data_bytes=data_bytes, data_type=data_type)
        service = AudioService(data=data, filename=filename)
        response = service.execute()
    except (InvalidFile, InvalidTranscription, InvalidModelName) as exc:
        details = str(exc)
        Logger.error(details)
    except Exception as exc:
        details = str(exc)
        Logger.error(details)
    return response, details
