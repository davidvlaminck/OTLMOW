# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Seinlantaarn import Seinlantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voetgangerslantaarn(Seinlantaarn):
    """Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van voetgangers te verhinderen of toe te laten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voetgangerslantaarn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie')
