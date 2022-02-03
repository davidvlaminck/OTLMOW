# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLMOW.OTLModel.Datatypes.KlEleAansluitvermogen import KlEleAansluitvermogen
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoedingDerdenLaagspanning(Voedingspunt, PuntGeometrie):
    """Aansluiting op het laagspanningsnet van een andere partij, niet rechtstreeks bij de distributienetbeheerder en niet afgetakt van de asset beheerder."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedingDerdenLaagspanning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Voedingspunt.__init__(self)
        PuntGeometrie.__init__(self)

        self._aansluitvermogen = OTLAttribuut(field=KlEleAansluitvermogen,
                                              naam='aansluitvermogen',
                                              label='aansluitvermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedingDerdenLaagspanning.aansluitvermogen',
                                              definition='Vermogen van de aansluiting.',
                                              owner=self)

    @property
    def aansluitvermogen(self):
        """Vermogen van de aansluiting."""
        return self._aansluitvermogen.waarde

    @aansluitvermogen.setter
    def aansluitvermogen(self, value):
        self._aansluitvermogen.set_waarde(value, owner=self)
