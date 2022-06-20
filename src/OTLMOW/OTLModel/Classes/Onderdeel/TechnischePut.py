# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Behuizing import Behuizing
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TechnischePut(Behuizing, PuntGeometrie):
    """Ondergrondse toezichtsput (manhole). Deze kan telecom installaties (glasvezel,koper) of elektriciteitskabels bevatten. 
Kan uit verschillende materialen bestaan: polycarbonaat,beton,gemetst,of staal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Behuizing.__init__(self)
        PuntGeometrie.__init__(self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut.materiaal',
                                       definition='Het materiaal waaruit de technische put opgebouwd is.',
                                       owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de technische put opgebouwd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
