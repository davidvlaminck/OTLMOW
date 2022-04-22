# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class BronOfDoelTypeWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._typeURI = OTLAttribuut(field=StringField,
                                     naam='typeURI',
                                     label='typeURI',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#BronOfDoelType.typeURI',
                                     definition='Een groep van tekens om een URI te vormen',
                                     owner=self)

    @property
    def typeURI(self):
        """Een groep van tekens om een AIM object te identificeren of te benoemen."""
        return self._typeURI.waarde

    @typeURI.setter
    def typeURI(self, value):
        self._typeURI.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBronOfDoelType(ComplexField, AttributeInfo):
    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""
    naam = 'BronOfDoelType'
    label = 'BronOfDoelType'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#BronOfDoelType'
    definition = 'extra datatype om aanleveringen in Davie te faciliteren waar het type van de bron of doel van een relatie expliciet moet worden meegegeven'
    waardeObject = BronOfDoelTypeWaarden

    def __str__(self):
        return ComplexField.__str__(self)


# Generated with OTLClassCreator. To modify: extend, do not edit
class RelatieObject(AIMDBStatus, AttributeInfo, OTLObject):
    """Abstracte die de relaties voorziet van gemeenschappelijk eigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AttributeInfo.__init__(self)
        OTLObject.__init__(self)

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._bronAssetId = OTLAttribuut(field=DtcIdentificator,
                                         naam='bronAssetId',
                                         label='asset-id bron-asset',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.bronAssetId',
                                         definition='De identificator van het object waaruit de relatie vertrekt.',
                                         owner=self)

        self._doelAssetId = OTLAttribuut(field=DtcIdentificator,
                                         naam='doelAssetId',
                                         label='asset-id doel-asset',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.doelAssetId',
                                         definition='De identificator van het object waarin de relatie toekomt.',
                                         owner=self)

        self._bron = OTLAttribuut(field=DtcBronOfDoelType,
                                  naam='bron',
                                  label='bron',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.bron',
                                  definition='De bron van de relatie.',
                                  owner=self)

        self._doel = OTLAttribuut(field=DtcBronOfDoelType,
                                  naam='doel',
                                  label='doel',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.doel',
                                  definition='Het doel van de relatie.',
                                  owner=self)

    @property
    def assetId(self):
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.waarde

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def bronAssetId(self):
        """De identificator van het object waaruit de relatie vertrekt."""
        return self._bronAssetId.waarde

    @bronAssetId.setter
    def bronAssetId(self, value):
        self._bronAssetId.set_waarde(value, owner=self)

    @property
    def doelAssetId(self):
        """De identificator van het object waarin de relatie toekomt."""
        return self._doelAssetId.waarde

    @doelAssetId.setter
    def doelAssetId(self, value):
        self._doelAssetId.set_waarde(value, owner=self)

    @property
    def bron(self):
        """De bron van de relatie."""
        return self._bron.waarde

    @bron.setter
    def bron(self, value):
        self._bron.set_waarde(value, owner=self)

    @property
    def doel(self):
        """Het doel van de relatie."""
        return self._doel.waarde

    @doel.setter
    def doel(self, value):
        self._doel.set_waarde(value, owner=self)
