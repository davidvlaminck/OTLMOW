# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVlakheid(Proef, AttributeInfo):
    """Controle van de effenheid van het oppervlak met behulp van een 3 meter lange rei volgens NBN EN 13036-7."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._vlakheid = OTLAttribuut(field=DtcDocument,
                                      naam='vlakheid',
                                      label='vlakheid',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid.vlakheid',
                                      definition='Proefresultaten van de vlakheid.')

    @property
    def vlakheid(self):
        """Proefresultaten van de vlakheid."""
        return self._vlakheid.waarde

    @vlakheid.setter
    def vlakheid(self, value):
        self._vlakheid.set_waarde(value, owner=self)
