# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AOWSType import AOWSType
from OTLMOW.OTLModel.Classes.Abstracten.Markering import Markering
from OTLMOW.OTLModel.Datatypes.KlOverlangseMarkeringCode import KlOverlangseMarkeringCode
from OTLMOW.OTLModel.Datatypes.KlOverlangsemarkeringType import KlOverlangsemarkeringType
from OTLMOW.OTLModel.Datatypes.KlPositieSoort import KlPositieSoort
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class OverlangseMarkering(AOWSType, Markering, LijnGeometrie):
    """Een markering overlangs op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AOWSType.__init__(self)
        Markering.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering')

        self._code = OTLAttribuut(field=KlOverlangseMarkeringCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.code',
                                  definition='De (COPRO/BENOR) code van de overlangse markering.',
                                  owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.lengte',
                                    definition='De lengte van de markering in meter.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.oppervlakte',
                                         definition='De oppervlakte van de overlangse markering in vierkante meter.',
                                         owner=self)

        self._positie = OTLAttribuut(field=KlPositieSoort,
                                     naam='positie',
                                     label='positie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.positie',
                                     definition='Bepaling van het wegdeel van de overlangse markering.',
                                     owner=self)

        self._type = OTLAttribuut(field=KlOverlangsemarkeringType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering.type',
                                  definition='Het type van overlangse markering.',
                                  owner=self)

    @property
    def code(self):
        """De (COPRO/BENOR) code van de overlangse markering."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de markering in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van de overlangse markering in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def positie(self):
        """Bepaling van het wegdeel van de overlangse markering."""
        return self._positie.get_waarde()

    @positie.setter
    def positie(self, value):
        self._positie.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van overlangse markering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
