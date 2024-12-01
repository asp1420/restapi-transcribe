from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any


@dataclass
class Service(ABC):

    filename: str
    data: Any = field(default=None)

    @abstractmethod
    def format_response(self, data: Any) -> Any: ...

    @abstractmethod
    def postprocess(self, output: Any) -> Any: ...

    @abstractmethod
    def predict(self, data: Any, filename: str) -> Any: ...

    def execute(self) -> dict[str, str]:
        prediction = self.predict(data=self.data, filename=self.filename)
        postprocessed = self.postprocess(output=prediction)
        result = self.format_response(data=postprocessed)
        return result
