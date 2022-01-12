import dataclasses


@dataclasses.dataclass
class OSLOEnumeration:
    name: str
    objectUri: str
    usagenote_nl: str
    definition_nl: str
    label_nl: str
    codelist: str
    deprecated_version: str




