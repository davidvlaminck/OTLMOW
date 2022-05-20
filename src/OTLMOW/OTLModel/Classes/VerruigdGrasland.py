# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Ruigte import Ruigte
from OTLMOW.OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerruigdGrasland(Ruigte):
    """R2 - grote brandnetel, kleefkruid, ridderzuring, akkerdistel, speerdistel, gewone berenklauw, fluitenkruid, bramen, klit, jacobskruiskruid, ijle dravik, dolle kervel, kweek, kropaar, haagwinde, zevenblad."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerruigdGrasland'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerruigdGrasland.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.',
                                               owner=self)

    @property
    def huidigNatuurbeeld(self):
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.get_waarde()

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)
