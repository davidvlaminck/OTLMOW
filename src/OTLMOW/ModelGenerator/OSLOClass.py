import dataclasses


@dataclasses.dataclass
class OSLOClass:
    label: str = ''
    name: str = ''
    objectUri: str = ''
    definition: str = ''
    usagenote: str = ''
    abstract: int = -1
    deprecated_version: str = ''
