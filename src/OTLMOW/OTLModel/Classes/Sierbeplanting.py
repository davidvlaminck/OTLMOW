# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLMOW.OTLModel.Datatypes.DtcSierbeplAanleg import DtcSierbeplAanleg
from OTLMOW.OTLModel.Datatypes.KlSierbeplantingType import KlSierbeplantingType
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sierbeplanting(BegroeidVoorkomen, VlakGeometrie):
    """Planten die geen blijvende houtige stengel vormen. Eenjarige,tweejarige of vaste planten,die in de winter tot de grond toe afsterven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BegroeidVoorkomen.__init__(self)
        VlakGeometrie.__init__(self)

        self._aanleg = OTLAttribuut(field=DtcSierbeplAanleg,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting.aanleg',
                                    definition='De manier van aanplanten van de sierbeplanting.',
                                    owner=self)

        self._type = OTLAttribuut(field=KlSierbeplantingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting.type',
                                  kardinaliteit_max='*',
                                  definition='Type van sierbeplanting.',
                                  owner=self)

    @property
    def aanleg(self):
        """De manier van aanplanten van de sierbeplanting."""
        return self._aanleg.waarde

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def type(self):
        """Type van sierbeplanting."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
