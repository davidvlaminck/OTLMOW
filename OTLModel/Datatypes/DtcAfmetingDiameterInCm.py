# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInCmWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._diameter = OTLAttribuut(field=KwantWrdInCentimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInCm.diameter',
                                      definition='De diameter in centimeter.')

    @property
    def diameter(self):
        """De diameter in centimeter."""
        return self._diameter.waarde

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInCm(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van een diameter in centimeter."""
    naam = 'DtcAfmetingDiameterInCm'
    label = 'Afmeting diameter in centimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInCm'
    definition = 'Complex datatype voor de afmeting van een diameter in centimeter.'
    waardeObject = DtcAfmetingDiameterInCmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

