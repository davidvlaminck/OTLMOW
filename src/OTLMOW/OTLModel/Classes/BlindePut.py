# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Put import Put
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BlindePut(Put, AIMObject, VlakGeometrie):
    """Een put waar de riolering op aangesloten is maar die niet meer zichtbaar is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Put.__init__(self)
        VlakGeometrie.__init__(self)

        self._materiaal = OTLAttribuut(field=KlPutMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut.materiaal',
                                       definition='Het materiaal waaruit de blinde put is vervaardigd.',
                                       owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de blinde put is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
