# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTSCKaart(PTModuleZFirmware, AttributeInfo):
    """Seriële controle uitbreidingskaart (optioneel): 4 lussen per kaart, max. 2 bijkomende uitbreidingskaarten per luscontactinterface."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTSCKaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        PTModuleZFirmware.__init__(self)
