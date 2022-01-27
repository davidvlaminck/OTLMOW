# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.GrazigeVegetatie import GrazigeVegetatie
from OTLMOW.OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grasland(GrazigeVegetatie):
    """Grazige vegetatie met daarin kruidachtigen die jaarlijks één of meerdere malen per jaar gemaaid of begraasd wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasland'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._natuurstreefbeeld = OTLAttribuut(field=KlNSB,
                                               naam='natuurstreefbeeld',
                                               label='natuurstreefbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasland.natuurstreefbeeld',
                                               definition='Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden.')

    @property
    def natuurstreefbeeld(self):
        """Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.
In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden."""
        return self._natuurstreefbeeld.waarde

    @natuurstreefbeeld.setter
    def natuurstreefbeeld(self, value):
        self._natuurstreefbeeld.set_waarde(value, owner=self)