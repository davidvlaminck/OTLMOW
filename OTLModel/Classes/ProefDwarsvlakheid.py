# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDwarsvlakheid(Proef, AttributeInfo):
    """Controle van de spoorvorming via de latmethode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._dwarsvlakheid = OTLAttribuut(field=DtcDocument,
                                           naam='dwarsvlakheid',
                                           label='dwarsvlakheid',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid.dwarsvlakheid',
                                           definition='Proefresultaten van de dwarsvlakheid.')

    @property
    def dwarsvlakheid(self):
        """Proefresultaten van de dwarsvlakheid."""
        return self._dwarsvlakheid.waarde

    @dwarsvlakheid.setter
    def dwarsvlakheid(self, value):
        self._dwarsvlakheid.set_waarde(value, owner=self)
