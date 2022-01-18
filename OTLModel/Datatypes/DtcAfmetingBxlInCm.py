# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInCmWaarden(AttributeInfo):
    def __init__(self):
        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm.breedte',
                                     definition='De breedte in centimeter.')

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm.lengte',
                                    definition='De lengte in centimeter.')

    @property
    def breedte(self):
        """De breedte in centimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value)

    @property
    def lengte(self):
        """De lengte in centimeter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInCm(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van de breedte en de lengte in centimeter."""
    naam = 'DtcAfmetingBxlInCm'
    label = 'Afmeting bxl in centimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInCm'
    definition = 'Complex datatype voor de afmeting van de breedte en de lengte in centimeter.'
    waardeObject = DtcAfmetingBxlInCmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

