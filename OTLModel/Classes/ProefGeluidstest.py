# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcGeluidstestRapport import DtcGeluidstestRapport


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGeluidstest(Proef, AttributeInfo):
    """Test van het geluidsscherm op oa. luchtgeluidsisolatie, geluidsabsorptie, e.d. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._geluidstestrapport = OTLAttribuut(field=DtcGeluidstestRapport,
                                                naam='geluidstestrapport',
                                                label='geluidstestrapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest.geluidstestrapport',
                                                definition='Het resultaat geluidstest.')

    @property
    def geluidstestrapport(self):
        """Het resultaat geluidstest."""
        return self._geluidstestrapport.waarde

    @geluidstestrapport.setter
    def geluidstestrapport(self, value):
        self._geluidstestrapport.set_waarde(value, owner=self)
