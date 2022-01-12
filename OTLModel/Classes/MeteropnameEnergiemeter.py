# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KwantWrdInkWh import KwantWrdInkWh


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeteropnameEnergiemeter(AIMNaamObject):
    """Resultaten van een meteropname van een energiemeter."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.datumMeterstand = DateField(naam="datumMeterstand",
                                         label="datum meterstand dag",
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter.datumMeterstand",
                                         definition="De datum van de laatste meteropname van de energiemeter.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De datum van de laatste meteropname van de energiemeter."""

        self.meterstandDag = KwantWrdInkWh()
        """De meterstand bij de laatste meteropname van de dag-energiemeter."""
        self.meterstandDag.naam = "meterstandDag"
        self.meterstandDag.label = "meterstand dag"
        self.meterstandDag.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter.meterstandDag"
        self.meterstandDag.definition = "De meterstand bij de laatste meteropname van de dag-energiemeter."
        self.meterstandDag.constraints = ""
        self.meterstandDag.usagenote = ""
        self.meterstandDag.deprecated_version = ""

        self.meterstandNacht = KwantWrdInkWh()
        """De meterstand bij de laatste meteropname van de nacht-energiemeter."""
        self.meterstandNacht.naam = "meterstandNacht"
        self.meterstandNacht.label = "meterstand nacht"
        self.meterstandNacht.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter.meterstandNacht"
        self.meterstandNacht.definition = "De meterstand bij de laatste meteropname van de nacht-energiemeter."
        self.meterstandNacht.constraints = ""
        self.meterstandNacht.usagenote = ""
        self.meterstandNacht.deprecated_version = ""
