from ..schemas.transcribe import RequestResponse
from ..consts import messages
from ..worker import process_data
from base64 import b64encode
from fastapi import APIRouter, status, UploadFile, HTTPException


router = APIRouter(
    tags=['Transcribe'],
    responses={
        status.HTTP_404_NOT_FOUND: {'description': 'Go to /docs for more information'}
    }
)


@router.post(
    path='/api/transcribe',
    response_model=RequestResponse,
    response_model_exclude_unset=True,
    status_code=status.HTTP_202_ACCEPTED
)
async def transcribe(audio: UploadFile | None) -> RequestResponse:
    if not audio:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=messages.BAD_PARAMETER_REQUEST)
    data_bytes = await audio.read()
    data_type = audio.content_type
    filename = audio.filename
    bytes64 = b64encode(data_bytes)
    base64_string = bytes64.decode('utf-8')
    result, details = process_data(data_bytes=base64_string, data_type=data_type, filename=filename)
    request_details = {'response': result}
    if details is not None:
        request_details.update({'details': details})
    response = RequestResponse(**request_details)
    return response


