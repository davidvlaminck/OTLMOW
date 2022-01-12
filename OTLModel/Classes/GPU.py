# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGPUMerk import KlGPUMerk
from OTLModel.Datatypes.KlGPUModelnaam import KlGPUModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class GPU(AIMNaamObject):
    """Grafische verwerkingseenheid."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GPU"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlGPUMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GPU.merk",
                                    definition="Het merk van de GPU.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de GPU."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlGPUModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GPU.modelnaam",
                                         definition="De modelnaam van de GPU.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de GPU."""
