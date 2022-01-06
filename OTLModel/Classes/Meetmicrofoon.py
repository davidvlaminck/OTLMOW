# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLModel.Datatypes.KlMeetmicrofoonMerk import KlMeetmicrofoonMerk
from OTLModel.Datatypes.KlMeetmicrofoonModelnaam import KlMeetmicrofoonModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetmicrofoon(AIMNaamObject):
    """Een microfoon is een elektromechanisch instrument dat geluid omzet in een elektrisch signaal. 
Een meetmicrofoon registreert de geluidsdruk, is gevoelig voor geluid uit alle richtingen en heeft een vlakke frequentiekarakteristiek. Nauwkeurigheid is hier belangrijker dan geluidskwaliteit. In een tunnel meet de microfoon het geluidsniveau in de tunnel om het volume van een luidspreker aan te kunnen passen om zo verstaanbaar mogelijk te communiceren.
"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlMeetmicrofoonMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.merk",
                                    definition="Het merk van de meetmicrofoon.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de meetmicrofoon."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlMeetmicrofoonModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.modelnaam",
                                         definition="De modelnaam van de meetmicrofoon.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de meetmicrofoon."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de meetmicrofoon."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de meetmicrofoon."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.transportType = KeuzelijstField(naam="transportType",
                                             label="transport type",
                                             lijst=KlAudioTransportType(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.transportType",
                                             definition="Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel."""
