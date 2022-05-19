# coding=utf-8
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class DteAssetTypeWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._typeURI = OTLAttribuut(field=StringField,
                                     naam='typeURI',
                                     label='typeURI',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.typeURI',
                                     definition='De uri van het assettype.',
                                     owner=self)

    @property
    def typeURI(self):
        """De uri van het assettype."""
        return self._typeURI.get_waarde()

    @typeURI.setter
    def typeURI(self, value):
        self._typeURI.set_waarde(value, owner=self._parent)


class DteAssetType(ComplexField, AttributeInfo):
    """Complex datatype om het assettype te benoemen"""
    naam = 'DteAssetType'
    label = 'AssetType'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteAssetType'
    definition = 'Complex datatype om het assettype te benoemen.'
    waardeObject = DteAssetTypeWaarden

    def __str__(self):
        return ComplexField.__str__(self)