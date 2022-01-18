# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Markering import Markering
from OTLModel.Classes.AOWSType import AOWSType
from OTLModel.Datatypes.KlOverlangseMarkeringCode import KlOverlangseMarkeringCode
from OTLModel.Datatypes.KlOverlangsemarkeringType import KlOverlangsemarkeringType
from OTLModel.Datatypes.KlPositieSoort import KlPositieSoort
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class OverlangseMarkering(Markering, AOWSType, AttributeInfo):
    """Een markering overlangs op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AOWSType.__init__(self)
        AttributeInfo.__init__(self)
        Markering.__init__(self)

        self._code = OTLAttribuut(field=KlOverlangseMarkeringCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.code',
                                  definition='De (COPRO/BENOR) code van de overlangse markering.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.lengte',
                                    definition='De lengte van de markering in meter.')

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.oppervlakte',
                                         definition='De oppervlakte van de overlangse markering in vierkante meter.')

        self._positie = OTLAttribuut(field=KlPositieSoort,
                                     naam='positie',
                                     label='positie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.positie',
                                     definition='Bepaling van het wegdeel van de overlangse markering.')

        self._type = OTLAttribuut(field=KlOverlangsemarkeringType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.type',
                                  definition='Het type van overlangse markering.')

    @property
    def code(self):
        """De (COPRO/BENOR) code van de overlangse markering."""
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
        """De oppervlakte van de overlangse markering in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def positie(self):
        """Bepaling van het wegdeel van de overlangse markering."""
        return self._positie.waarde

    @positie.setter
    def positie(self, value):
        self._positie.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van overlangse markering."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
