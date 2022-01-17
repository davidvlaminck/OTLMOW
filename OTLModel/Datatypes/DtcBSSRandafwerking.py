# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KlBSSRandafwerking import KlBSSRandafwerking
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBSSRandafwerkingWaarden(AttributeInfo):
    def __init__(self):
        self._lengteRandafwerking = OTLAttribuut(field=KwantWrdInMeter,
                                                 naam='lengteRandafwerking',
                                                 label='lengte randafwerking',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.lengteRandafwerking',
                                                 definition='De lengte in meter van de randafwerking.')

        self._randafwerking = OTLAttribuut(field=KlBSSRandafwerking,
                                           naam='randafwerking',
                                           label='randafwerking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking.randafwerking',
                                           definition='De mogelijke wijzen van randafwerking van de verharding.')

    @property
    def lengteRandafwerking(self):
        """De lengte in meter van de randafwerking."""
        return self._lengteRandafwerking.waarde

    @lengteRandafwerking.setter
    def lengteRandafwerking(self, value):
        self._lengteRandafwerking.set_waarde(value)

    @property
    def randafwerking(self):
        """De mogelijke wijzen van randafwerking van de verharding."""
        return self._randafwerking.waarde

    @randafwerking.setter
    def randafwerking(self, value):
        self._randafwerking.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBSSRandafwerking(ComplexField, AttributeInfo):
    """Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding."""
    naam = 'DtcBSSRandafwerking'
    label = 'Betonstraatsteenafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBSSRandafwerking'
    definition = 'Complex datatype voor de afwerking van de rand van een betonstraatsteenverharding.'
    waardeObject = DtcBSSRandafwerkingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

