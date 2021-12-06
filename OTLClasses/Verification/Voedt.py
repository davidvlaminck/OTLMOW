from ModelGenerator.BaseClasses import URIField
from OTLClasses.Verification.DirectioneleRelatie import DirectioneleRelatie
from OTLClasses.Verification.KwantWrdInVolt import KwantWrdInVolt


class Voedt(DirectioneleRelatie):
    """Deze relatie wordt enkel gelegd naar onderdelen die permanent onder spanning staan in normaal bedrijf. Aan deze relatie
    wordt steeds een richting toegekend van de voedinggever naar de ontvanger. """

    def __init__(self):
        pass

    aansluitspanning = KwantWrdInVolt()
    """Spanning van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar."""

    uri: URIField = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt"
