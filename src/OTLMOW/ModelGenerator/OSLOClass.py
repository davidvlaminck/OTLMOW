import dataclasses


@dataclasses.dataclass
class OSLOClass:
    label: str
    name: str
    objectUri: str
    definition: str
    usagenote: str
    abstract: int
    deprecated_version: str
