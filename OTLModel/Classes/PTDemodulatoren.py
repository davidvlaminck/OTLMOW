# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTDemodulatoren(PTModuleZFirmware, AttributeInfo):
    """De functie van de demodulator bestaat erin de data, ontvangen door de lus, te decoderen en in het juiste formaat door te sturen naar de centrale verwerkingseenheid, de PT-verwerkingseenheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTDemodulatoren'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        PTModuleZFirmware.__init__(self)
