# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlLantaarnLamptype import KlLantaarnLamptype


# Generated with OTLClassCreator. To modify: extend, do not edit
class BiFlash(AIMNaamObject):
    """Een seinlantaarn type bi-flash is een balkvormig lichaam waarin twee amberkleurige lampen zitten die beurtelings kunnen knipperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BiFlash'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._lamptype = OTLAttribuut(field=KlLantaarnLamptype,
                                      naam='lamptype',
                                      label='lamptype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BiFlash.lamptype',
                                      definition='Het type lamp van de bi-flash.',
                                      owner=self)

    @property
    def lamptype(self):
        """Het type lamp van de bi-flash."""
        return self._lamptype.get_waarde()

    @lamptype.setter
    def lamptype(self, value):
        self._lamptype.set_waarde(value, owner=self)
