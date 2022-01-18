# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware
from OTLModel.Datatypes.KlVrStuurkaartCommunicatieprotocol import KlVrStuurkaartCommunicatieprotocol


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRStuurkaart(VRModuleMetFirmware, AttributeInfo):
    """Ook wel basissturing genoemd. Dit is de hoofdprocessorkaart van de VRI. Hier wordt het instructieprogramma en het kruispuntprogramma ingeladen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRStuurkaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        VRModuleMetFirmware.__init__(self)

        self._communicatieprotocol = OTLAttribuut(field=KlVrStuurkaartCommunicatieprotocol,
                                                  naam='communicatieprotocol',
                                                  label='communicatieprotocol',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRStuurkaart.communicatieprotocol',
                                                  definition='Gebruikte communicatieprotocol voor de stuurkaart.')

    @property
    def communicatieprotocol(self):
        """Gebruikte communicatieprotocol voor de stuurkaart."""
        return self._communicatieprotocol.waarde

    @communicatieprotocol.setter
    def communicatieprotocol(self, value):
        self._communicatieprotocol.set_waarde(value, owner=self)
