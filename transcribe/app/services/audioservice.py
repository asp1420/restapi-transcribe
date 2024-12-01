import os
import whisper

from ..utils.logger import Logger
from ..exceptions.apiexceptions import InvalidTranscription, InvalidModelName
from ..config import EnvVariables
from ..consts import paths
from .service import Service
from dataclasses import dataclass
from io import BytesIO


@dataclass
class AudioService(Service):

    def predict(self, data: BytesIO, filename: str) -> dict[str, str] | None:
        config = EnvVariables()
        try:
            model = whisper.load_model(
                name=os.path.join(os.getcwd(), paths.WEIGHTS_PATH, config.model),
                device='cpu'
            )
        except RuntimeError:
            raise InvalidModelName
        with open(filename, 'wb') as pointer:
            pointer.write(data.getbuffer())
        try:
            result = model.transcribe(filename, fp16=False)
            os.remove(filename)
        except Exception as e:
            Logger.error(e)
            raise InvalidTranscription
        return result

    def postprocess(self, output: dict[str, str] | None) -> str | None:
        prosprocessed = None
        if output is not None:
            prosprocessed = output.get('text')
            prosprocessed = prosprocessed.strip()
        return prosprocessed

    def format_response(self, data: str | None) -> dict[str, str] | None:
        response = None
        if data is not None:
            response = {'transcribe': data}
        return response
