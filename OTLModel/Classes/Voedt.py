# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie
from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedt(DirectioneleRelatie):
    """Deze relatie wordt enkel gelegd naar onderdelen die permanent onder spanning staan in normaal bedrijf. Aan deze relatie wordt steeds een richting toegekend van de voedinggever naar de ontvanger."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aansluitspanning = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='aansluitspanning',
                                              label='aansluitspanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt.aansluitspanning',
                                              definition='Spanning van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar.')

        self._aansluitvermogen = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='aansluitvermogen',
                                              label='aansluitvermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt.aansluitvermogen',
                                              usagenote='Attribuut uit gebruik sinds versie 2.1.0 ',
                                              deprecated_version='2.1.0',
                                              definition='Vermogen van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar.')

    @property
    def aansluitspanning(self):
        """Spanning van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar."""
        return self._aansluitspanning.waarde

    @aansluitspanning.setter
    def aansluitspanning(self, value):
        self._aansluitspanning.set_waarde(value, owner=self)

    @property
    def aansluitvermogen(self):
        """Vermogen van de aansluiting, dit wordt enkel ingevuld op voedingsrelaties voorbij de hoofdschakelaar."""
        return self._aansluitvermogen.waarde

    @aansluitvermogen.setter
    def aansluitvermogen(self, value):
        self._aansluitvermogen.set_waarde(value, owner=self)
