# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AOWSType import AOWSType
from OTLMOW.OTLModel.Classes.Abstracten.Markering import Markering
from OTLMOW.OTLModel.Datatypes.KlGekleurdWVCode import KlGekleurdWVCode
from OTLMOW.OTLModel.Datatypes.KlGekleurdWVSoort import KlGekleurdWVSoort
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GekleurdWegvlakMarkering(AOWSType, Markering, VlakGeometrie):
    """Een markering van een wegdeel aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AOWSType.__init__(self)
        Markering.__init__(self)
        VlakGeometrie.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.breedte',
                                     definition='De breedte van de markering in meter.',
                                     owner=self)

        self._code = OTLAttribuut(field=KlGekleurdWVCode,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.code',
                                  definition='De  (COPRO/BENOR) code van de gekleurde wegvlak markering.',
                                  owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.lengte',
                                    definition='De lengte van de markering in meter.',
                                    owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.oppervlakte',
                                         definition='De oppervlakte van het gekleurd wegdeel in vierkante meter.',
                                         owner=self)

        self._soortOmschrijving = OTLAttribuut(field=KlGekleurdWVSoort,
                                               naam='soortOmschrijving',
                                               label='soort omschrijving',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering.soortOmschrijving',
                                               definition='De soort en tevens omschrijving van de figuratie markering.',
                                               owner=self)

    @property
    def breedte(self):
        """De breedte van de markering in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def code(self):
        """De  (COPRO/BENOR) code van de gekleurde wegvlak markering."""
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
        """De oppervlakte van het gekleurd wegdeel in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def soortOmschrijving(self):
        """De soort en tevens omschrijving van de figuratie markering."""
        return self._soortOmschrijving.get_waarde()

    @soortOmschrijving.setter
    def soortOmschrijving(self, value):
        self._soortOmschrijving.set_waarde(value, owner=self)
