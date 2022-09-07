# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLMOW.OTLModel.Datatypes.KlMeetmicrofoonMerk import KlMeetmicrofoonMerk
from OTLMOW.OTLModel.Datatypes.KlMeetmicrofoonModelnaam import KlMeetmicrofoonModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetmicrofoon(AIMNaamObject, PuntGeometrie):
    """Een microfoon is een elektromechanisch instrument dat geluid omzet in een elektrisch signaal. 
Een meetmicrofoon registreert de geluidsdruk, is gevoelig voor geluid uit alle richtingen en heeft een vlakke frequentiekarakteristiek. Nauwkeurigheid is hier belangrijker dan geluidskwaliteit. In een tunnel meet de microfoon het geluidsniveau in de tunnel om het volume van een luidspreker aan te kunnen passen om zo verstaanbaar mogelijk te communiceren.
"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Audioversterker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer')

        self._merk = OTLAttribuut(field=KlMeetmicrofoonMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.merk',
                                  definition='Het merk van de meetmicrofoon.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlMeetmicrofoonModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.modelnaam',
                                       definition='De modelnaam van de meetmicrofoon.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.technischeFiche',
                                             definition='De technische fiche van de meetmicrofoon.',
                                             owner=self)

        self._transportType = OTLAttribuut(field=KlAudioTransportType,
                                           naam='transportType',
                                           label='transport type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon.transportType',
                                           definition='Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel.',
                                           owner=self)

    @property
    def merk(self):
        """Het merk van de meetmicrofoon."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de meetmicrofoon."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de meetmicrofoon."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def transportType(self):
        """Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel."""
        return self._transportType.get_waarde()

    @transportType.setter
    def transportType(self, value):
        self._transportType.set_waarde(value, owner=self)
