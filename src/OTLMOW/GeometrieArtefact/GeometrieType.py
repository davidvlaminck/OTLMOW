import dataclasses


@dataclasses.dataclass
class GeometrieType:
    objectUri: str
    label_nl: str
    geen_geometrie: int
    punt3D: int
    lijn3D: int
    polygoon3D: int
    gewijzigd_sinds: str
