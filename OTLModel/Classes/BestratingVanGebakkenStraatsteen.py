# coding=utf-8
from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlFormaatGebakkenStraatsteen import KlFormaatGebakkenStraatsteen
from OTLModel.Datatypes.KlStandaardkwaliteitsklasse import KlStandaardkwaliteitsklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGebakkenStraatsteen(Bestrating):
    """Gebakken straatstenen zijn straatstenen, in hoofdzaak vervaardigd uit klei al dan niet gemengd met leem, zand, brandstoffen of andere toeslagstoffen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.formaatVanBestratingselement = KeuzelijstField(naam="formaatVanBestratingselement",
                                                            label="formaat van bestratingselement",
                                                            lijst=KlFormaatGebakkenStraatsteen(),
                                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.formaatVanBestratingselement",
                                                            definition="Bepaling van de afmeting van het bestratingselement.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        """Bepaling van de afmeting van het bestratingselement."""

        self.standaardkwaliteitsklasse = KeuzelijstField(naam="standaardkwaliteitsklasse",
                                                         label="standaardkwaliteitsklasse",
                                                         lijst=KlStandaardkwaliteitsklasse(),
                                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.standaardkwaliteitsklasse",
                                                         definition="De standaardkwaliteitsklasse volgens PTV 910.",
                                                         constraints="",
                                                         usagenote="",
                                                         deprecated_version="")
        """De standaardkwaliteitsklasse volgens PTV 910."""
