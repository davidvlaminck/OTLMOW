# coding=utf-8
from OTLModel.Classes.HardwareToegang import HardwareToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVirtueleServerMerk import KlVirtueleServerMerk
from OTLModel.Datatypes.KlVirtueleServerModelnaam import KlVirtueleServerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VirtueleServer(HardwareToegang):
    """Gedeelte van een fysieke server, dat zich met behulp van software gedraagt als een 'echte' server."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVirtueleServerMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer.merk",
                                    definition="Het merk van de virtuele server.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de virtuele server."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVirtueleServerModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer.modelnaam",
                                         definition="De modelnaam van de virtuele server.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de virtuele server."""
