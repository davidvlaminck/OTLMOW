# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Markering import Markering
from OTLModel.Classes.AOWSType import AOWSType
from OTLModel.Datatypes.KlLEMarkeringCode import KlLEMarkeringCode
from OTLModel.Datatypes.KlLEMarkeringSoort import KlLEMarkeringSoort
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class LijnvormigElementMarkering(Markering, AOWSType, AttributeInfo):
    """Een markering van een lijnvormig element om de zichtbaarheid te verhogen om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AOWSType.__init__(self)
        AttributeInfo.__init__(self)
        Markering.__init__(self)

        self._code = OTLAttribuut(field=KlLEMarkeringCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.code',
                                  definition='De (COPRO/BENOR) code van de lijnvormig element markering.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.lengte',
                                    definition='De lengte van de markering in meter.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.oppervlakte',
                                         definition='De oppervlakte van de markering op het lijnvormig element in vierkante meter.')

        self._soortOmschrijving = OTLAttribuut(field=KlLEMarkeringSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering.soortOmschrijving',
                                               definition='De soort en tevens de omschrijving van de lijnvormige elementen markering.')

    @property
    def code(self):
        """De (COPRO/BENOR) code van de lijnvormig element markering."""
        return self._code.waarde

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de markering in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van de markering op het lijnvormig element in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self):
        """De soort en tevens de omschrijving van de lijnvormige elementen markering."""
        return self._soortOmschrijving.waarde

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)
