# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.EMAfbakening import EMAfbakening
from OTLMOW.OTLModel.Datatypes.KlLichtzuilSoortLamp import KlLichtzuilSoortLamp
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtzuil(EMAfbakening, PuntGeometrie):
    """Inwendig verlichte, geel gekleurde conische steun, inclusief het voetstuk waarop het bevestigd is, die gebruikt wordt om obstakels op de weg te signaleren voor het aankomend verkeer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtzuil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        EMAfbakening.__init__(self)
        PuntGeometrie.__init__(self)

        self._soortLamp = OTLAttribuut(field=KlLichtzuilSoortLamp,
                                       naam='soortLamp',
                                       label='soort lamp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtzuil.soortLamp',
                                       definition='Welke soort lamp er gebruikt wordt in de lichtzuil.',
                                       owner=self)

    @property
    def soortLamp(self):
        """Welke soort lamp er gebruikt wordt in de lichtzuil."""
        return self._soortLamp.get_waarde()

    @soortLamp.setter
    def soortLamp(self, value):
        self._soortLamp.set_waarde(value, owner=self)
