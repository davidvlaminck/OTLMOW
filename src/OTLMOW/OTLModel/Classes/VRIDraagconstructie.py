# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.SteunStandaard import SteunStandaard


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRIDraagconstructie(SteunStandaard):
    """Abstracte voor een dragend element (bv. paal, kolom ) waaraan lantaarns met verkeerslichten bevestigd kunnen worden bij de verkeersregelinstallatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
