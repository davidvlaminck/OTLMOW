from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHulppostkastType import KlHulppostkastType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulppostkast(Buitenkast):
    """Een kast waarin verschillende onderdelen verzameld worden voor bijstand in noodgevallen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlHulppostkastType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast.type",
                                    definition="Classificatie van de hulppostkast op basis van de inhoud en vorm volgens gangbare standaarden.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Classificatie van de hulppostkast op basis van de inhoud en vorm volgens gangbare standaarden."""
