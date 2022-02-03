# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInMWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.breedte',
                                     definition='De breedte in meter.',
                                     owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.hoogte',
                                    definition='De hoogte in meter.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM.lengte',
                                    definition='De lengte in meter.',
                                    owner=self)

    @property
    def breedte(self):
        """De breedte in meter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def hoogte(self):
        """De hoogte in meter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self._parent)

    @property
    def lengte(self):
        """De lengte in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInM(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van de breedte, de lengte en hoogte in meter."""
    naam = 'DtcAfmetingBxlxhInM'
    label = 'Afmeting bxlxh in meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInM'
    definition = 'Complex datatype voor de afmeting van de breedte, de lengte en hoogte in meter.'
    waardeObject = DtcAfmetingBxlxhInMWaarden

    def __str__(self):
        return ComplexField.__str__(self)

