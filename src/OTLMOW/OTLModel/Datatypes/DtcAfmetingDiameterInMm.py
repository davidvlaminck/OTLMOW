# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInMmWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm.diameter',
                                      definition='De diameter in millimeter.',
                                      owner=self)

    @property
    def diameter(self):
        """De diameter in millimeter."""
        return self._diameter.waarde

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInMm(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van een diameter in millimeter."""
    naam = 'DtcAfmetingDiameterInMm'
    label = 'Afmeting diameter in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm'
    definition = 'Complex datatype voor de afmeting van een diameter in millimeter.'
    waardeObject = DtcAfmetingDiameterInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

