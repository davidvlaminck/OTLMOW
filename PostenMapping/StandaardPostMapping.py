import dataclasses


@dataclasses.dataclass
class StandaardPostMapping:
    typeURI: str
    attribuutURI: str
    dotnotatie: str
    defaultWaarde: str
    range: str
    usagenote: str
    isMeetstaatAttr: int
    isAltijdInTeVullen: int
    isBasisMapping: int
    mappingStatus: str
    mappingOpmerking: str
    standaardpostnummer: str