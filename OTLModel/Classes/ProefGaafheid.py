# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGaafheid(Proef, AttributeInfo):
    """Controle van het lijnvormig element op de ongeschondenheid, volledigheid en zuiverheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._gaafheid = OTLAttribuut(field=DtcDocument,
                                      naam='gaafheid',
                                      label='gaafheid',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid.gaafheid',
                                      definition='De resultaten van de controle.')

    @property
    def gaafheid(self):
        """De resultaten van de controle."""
        return self._gaafheid.waarde

    @gaafheid.setter
    def gaafheid(self, value):
        self._gaafheid.set_waarde(value, owner=self)
