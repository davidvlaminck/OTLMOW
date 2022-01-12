# coding=utf-8
from OTLModel.Classes.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting
from OTLModel.Datatypes.IntegerField import IntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class KantstrookAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting, bestemd om de verharding steun te geven."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalRijenBetonstraatsteen = IntegerField(naam="aantalRijenBetonstraatsteen",
                                                        label="aantal rijen betonstraatsteen",
                                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw.aantalRijenBetonstraatsteen",
                                                        definition="Het aantal rijen betonstraatsteen waaruit de kantstrook is opgebouwd.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Het aantal rijen betonstraatsteen waaruit de kantstrook is opgebouwd."""
