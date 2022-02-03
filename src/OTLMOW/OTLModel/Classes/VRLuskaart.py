# coding=utf-8
from OTLMOW.OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRLuskaart(VRModuleMetFirmware):
    """Kaart die instaat voor het verwerken van de informatie uit de lussen en voor het doorgeven van die informatie naar de besturingskaart."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRLuskaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
