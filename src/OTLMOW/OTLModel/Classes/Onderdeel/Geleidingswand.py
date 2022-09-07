# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Geleiding import Geleiding
from OTLMOW.OTLModel.Datatypes.KlGeleidingMateriaal import KlGeleidingMateriaal
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleidingswand(Geleiding, LijnGeometrie):
    """Een geleidingswand geleidt kleinere dieren zoals amfibieën naar kleinere ecokokers, ecoduikers en dergelijke."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Geleiding.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand.hoogte',
                                    definition='De hoogte van de geleidingswand in millimeter.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand.lengte',
                                    definition='De lengte van de geleidingswand in meter.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlGeleidingMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand.materiaal',
                                       definition='Het materiaal van de geleiding.',
                                       owner=self)

    @property
    def hoogte(self):
        """De hoogte van de geleidingswand in millimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de geleidingswand in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal van de geleiding."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
