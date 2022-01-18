import dataclasses


@dataclasses.dataclass
class OSLORelatie:
    bron_overerving: str
    doel_overerving: str
    bron_uri: str
    doel_uri: str
    objectUri: str
    richting: str
    usagenote: str
    deprecated_version: str
