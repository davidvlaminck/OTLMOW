# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.LinkendElement import LinkendElement
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wervel(LinkendElement, VlakGeometrie):
    """Een wervel is een debietsbeperkend element dat zich tussen 2 kamers of tussen een kamer en een leiding bevindt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wervel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        LinkendElement.__init__(self)
        VlakGeometrie.__init__(self)

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wervel.peil',
                                  definition='Dit is het niveau in meter-TAW van de inlaat van het wervelventiel.',
                                  owner=self)

    @property
    def peil(self):
        """Dit is het niveau in meter-TAW van de inlaat van het wervelventiel."""
        return self._peil.waarde

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)
