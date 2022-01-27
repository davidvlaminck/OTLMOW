# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.HoutigeVegetatie import HoutigeVegetatie
from src.OTLMOW.OTLModel.Datatypes.KlGroeiplaatsverbetering import KlGroeiplaatsverbetering
from src.OTLMOW.OTLModel.Datatypes.KlHoutigeType import KlHoutigeType
from src.OTLMOW.OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class OpgaandeHoutigeVegetatie(HoutigeVegetatie):
    """Een houtkant of een bos."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._groeiplaatsverbetering = OTLAttribuut(field=KlGroeiplaatsverbetering,
                                                    naam='groeiplaatsverbetering',
                                                    label='groeiplaatsverbetering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.groeiplaatsverbetering',
                                                    kardinaliteit_max='*',
                                                    definition='De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.')

        self._huidigNatuurbeeld = OTLAttribuut(field=KlNSB,
                                               naam='huidigNatuurbeeld',
                                               label='huidig natuurbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.huidigNatuurbeeld',
                                               definition='Bepaling van het vegetatietype op basis van terreininventarisatie.')

        self._natuurstreefbeeld = OTLAttribuut(field=KlNSB,
                                               naam='natuurstreefbeeld',
                                               label='natuurstreefbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.natuurstreefbeeld',
                                               definition='Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden.')

        self._type = OTLAttribuut(field=KlHoutigeType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.type',
                                  definition='Het type van de opgaande houtige vegetatie.')

    @property
    def groeiplaatsverbetering(self):
        """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""
        return self._groeiplaatsverbetering.waarde

    @groeiplaatsverbetering.setter
    def groeiplaatsverbetering(self, value):
        self._groeiplaatsverbetering.set_waarde(value, owner=self)

    @property
    def huidigNatuurbeeld(self):
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
        return self._huidigNatuurbeeld.waarde

    @huidigNatuurbeeld.setter
    def huidigNatuurbeeld(self, value):
        self._huidigNatuurbeeld.set_waarde(value, owner=self)

    @property
    def natuurstreefbeeld(self):
        """Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.
In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden."""
        return self._natuurstreefbeeld.waarde

    @natuurstreefbeeld.setter
    def natuurstreefbeeld(self, value):
        self._natuurstreefbeeld.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de opgaande houtige vegetatie."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
