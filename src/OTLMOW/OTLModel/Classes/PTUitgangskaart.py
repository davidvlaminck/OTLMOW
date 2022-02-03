# coding=utf-8
from OTLMOW.OTLModel.Classes.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTUitgangskaart(PTModuleZFirmware):
    """Relaiskaart met 12 spanningsvrije contacten per kaart, max. 2 bijkomende kaarten per luscontactinterface."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTUitgangskaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
