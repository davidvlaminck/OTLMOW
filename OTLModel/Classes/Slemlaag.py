from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLModel.Datatypes.KlSlemProductfamilie import KlSlemProductfamilie
from OTLModel.Datatypes.KlSlemlaagsoort import KlSlemlaagsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slemlaag(AndereLaag):
    """Een slemlaag (slem) is een oppervlaktebehandeling die bestaat uit een mengsel dat ter plaatse bereid en verwerkt wordt.
"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlKleurSupp(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.kleur",
                                     definition="De kleur van de slemlaag.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De kleur van de slemlaag."""

        self.productfamilie = KeuzelijstField(naam="productfamilie",
                                              label="productfamilie",
                                              lijst=KlSlemProductfamilie(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.productfamilie",
                                              definition="Bepaling tot welke productfamilie de slemlaag behoort. ",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Bepaling tot welke productfamilie de slemlaag behoort. """

        self.soort = KeuzelijstField(naam="soort",
                                     label="soort",
                                     lijst=KlSlemlaagsoort(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.soort",
                                     definition="De soort slemlaag.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De soort slemlaag."""
