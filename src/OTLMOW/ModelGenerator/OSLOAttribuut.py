import dataclasses


@dataclasses.dataclass
class OSLOAttribuut:
    name: str = ''
    label: str = ''
    definition: str = ''
    class_uri: str = ''
    kardinaliteit_min: str = ''
    kardinaliteit_max: str = ''
    objectUri: str = ''
    type: str = ''
    overerving: int = -1
    constraints: str = ''
    readonly: int = -1
    usagenote: str = ''
    deprecated_version: str = ''




