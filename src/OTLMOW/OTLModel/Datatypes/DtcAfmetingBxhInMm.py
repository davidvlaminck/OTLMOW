# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxhInMmWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInMm.breedte',
                                     definition='De breedte in millimeter.',
                                     owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInMm.hoogte',
                                    definition='De hoogte in millimeter.',
                                    owner=self)

    @property
    def breedte(self):
        """De breedte in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def hoogte(self):
        """De hoogte in millimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxhInMm(ComplexField, AttributeInfo):
    """Complex datatype voor de afmeting van de breedte en hoogte in millimeter."""
    naam = 'DtcAfmetingBxhInMm'
    label = 'Afmeting bxh in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInMm'
    definition = 'Complex datatype voor de afmeting van de breedte en hoogte in millimeter.'
    waardeObject = DtcAfmetingBxhInMmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

