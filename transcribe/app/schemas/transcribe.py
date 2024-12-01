from ..consts import api
from pydantic import BaseModel, Field


class TranscribeServiceResponse(BaseModel):
    transcribe: str = Field(description=api.DOC_TRANSCRIPTION)


class RequestResponse(BaseModel):
    response: TranscribeServiceResponse | int | None = None
    details: str | None = Field(default=None, description=api.DOC_TRANSCRIBE_RESPONSE)
