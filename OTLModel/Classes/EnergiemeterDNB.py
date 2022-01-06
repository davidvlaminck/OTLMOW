from OTLModel.Classes.DNBMeter import DNBMeter
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEnergiemeterDNBUurtarief import KlEnergiemeterDNBUurtarief


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterDNB(DNBMeter):
    """Toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor het meten van het energieverbruik van de betreffende installatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isGecombineerdeEnergiemeter = BooleanField(naam="isGecombineerdeEnergiemeter",
                                                        label="is gecombineerde energiemeter",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB.isGecombineerdeEnergiemeter",
                                                        definition="Geeft aan of de meter naast de gewone verbruiksmeting ook reactief vermogen en piek metingen doet.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Geeft aan of de meter naast de gewone verbruiksmeting ook reactief vermogen en piek metingen doet."""

        self.uurtarief = KeuzelijstField(naam="uurtarief",
                                         label="uurtarief",
                                         lijst=KlEnergiemeterDNBUurtarief(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB.uurtarief",
                                         definition="Type uurtarief vb enkelvoudig, dubbelvoudig,...",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Type uurtarief vb enkelvoudig, dubbelvoudig,..."""
