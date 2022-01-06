# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHoogtedetectieMerk import KlHoogtedetectieMerk
from OTLModel.Datatypes.KlHoogtedetectieModelnaam import KlHoogtedetectieModelnaam
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoogtedetectie(AIMNaamObject):
    """Hoogtedetectiesysteem voor het voorkomen van schade aan kunstwerken. Stuurt vaak een dynamisch bord aan. Voor handhaving staat het in relatie met een ANPR-camera."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.detectiehoogte = KwantWrdInMeter()
        """De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen."""
        self.detectiehoogte.naam = "detectiehoogte"
        self.detectiehoogte.label = "detectiehoogte"
        self.detectiehoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.detectiehoogte"
        self.detectiehoogte.definition = "De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen."
        self.detectiehoogte.constraints = ""
        self.detectiehoogte.usagenote = ""
        self.detectiehoogte.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlHoogtedetectieMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.merk",
                                    definition="Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent.",
                                    constraints="",
                                    usagenote="volgens een keuzelijst",
                                    deprecated_version="")
        """Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlHoogtedetectieModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.modelnaam",
                                         definition="De modelnaam van de hoogtedetectie.",
                                         constraints="",
                                         usagenote="Uit een keuzelijst.",
                                         deprecated_version="")
        """De modelnaam van de hoogtedetectie."""
