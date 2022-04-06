# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.EMAfbakening import EMAfbakening
from OTLMOW.OTLModel.Datatypes.KlIVLichtzuilSoortLamp import KlIVLichtzuilSoortLamp
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVLichtzuil(EMAfbakening, PuntGeometrie):
    """Inwendig verlichte, geel gekleurde conische steun, inclusief het voetstuk waarop het bevestigd is, die gebruikt wordt om obstakels op de weg te signaleren voor het aankomend verkeer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVLichtzuil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        EMAfbakening.__init__(self)
        PuntGeometrie.__init__(self)

        self._soortLamp = OTLAttribuut(field=KlIVLichtzuilSoortLamp,
                                       naam='soortLamp',
                                       label='soort lamp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVLichtzuil.soortLamp',
                                       definition='Welke soort lamp er gebruikt wordt in de inwendig verlichte verkeerszuil.',
                                       owner=self)

    @property
    def soortLamp(self):
        """Welke soort lamp er gebruikt wordt in de inwendig verlichte verkeerszuil."""
        return self._soortLamp.waarde

    @soortLamp.setter
    def soortLamp(self, value):
        self._soortLamp.set_waarde(value, owner=self)
