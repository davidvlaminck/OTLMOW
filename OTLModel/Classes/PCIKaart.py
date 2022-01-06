# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPCIkaartMerk import KlPCIkaartMerk
from OTLModel.Datatypes.KlPCIkaartModelnaam import KlPCIkaartModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class PCIKaart(AIMNaamObject):
    """Peripheral Component Interconnect of uitbreidingssleuf."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlPCIkaartMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart.merk",
                                    definition="Het merk van de PCI-kaart.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de PCI-kaart."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlPCIkaartModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PCIKaart.modelnaam",
                                         definition="De modelnaam van de PCI-kaart.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de PCI-kaart."""
