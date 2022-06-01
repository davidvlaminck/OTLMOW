# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlLokaalTerreinType import KlLokaalTerreinType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetstation(AIMNaamObject):
    """De plaats waar verschillende sensoren samen 1 meetstation vormen. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beoordelingLokaleTerrein = OTLAttribuut(field=KlLokaalTerreinType,
                                                      naam='beoordelingLokaleTerrein',
                                                      label='Beoordeling lokale terrein',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.beoordelingLokaleTerrein',
                                                      kardinaliteit_max='*',
                                                      definition='Het soort terrein waarin het meetstation staat met betrekking tot het reliëf en de vegetatie.',
                                                      owner=self)

        self._fotoNoord = OTLAttribuut(field=DtcDocument,
                                       naam='fotoNoord',
                                       label='foto noord',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.fotoNoord',
                                       definition='Een foto van de omgeving van het meetstation getrokken in de richting van het noorden.',
                                       owner=self)

        self._fotoOost = OTLAttribuut(field=DtcDocument,
                                      naam='fotoOost',
                                      label='Foto oost',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.fotoOost',
                                      definition='Een foto van de omgeving van het meetstation getrokken in de richting van het oosten.',
                                      owner=self)

        self._fotoWest = OTLAttribuut(field=DtcDocument,
                                      naam='fotoWest',
                                      label='Foto west',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.fotoWest',
                                      definition='Een foto van de omgeving van het meetstation getrokken in de richting van het westen.',
                                      owner=self)

        self._fotoZuid = OTLAttribuut(field=DtcDocument,
                                      naam='fotoZuid',
                                      label='Foto zuid',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.fotoZuid',
                                      definition='Een foto van de omgeving van het meetstation getrokken in de richting van het zuiden.',
                                      owner=self)

        self._keuringsrapport = OTLAttribuut(field=DtcDocument,
                                             naam='keuringsrapport',
                                             label='keuringsrapport',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.keuringsrapport',
                                             definition='Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation.',
                                             owner=self)

        self._masterOfBridgeSensor = OTLAttribuut(field=BooleanField,
                                                  naam='masterOfBridgeSensor',
                                                  label='Master of bridge sensor',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.masterOfBridgeSensor',
                                                  definition='Geeft aan of het meetstation ingeplant is ter hoogte van een brug.',
                                                  owner=self)

        self._nabijheidVanHindernissen = OTLAttribuut(field=KwantWrdInMeter,
                                                      naam='nabijheidVanHindernissen',
                                                      label='Nabijheid van hindernissen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.nabijheidVanHindernissen',
                                                      kardinaliteit_max='*',
                                                      definition='De afstand tot een hindernis in de nabijheid.',
                                                      owner=self)

        self._nabijheidVanWaterlopen = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='nabijheidVanWaterlopen',
                                                    label='Nabijheid van waterlopen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.nabijheidVanWaterlopen',
                                                    kardinaliteit_max='*',
                                                    definition='De afstand tot een waterloop in de nabijheid.',
                                                    owner=self)

        self._onderhoudsrapport = OTLAttribuut(field=DtcDocument,
                                               naam='onderhoudsrapport',
                                               label='onderhoudsrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.onderhoudsrapport',
                                               definition='Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation.',
                                               owner=self)

        self._overzichtsfoto = OTLAttribuut(field=DtcDocument,
                                            naam='overzichtsfoto',
                                            label='Overzichtsfoto',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation.overzichtsfoto',
                                            definition='Een foto van het gehele meetstation.',
                                            owner=self)

    @property
    def beoordelingLokaleTerrein(self):
        """Het soort terrein waarin het meetstation staat met betrekking tot het reliëf en de vegetatie."""
        return self._beoordelingLokaleTerrein.get_waarde()

    @beoordelingLokaleTerrein.setter
    def beoordelingLokaleTerrein(self, value):
        self._beoordelingLokaleTerrein.set_waarde(value, owner=self)

    @property
    def fotoNoord(self):
        """Een foto van de omgeving van het meetstation getrokken in de richting van het noorden."""
        return self._fotoNoord.get_waarde()

    @fotoNoord.setter
    def fotoNoord(self, value):
        self._fotoNoord.set_waarde(value, owner=self)

    @property
    def fotoOost(self):
        """Een foto van de omgeving van het meetstation getrokken in de richting van het oosten."""
        return self._fotoOost.get_waarde()

    @fotoOost.setter
    def fotoOost(self, value):
        self._fotoOost.set_waarde(value, owner=self)

    @property
    def fotoWest(self):
        """Een foto van de omgeving van het meetstation getrokken in de richting van het westen."""
        return self._fotoWest.get_waarde()

    @fotoWest.setter
    def fotoWest(self, value):
        self._fotoWest.set_waarde(value, owner=self)

    @property
    def fotoZuid(self):
        """Een foto van de omgeving van het meetstation getrokken in de richting van het zuiden."""
        return self._fotoZuid.get_waarde()

    @fotoZuid.setter
    def fotoZuid(self, value):
        self._fotoZuid.set_waarde(value, owner=self)

    @property
    def keuringsrapport(self):
        """Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation."""
        return self._keuringsrapport.get_waarde()

    @keuringsrapport.setter
    def keuringsrapport(self, value):
        self._keuringsrapport.set_waarde(value, owner=self)

    @property
    def masterOfBridgeSensor(self):
        """Geeft aan of het meetstation ingeplant is ter hoogte van een brug."""
        return self._masterOfBridgeSensor.get_waarde()

    @masterOfBridgeSensor.setter
    def masterOfBridgeSensor(self, value):
        self._masterOfBridgeSensor.set_waarde(value, owner=self)

    @property
    def nabijheidVanHindernissen(self):
        """De afstand tot een hindernis in de nabijheid."""
        return self._nabijheidVanHindernissen.get_waarde()

    @nabijheidVanHindernissen.setter
    def nabijheidVanHindernissen(self, value):
        self._nabijheidVanHindernissen.set_waarde(value, owner=self)

    @property
    def nabijheidVanWaterlopen(self):
        """De afstand tot een waterloop in de nabijheid."""
        return self._nabijheidVanWaterlopen.get_waarde()

    @nabijheidVanWaterlopen.setter
    def nabijheidVanWaterlopen(self, value):
        self._nabijheidVanWaterlopen.set_waarde(value, owner=self)

    @property
    def onderhoudsrapport(self):
        """Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation."""
        return self._onderhoudsrapport.get_waarde()

    @onderhoudsrapport.setter
    def onderhoudsrapport(self, value):
        self._onderhoudsrapport.set_waarde(value, owner=self)

    @property
    def overzichtsfoto(self):
        """Een foto van het gehele meetstation."""
        return self._overzichtsfoto.get_waarde()

    @overzichtsfoto.setter
    def overzichtsfoto(self, value):
        self._overzichtsfoto.set_waarde(value, owner=self)
