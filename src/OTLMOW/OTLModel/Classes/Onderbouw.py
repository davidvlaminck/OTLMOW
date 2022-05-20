# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.LaagDikte import LaagDikte
from OTLMOW.OTLModel.Classes.Laag import Laag
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcKrimpvoeg import DtcKrimpvoeg
from OTLMOW.OTLModel.Datatypes.KlOnderbouwType import KlOnderbouwType
from OTLMOW.OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderbouw(LaagDikte, Laag):
    """Gedeelte van het baanlichaam dat tussen het baanbed en de verharding ligt. Deze omvat onderfundering, fundering en de straatlaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Laag.__init__(self)
        LaagDikte.__init__(self)

        self._isHerstel = OTLAttribuut(field=BooleanField,
                                       naam='isHerstel',
                                       label='is herstel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.isHerstel',
                                       definition='Aanduiding of de onderbouw laag is of wordt hersteld.',
                                       owner=self)

        self._krimpvoegen = OTLAttribuut(field=DtcKrimpvoeg,
                                         naam='krimpvoegen',
                                         label='Krimpvoegen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.krimpvoegen',
                                         definition='Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlOnderbouwType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.type',
                                  definition='Het type van onderbouw.',
                                  owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw.volume',
                                    definition='Het volume van onderbouw in kubieke meter.',
                                    owner=self)

    @property
    def isHerstel(self):
        """Aanduiding of de onderbouw laag is of wordt hersteld."""
        return self._isHerstel.get_waarde()

    @isHerstel.setter
    def isHerstel(self, value):
        self._isHerstel.set_waarde(value, owner=self)

    @property
    def krimpvoegen(self):
        """Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat."""
        return self._krimpvoegen.get_waarde()

    @krimpvoegen.setter
    def krimpvoegen(self, value):
        self._krimpvoegen.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van onderbouw."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def volume(self):
        """Het volume van onderbouw in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
