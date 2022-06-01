# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Randprofiel(ConstructiefObject):
    """Profiel ter afwerking en versterking van de rand. Deze kan uitgevoerd worden in verschillende materialen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Randprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._lopendeMeter = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='lopendeMeter',
                                          label='lopende meter',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Randprofiel.lopendeMeter',
                                          definition='Lopende meter van het randprofiel.',
                                          owner=self)

    @property
    def lopendeMeter(self):
        """Lopende meter van het randprofiel."""
        return self._lopendeMeter.get_waarde()

    @lopendeMeter.setter
    def lopendeMeter(self, value):
        self._lopendeMeter.set_waarde(value, owner=self)
