# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.DavieRelatieAttributes import DavieRelatieAttributes
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from OTLMOW.OTLModel.Datatypes.DtcIdentificator import DtcIdentificator


# Generated with OTLClassCreator. To modify: extend, do not edit
class RelatieObject(AIMDBStatus, AttributeInfo, OTLObject, DavieRelatieAttributes):
    """Abstracte die de relaties voorziet van gemeenschappelijk eigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AttributeInfo.__init__(self)
        DavieRelatieAttributes.__init__(self)
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

    @property
    def assetId(self):
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def bronAssetId(self):
        """De identificator van het object waaruit de relatie vertrekt."""
        return self._bronAssetId.get_waarde()

    @bronAssetId.setter
    def bronAssetId(self, value):
        self._bronAssetId.set_waarde(value, owner=self)

    @property
    def doelAssetId(self):
        """De identificator van het object waarin de relatie toekomt."""
        return self._doelAssetId.get_waarde()

    @doelAssetId.setter
    def doelAssetId(self, value):
        self._doelAssetId.set_waarde(value, owner=self)
