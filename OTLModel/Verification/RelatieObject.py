from abc import abstractmethod

from OTLModel.Datatypes.URIField import URIField
from OTLModel.Verification.AIMDBStatus import AIMDBStatus
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator


class RelatieObject(AIMDBStatus):
    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

    assetId = DtcIdentificator()

    bronAssetId = DtcIdentificator()

    doelAssetId = DtcIdentificator()

    typeURI = URIField(naam="typeURI",
                                label="type URI",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI",
                                definition="De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI .",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""
