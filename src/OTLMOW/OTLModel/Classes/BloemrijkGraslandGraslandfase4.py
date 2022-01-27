# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Grasland import Grasland
from src.OTLMOW.OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class BloemrijkGraslandGraslandfase4(Grasland):
    """G4 - Fijn mozaïek van grassen, kruiden, russen en zeggen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BloemrijkGraslandGraslandfase4'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BloemrijkGraslandGraslandfase4.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.')

    @property
    def huidigNatuurbeeld(self):
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.waarde

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)
