# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingDiameterInMmWaarden(AttributeInfo):
    def __init__(self):
        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingDiameterInMm.diameter',
                                      definition='De diameter in millimeter.')

    @property
    def diameter(self):
        """De diameter in millimeter."""
        return self._diameter.waarde

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value)


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

