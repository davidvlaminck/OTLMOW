from OTLModel.Classes.Seinlantaarn import Seinlantaarn


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voertuiglantaarn(Seinlantaarn):
    """Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van voertuigen te verhinderen of toe te laten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voertuiglantaarn"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
