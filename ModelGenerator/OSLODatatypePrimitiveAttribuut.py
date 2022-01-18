import dataclasses


@dataclasses.dataclass
class OSLODatatypePrimitiveAttribuut:
    name: str
    label: str
    definition: str
    class_uri: str
    kardinaliteit_min: str
    kardinaliteit_max: str
    objectUri: str
    type: str
    overerving: int
    constraints: str
    readonly: int
    usagenote: str
    deprecated_version: str




