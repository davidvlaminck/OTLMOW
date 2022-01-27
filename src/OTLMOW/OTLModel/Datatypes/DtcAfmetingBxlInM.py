# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInMWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInM.breedte',
                                     definition='De breedte in meter.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInM.lengte',
                                    definition='De lengte in meter.')

    @property
    def breedte(self):
        """De breedte in meter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def lengte(self):
        """De lengte in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlInM(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van de breedte en de lengte in meter."""
    naam = 'DtcAfmetingBxlInM'
    label = 'Afmeting bxl in meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlInM'
    definition = 'Complex datatype voor de afmeting van de breedte en de lengte in meter.'
    waardeObject = DtcAfmetingBxlInMWaarden

    def __str__(self):
        return ComplexField.__str__(self)

