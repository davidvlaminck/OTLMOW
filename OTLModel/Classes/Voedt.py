# coding=utf-8
from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie
from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedt(DirectioneleRelatie):
    """Deze relatie wordt enkel gelegd naar onderdelen die permanent onder spanning staan in normaal bedrijf. Aan deze relatie wordt steeds een richting toegekend van de voedinggever naar de ontvanger."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aansluitspanning = KwantWrdInVolt()
        """Spanning van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar."""
        self.aansluitspanning.naam = "aansluitspanning"
        self.aansluitspanning.label = "aansluitspanning"
        self.aansluitspanning.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt.aansluitspanning"
        self.aansluitspanning.definition = "Spanning van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar."
        self.aansluitspanning.constraints = ""
        self.aansluitspanning.usagenote = ""
        self.aansluitspanning.deprecated_version = ""
