# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRKortsluitbeveiliging(VRModuleMetFirmware, AttributeInfo):
    """Een elektronische kortsluitbeveiliging ingebouwd in de vermogen-/lampenschakelaars. Tevens zijn alle uitgangen voorzien van een zekering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRKortsluitbeveiliging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        VRModuleMetFirmware.__init__(self)
