import dataclasses


@dataclasses.dataclass
class Inheritance:
    base_name: str = ''
    base_uri: str = ''
    class_uri: str = ''
    class_name: str = ''
    deprecated_version: str = ''
