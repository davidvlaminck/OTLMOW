import dataclasses


@dataclasses.dataclass
class OSLORelatie:
    bron_overerving: str
    doel_overerving: str
    bron_uri: str
    doel_uri: str
    uri: str
    richting: str
    usagenote_nl: str
    deprecated_version: str
