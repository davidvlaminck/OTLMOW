# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Seinlantaarn import Seinlantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class OpenbaarVervoerslantaarn(Seinlantaarn):
    """Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van het openbaar vervoer te verhinderen of toe te laten. 
Deze lantaarns worden enkel gebruikt op de plaatsen waar het openbaar vervoer in een eigen bedding of bijzondere overrijdbare bedding rijdt. Het openbaar vervoer en het toegelaten verkeer op de bijzondere overrijdbare bedding moeten deze verkeerslichten volgen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenbaarVervoerslantaarn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie')
