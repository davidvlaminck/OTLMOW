# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.GrazigeVegetatie import GrazigeVegetatie
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grasland(GrazigeVegetatie, AttributeInfo):
    """Grazige vegetatie met daarin kruidachtigen die jaarlijks één of meerdere malen per jaar gemaaid of begraasd wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasland'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        GrazigeVegetatie.__init__(self)

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
