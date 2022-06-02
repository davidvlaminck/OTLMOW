import dataclasses


@dataclasses.dataclass
class OSLOTypeLink:
    item_uri: str = ''
    item_tabel: str = ''
    deprecated_version: str = ''
