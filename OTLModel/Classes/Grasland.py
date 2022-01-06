from OTLModel.Classes.GrazigeVegetatie import GrazigeVegetatie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grasland(GrazigeVegetatie):
    """Grazige vegetatie met daarin kruidachtigen die jaarlijks één of meerdere malen per jaar gemaaid of begraasd wordt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasland"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.natuurstreefbeeld = KeuzelijstField(naam="natuurstreefbeeld",
                                                 label="natuurstreefbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grasland.natuurstreefbeeld",
                                                 definition="Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden."""
