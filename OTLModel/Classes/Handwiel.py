from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handwiel(AIMObject):
    """Een handwiel kan worden gebruikt voor het openen of sluiten van een afsluiter."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handwiel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
