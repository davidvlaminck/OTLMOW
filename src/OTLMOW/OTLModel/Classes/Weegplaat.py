# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weegplaat(AIMObject):
    """Een plaat waarop te wegen objecten komen en die rust op weegsensoren rust."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegplaat.materiaal',
                                       definition='Het materiaal waaruit de weegplaat is gemaakt volgens een vaste lijst van mogelijke materialen.',
                                       owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de weegplaat is gemaakt volgens een vaste lijst van mogelijke materialen."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
