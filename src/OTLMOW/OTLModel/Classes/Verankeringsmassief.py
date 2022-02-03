# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Betonfundering import Betonfundering
from OTLMOW.OTLModel.Classes.KlassiekeFundering import KlassiekeFundering
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verankeringsmassief(Betonfundering, KlassiekeFundering):
    """Een fundering waarin ankers zijn aangebracht en die zorgen voor bevestiging en stabilisatie van een object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Betonfundering.__init__(self)
        KlassiekeFundering.__init__(self)

        self._isAfgedektMetBitumen = OTLAttribuut(field=BooleanField,
                                                  naam='isAfgedektMetBitumen',
                                                  label='is afgedekt met bitumen',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief.isAfgedektMetBitumen',
                                                  definition='Geeft aan of de fundering afgedekt is met een waterbestendige laag die regenwater en vuil wegvoert van de fundering.',
                                                  owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringsmassief.volume',
                                    definition='Het volume in kubieke meter van het verankeringsmassief.',
                                    owner=self)

    @property
    def isAfgedektMetBitumen(self):
        """Geeft aan of de fundering afgedekt is met een waterbestendige laag die regenwater en vuil wegvoert van de fundering."""
        return self._isAfgedektMetBitumen.waarde

    @isAfgedektMetBitumen.setter
    def isAfgedektMetBitumen(self, value):
        self._isAfgedektMetBitumen.set_waarde(value, owner=self)

    @property
    def volume(self):
        """Het volume in kubieke meter van het verankeringsmassief."""
        return self._volume.waarde

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
