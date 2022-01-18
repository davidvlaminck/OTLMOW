# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDraagvermogen(Proef, AttributeInfo):
    """Controle van de verdichting van de ondergrond of van een funderingslaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._draagvermogen = OTLAttribuut(field=DtcDocument,
                                           naam='draagvermogen',
                                           label='draagvermogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraagvermogen.draagvermogen',
                                           definition='Proef die het draagvermogen van de laag bepaald.')

    @property
    def draagvermogen(self):
        """Proef die het draagvermogen van de laag bepaald."""
        return self._draagvermogen.waarde

    @draagvermogen.setter
    def draagvermogen(self, value):
        self._draagvermogen.set_waarde(value, owner=self)
