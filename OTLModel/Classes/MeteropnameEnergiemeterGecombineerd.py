from OTLModel.Classes.MeteropnameEnergiemeter import MeteropnameEnergiemeter
from OTLModel.Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt
from OTLModel.Datatypes.KwantWrdInkVARh import KwantWrdInkVARh


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeteropnameEnergiemeterGecombineerd(MeteropnameEnergiemeter):
    """Resultaten van een meteropname van een gecombineerde energiemeter."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.meterstandPiek = KwantWrdInKiloWatt()
        """De stand van de energiemeter waarmee het piekvermogen gemeten wordt."""
        self.meterstandPiek.naam = "meterstandPiek"
        self.meterstandPiek.label = "meterstand piek"
        self.meterstandPiek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandPiek"
        self.meterstandPiek.definition = "De stand van de energiemeter waarmee het piekvermogen gemeten wordt."
        self.meterstandPiek.constraints = ""
        self.meterstandPiek.usagenote = ""
        self.meterstandPiek.deprecated_version = ""

        self.meterstandReactiefVermogenDag = KwantWrdInkVARh()
        """De stand van de dag-energiemeter waarmee het reactief vermogen gemeten wordt."""
        self.meterstandReactiefVermogenDag.naam = "meterstandReactiefVermogenDag"
        self.meterstandReactiefVermogenDag.label = "dag-meterstand reactief vermogen"
        self.meterstandReactiefVermogenDag.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandReactiefVermogenDag"
        self.meterstandReactiefVermogenDag.definition = "De stand van de dag-energiemeter waarmee het reactief vermogen gemeten wordt."
        self.meterstandReactiefVermogenDag.constraints = ""
        self.meterstandReactiefVermogenDag.usagenote = ""
        self.meterstandReactiefVermogenDag.deprecated_version = ""

        self.meterstandReactiefVermogenNacht = KwantWrdInkVARh()
        """De stand van de nacht-energiemeter waarmee het reactief vermogen gemeten wordt."""
        self.meterstandReactiefVermogenNacht.naam = "meterstandReactiefVermogenNacht"
        self.meterstandReactiefVermogenNacht.label = "nacht-meterstand reactief vermogen"
        self.meterstandReactiefVermogenNacht.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeterGecombineerd.meterstandReactiefVermogenNacht"
        self.meterstandReactiefVermogenNacht.definition = "De stand van de nacht-energiemeter waarmee het reactief vermogen gemeten wordt."
        self.meterstandReactiefVermogenNacht.constraints = ""
        self.meterstandReactiefVermogenNacht.usagenote = ""
        self.meterstandReactiefVermogenNacht.deprecated_version = ""
