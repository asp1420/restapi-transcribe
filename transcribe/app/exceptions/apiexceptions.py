from ..consts import messages


class InvalidFile(Exception):
    def __init__(self) -> None: ...

    def __str__(self) -> str:
        return messages.INVALID_FILE


class InvalidTranscription(Exception):
    def __init__(self) -> None: ...

    def __str__(self) -> str:
        return messages.INVALID_TRANSCRIPTION


class InvalidModelName(Exception):
    def __init__(self) -> None: ...

    def __str__(self) -> str:
        return messages.INVALID_MODEL_NAME
