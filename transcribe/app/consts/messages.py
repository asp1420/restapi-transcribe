from typing import Final


BAD_PARAMETER_REQUEST: Final[str] = "@audio param not sent in request."
INVALID_FILE: Final[str] = "The file is not supported for this REST API."
INVALID_FORMAT_FILE: Final[str] = "The input file doesn't contain a valid image format."
INVALID_TRANSCRIPTION: Final[str] = 'Was not able to transcribe the file.'
INVALID_MODEL_NAME: Final[str] = "Incorrect model name; available models = " \
                                  "tiny.en, tiny, base.en, base, small.en, small, " \
                                  "medium.es, medium, large."
