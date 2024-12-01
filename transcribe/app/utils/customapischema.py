from typing import Any
from fastapi.openapi.utils import get_openapi
from ..config import OpenAPISchemaConfig
from ..consts import api
from fastapi import FastAPI


class CustomizerOpenAPI:

    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def custom_openapi(self) -> str | Any:
        if self.app.openapi_schema:
            return self.app.openapi_schema
        config = OpenAPISchemaConfig()
        openapi_schema = get_openapi(
            title=api.TILE,
            version=config.version,
            description=api.DESCRIPTION,
            routes=self.app.routes,
        )
        self.app.openapi_schema = openapi_schema
        return self.app.openapi_schema
