from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBestratingOpvulsoort import KlBestratingOpvulsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGrasbetontegel(Bestrating):
    """Bestrating van grasbetontegels."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.vulling = KeuzelijstField(naam="vulling",
                                       label="vulling",
                                       lijst=KlBestratingOpvulsoort(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel.vulling",
                                       definition="Het gebruikte materiaal als toevoeging in de vrije openingen van de tegels.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het gebruikte materiaal als toevoeging in de vrije openingen van de tegels."""
