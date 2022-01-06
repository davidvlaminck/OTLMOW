from abc import abstractmethod
from OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.URIField import URIField


# Generated with OTLClassCreator. To modify: extend, do not edit
class RelatieObject(AIMDBStatus):
    """Abstracte die de relaties voorziet van gemeenschappelijk eigenschappen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.assetId = DtcIdentificator()
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        self.assetId.naam = "assetId"
        self.assetId.label = "asset-id"
        self.assetId.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.assetId"
        self.assetId.definition = "Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."
        self.assetId.constraints = ""
        self.assetId.usagenote = ""
        self.assetId.deprecated_version = ""

        self.bronAssetId = DtcIdentificator()
        """De identificator van het object waaruit de relatie vertrekt."""
        self.bronAssetId.naam = "bronAssetId"
        self.bronAssetId.label = "asset-id bron-asset"
        self.bronAssetId.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.bronAssetId"
        self.bronAssetId.definition = "De identificator van het object waaruit de relatie vertrekt."
        self.bronAssetId.constraints = ""
        self.bronAssetId.usagenote = ""
        self.bronAssetId.deprecated_version = ""

        self.doelAssetId = DtcIdentificator()
        """De identificator van het object waarin de relatie toekomt."""
        self.doelAssetId.naam = "doelAssetId"
        self.doelAssetId.label = "asset-id doel-asset"
        self.doelAssetId.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.doelAssetId"
        self.doelAssetId.definition = "De identificator van het object waarin de relatie toekomt."
        self.doelAssetId.constraints = ""
        self.doelAssetId.usagenote = ""
        self.doelAssetId.deprecated_version = ""

        uri = self.typeURI
        self.typeURI = URIField(naam="typeURI",
                                label="type URI",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.typeURI",
                                definition="De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI .",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI ."""
