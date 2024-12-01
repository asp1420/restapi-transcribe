import os

from dataclasses import dataclass, field

CONF_TYPE = str | None
CONF_VARIABLES = {
    'APP_VERSION': os.environ.get('APP_VERSION', '0.1'),
    'MODEL_NAME': os.environ.get('MODEL_NAME', 'small.pt')
}


@dataclass
class Configuration:
    config: dict[str, str | None] = field(default_factory=lambda: CONF_VARIABLES)

    def get_property(self, property_name: str) -> CONF_TYPE:
        if property_name not in self.config.keys():
            return None
        return self.config[property_name]


@dataclass
class EnvVariables(Configuration):
    
    @property
    def model(self) -> CONF_TYPE:
        return self.get_property('MODEL_NAME')


class OpenAPISchemaConfig(Configuration):

    @property
    def version(self) -> CONF_TYPE:
        return self.get_property('APP_VERSION')
