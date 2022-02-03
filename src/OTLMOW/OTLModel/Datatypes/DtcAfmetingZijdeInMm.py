# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingZijdeInMmWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._zijde = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='zijde',
                                   label='zijde',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingZijdeInMm.zijde',
                                   definition='De afmeting van een zijde in millimeter.',
                                   owner=self)

    @property
    def zijde(self):
        """De afmeting van een zijde in millimeter."""
        return self._zijde.waarde

    @zijde.setter
    def zijde(self, value):
        self._zijde.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingZijdeInMm(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van een zijde in millimeter."""
    naam = 'DtcAfmetingZijdeInMm'
    label = 'Afmeting zijde in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingZijdeInMm'
    definition = 'Complex datatype voor de afmeting van een zijde in millimeter.'
    waardeObject = DtcAfmetingZijdeInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

