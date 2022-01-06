# coding=utf-8
from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBestrijkingKaliber import KlBestrijkingKaliber
from OTLModel.Datatypes.KlBestrijkingProductfamilie import KlBestrijkingProductfamilie
from OTLModel.Datatypes.KlBestrijkingsoort import KlBestrijkingsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bestrijking(AndereLaag):
    """Een bestrijking bestaat in het sproeien op een verharding of een fundering van één of twee eenvormige 
lagen bindmiddel met een geschikte viscositeit."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.kaliber = KeuzelijstField(naam="kaliber",
                                       label="kaliber",
                                       lijst=KlBestrijkingKaliber(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.kaliber",
                                       definition="De korrelmaat gebruikt bij de bestrijking.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """De korrelmaat gebruikt bij de bestrijking."""

        self.productfamilie = KeuzelijstField(naam="productfamilie",
                                              label="productfamilie",
                                              lijst=KlBestrijkingProductfamilie(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.productfamilie",
                                              definition="Bepaling tot welke productfamilie de bestrijking behoort. ",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Bepaling tot welke productfamilie de bestrijking behoort. """

        self.soort = KeuzelijstField(naam="soort",
                                     label="soort",
                                     lijst=KlBestrijkingsoort(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.soort",
                                     definition="De soort bestrijking.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De soort bestrijking."""
