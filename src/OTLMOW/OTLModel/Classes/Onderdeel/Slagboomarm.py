# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlSlagboomarmMerk import KlSlagboomarmMerk
from OTLMOW.OTLModel.Datatypes.KlSlagboomarmModelnaam import KlSlagboomarmModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboomarm(AIMObject, LijnGeometrie):
    """De bewegende arm van een slagboominstallatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._lengteBoom = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='lengteBoom',
                                        label='lengte boom',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.lengteBoom',
                                        definition='De lengte van de slagboomarm uitgedrukt in meter.',
                                        owner=self)

        self._merk = OTLAttribuut(field=KlSlagboomarmMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.merk',
                                  definition='Het merk van de slagboom installatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSlagboomarmModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.modelnaam',
                                       definition='Naam van het model van de slagboominstallatie.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.technischeFiche',
                                             definition='Technische fiche van de slagboominstallatie.',
                                             owner=self)

    @property
    def lengteBoom(self):
        """De lengte van de slagboomarm uitgedrukt in meter."""
        return self._lengteBoom.get_waarde()

    @lengteBoom.setter
    def lengteBoom(self, value):
        self._lengteBoom.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de slagboom installatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Naam van het model van de slagboominstallatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Technische fiche van de slagboominstallatie."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
