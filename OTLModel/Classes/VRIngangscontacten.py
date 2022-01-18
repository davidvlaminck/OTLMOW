# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRIngangscontacten(VRModuleMetFirmware, AttributeInfo):
    """Visualisatie van inkomende contacten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIngangscontacten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        VRModuleMetFirmware.__init__(self)
