# coding=utf-8
from OTLModel.Classes.HardwareToegang import HardwareToegang
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHardwareMerk import KlHardwareMerk
from OTLModel.Datatypes.KlHardwareModelnaam import KlHardwareModelnaam
from OTLModel.Datatypes.KlHardwareVormfactor import KlHardwareVormfactor


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hardware(HardwareToegang):
    """Fysieke componenten of onderdelen van een computer."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalUnits = IntegerField(naam="aantalUnits",
                                        label="aantal units",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.aantalUnits",
                                        definition="Het aantal units dat een server in een rack inneemt.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Het aantal units dat een server in een rack inneemt."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlHardwareMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.merk",
                                    definition="Het merk van de hardware.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de hardware."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlHardwareModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.modelnaam",
                                         definition="De modelnaam van de hardware.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de hardware."""

        self.vormfactor = KeuzelijstField(naam="vormfactor",
                                          label="vormfactor",
                                          lijst=KlHardwareVormfactor(),
                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.vormfactor",
                                          definition="Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
