from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLModel.Verification.DirectioneleRelatie import DirectioneleRelatie



class Voedt(DirectioneleRelatie):
    """Deze relatie wordt enkel gelegd naar onderdelen die permanent onder spanning staan in normaal bedrijf. Aan deze relatie
    wordt steeds een richting toegekend van de voedinggever naar de ontvanger. """

    def __init__(self):
        pass

    aansluitspanning = KwantWrdInVolt()
    """Spanning van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar."""

    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""
