# coding=utf-8
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.DavieRelatieAttributes import DavieRelatieAttributes
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class RelatieObject(AIMDBStatus, AttributeInfo, DavieRelatieAttributes, OTLObject):
    """Abstracte die de relaties voorziet van gemeenschappelijk eigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AttributeInfo.__init__(self)
        DavieRelatieAttributes.__init__(self)
        OTLObject.__init__(self)
