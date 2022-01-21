# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInMmWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.breedte',
                                     definition='De breedte in millimeter.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.hoogte',
                                    definition='De hoogte in millimeter.')

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm.lengte',
                                    definition='De lengte in millimeter.')

    @property
    def breedte(self):
        """De breedte in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def hoogte(self):
        """De hoogte in millimeter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self._parent)

    @property
    def lengte(self):
        """De lengte in millimeter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInMm(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van de breedte,de lengte en hoogte in millimeter."""
    naam = 'DtcAfmetingBxlxhInMm'
    label = 'Afmeting bxlxh in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInMm'
    definition = 'Complex datatype voor de afmeting van de breedte,de lengte en hoogte in millimeter.'
    waardeObject = DtcAfmetingBxlxhInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

