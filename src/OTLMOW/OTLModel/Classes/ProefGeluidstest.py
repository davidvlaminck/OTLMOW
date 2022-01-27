# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcGeluidstestRapport import DtcGeluidstestRapport


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGeluidstest(Proef):
    """Test van het geluidsscherm op oa. luchtgeluidsisolatie, geluidsabsorptie, e.d. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

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
