import dataclasses


@dataclasses.dataclass
class GeometrieType:
    objectUri: str = ''
    label_nl: str = ''
    geen_geometrie: int = -1
    punt3D: int = -1
    lijn3D: int = -1
    polygoon3D: int = -1
    gewijzigd_sinds: str = ''
