# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlFietstelsysteemMerk import KlFietstelsysteemMerk
from OTLModel.Datatypes.KlFietstelsysteemModelnaam import KlFietstelsysteemModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fietstelsysteem(AIMNaamObject):
    """Toestel bij de fietstelinstallatie dat gegevens van detectielussen over passerende fietsers verzamelt en verwerkt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingen = DtcAfmetingBxlxhInMm()
        """De afmetingen van het fietstelsysteem."""
        self.afmetingen.naam = "afmetingen"
        self.afmetingen.label = "afmetingen"
        self.afmetingen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.afmetingen"
        self.afmetingen.definition = "De afmetingen van het fietstelsysteem."
        self.afmetingen.constraints = ""
        self.afmetingen.usagenote = ""
        self.afmetingen.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlFietstelsysteemMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.merk",
                                    definition="Merknaam van het fietstelsysteem.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merknaam van het fietstelsysteem."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlFietstelsysteemModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.modelnaam",
                                         definition="Naam van het model van het fietstelsysteem volgens de fabrikant.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam van het model van het fietstelsysteem volgens de fabrikant."""

        self.technischeFiche = DtcDocument()
        """Document met de technische specificaties van het fietstelsysteem."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.technischeFiche"
        self.technischeFiche.definition = "Document met de technische specificaties van het fietstelsysteem."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
