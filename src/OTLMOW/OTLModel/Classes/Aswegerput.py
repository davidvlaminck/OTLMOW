# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.PutRelatie import PutRelatie
from OTLMOW.OTLModel.Classes.Put import Put
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aswegerput(PutRelatie, Put):
    """Een ondergrondse constructie die de elektronica van een asweger bevat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInM,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput.afmetingGrondvlak',
                                               definition='De lengte en breedte van de vrije ruimte tussen de constructieve elementen van de aswegerput ter hoogte van het maaiveld.',
                                               owner=self)

    @property
    def afmetingGrondvlak(self):
        """De lengte en breedte van de vrije ruimte tussen de constructieve elementen van de aswegerput ter hoogte van het maaiveld."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)
