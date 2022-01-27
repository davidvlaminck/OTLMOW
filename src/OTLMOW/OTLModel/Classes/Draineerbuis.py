# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Buis import Buis
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlDraineerbuisMateriaal import KlDraineerbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draineerbuis(Buis):
    """Een buis voor het afvoeren van water uit de bodem over en door de grond,met als gevolg het verlagen van het grondwaterpeil."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftDrainbrug = OTLAttribuut(field=BooleanField,
                                            naam='heeftDrainbrug',
                                            label='heeft drainbrug',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.heeftDrainbrug',
                                            definition='Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden.')

        self._materiaal = OTLAttribuut(field=KlDraineerbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.materiaal',
                                       definition='Bepaalt het materiaal van de draineerbuis.')

    @property
    def heeftDrainbrug(self):
        """Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden."""
        return self._heeftDrainbrug.waarde

    @heeftDrainbrug.setter
    def heeftDrainbrug(self, value):
        self._heeftDrainbrug.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de draineerbuis."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
