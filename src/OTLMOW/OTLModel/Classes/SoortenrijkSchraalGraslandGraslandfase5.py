# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Grasland import Grasland
from OTLMOW.OTLModel.Datatypes.KlNSB import KlNSB
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SoortenrijkSchraalGraslandGraslandfase5(Grasland, VlakGeometrie):
    """G5 - Een fijn, soortenrijk mozaïek van geel-, grijs- en blauwgroene laagblijvende schijngrassen (zeggen en russen) en kruiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoortenrijkSchraalGraslandGraslandfase5'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Grasland.__init__(self)
        VlakGeometrie.__init__(self)

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoortenrijkSchraalGraslandGraslandfase5.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.',
                                               owner=self)

    @property
    def huidigNatuurbeeld(self):
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.waarde

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)
