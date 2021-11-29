import dataclasses


@dataclasses.dataclass
class OSLOClass:
    label_nl: str
    name: str
    uri: str
    definition_nl: str
    usagenote_nl: str
    abstract: int
    deprecated_version: str
