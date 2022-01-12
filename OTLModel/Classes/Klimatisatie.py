# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKlimatisatieMerk import KlKlimatisatieMerk
from OTLModel.Datatypes.KlKlimatisatieModelnaam import KlKlimatisatieModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Klimatisatie(AIMNaamObject):
    """Component waarmee de temperatuur en klimaat geregeld wordt van het objecttype waaraan het bevestigd is zoals een behuizing of ruimte."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlKlimatisatieMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie.merk",
                                    definition="De merknaam van de klimatisatie volgens de fabrikant.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam van de klimatisatie volgens de fabrikant."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlKlimatisatieModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie.modelnaam",
                                         definition="Naam waarmee de fabrikant het model van de klimatisatie identificeert.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam waarmee de fabrikant het model van de klimatisatie identificeert."""
