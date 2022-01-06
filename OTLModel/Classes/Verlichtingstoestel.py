# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerlichtingstoestelMerk import KlVerlichtingstoestelMerk
from OTLModel.Datatypes.KlVerlichtingstoestelModelnaam import KlVerlichtingstoestelModelnaam
from OTLModel.Datatypes.KlVerlichtingstoestelVerlichtGebied import KlVerlichtingstoestelVerlichtGebied
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verlichtingstoestel(AIMNaamObject):
    """Abstracte voor het geheel van de lichtbron en de behuizing die werden samengesteld met als doel:
* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.heeftAansluitkastGeintegreerd = BooleanField(naam="heeftAansluitkastGeintegreerd",
                                                          label="heeft aansluitkast geintegreerd",
                                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.heeftAansluitkastGeintegreerd",
                                                          definition="Is de aansluitkast geïntegreerd?",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        """Is de aansluitkast geïntegreerd?"""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVerlichtingstoestelMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.merk",
                                    definition="Het merk van het verlichtingstoestel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van het verlichtingstoestel."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVerlichtingstoestelModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.modelnaam",
                                         definition="De modelnaam van het verlichtingstoestel.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van het verlichtingstoestel."""

        self.stroomkringnummer = StringField(naam="stroomkringnummer",
                                             label="stroomkringnummer",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.stroomkringnummer",
                                             definition="Nummer van de stroomkring waarop het verlichtingstoestel is aangesloten.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Nummer van de stroomkring waarop het verlichtingstoestel is aangesloten."""

        self.systeemvermogen = KwantWrdInWatt()
        """Systeemvermogen (Watt) van het verlichtingstoestel."""
        self.systeemvermogen.naam = "systeemvermogen"
        self.systeemvermogen.label = "systeemvermogen"
        self.systeemvermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.systeemvermogen"
        self.systeemvermogen.definition = "Systeemvermogen (Watt) van het verlichtingstoestel."
        self.systeemvermogen.constraints = ""
        self.systeemvermogen.usagenote = ""
        self.systeemvermogen.deprecated_version = ""

        self.verlichtGebied = KeuzelijstField(naam="verlichtGebied",
                                              label="verlicht gebied",
                                              lijst=KlVerlichtingstoestelVerlichtGebied(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.verlichtGebied",
                                              definition="Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel."""
