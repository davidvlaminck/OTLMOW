# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlLEGCGeluidskarakteristiek import KlLEGCGeluidskarakteristiek
from OTLMOW.OTLModel.Datatypes.KlLEGCMateriaal import KlLEGCMateriaal


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGCMateriaalKarakteristiekWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._geluidskarakteristiek = OTLAttribuut(field=KlLEGCGeluidskarakteristiek,
                                                   naam='geluidskarakteristiek',
                                                   label='geluidskarakteristiek',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek.geluidskarakteristiek',
                                                   definition='Het kenmerkend gedrag inzake geluid van de geluidswerende constructie.')

        self._materiaal = OTLAttribuut(field=KlLEGCMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek.materiaal',
                                       definition='Het materiaal van de geluidswerende constructie.')

    @property
    def geluidskarakteristiek(self):
        """Het kenmerkend gedrag inzake geluid van de geluidswerende constructie."""
        return self._geluidskarakteristiek.waarde

    @geluidskarakteristiek.setter
    def geluidskarakteristiek(self, value):
        self._geluidskarakteristiek.set_waarde(value, owner=self._parent)

    @property
    def materiaal(self):
        """Het materiaal van de geluidswerende constructie."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcGCMateriaalKarakteristiek(ComplexField, AttributeInfo):
    """Complex datatype voor het materiaal en zijn geluidskarakteristiek van de geluidswerende constructie."""
    naam = 'DtcGCMateriaalKarakteristiek'
    label = 'Materiaal karakteristiek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcGCMateriaalKarakteristiek'
    definition = 'Complex datatype voor het materiaal en zijn geluidskarakteristiek van de geluidswerende constructie.'
    waardeObject = DtcGCMateriaalKarakteristiekWaarden

    def __str__(self):
        return ComplexField.__str__(self)

