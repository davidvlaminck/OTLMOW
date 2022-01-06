from OTLModel.Classes.HoutigeVegetatie import HoutigeVegetatie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class Struweel(HoutigeVegetatie):
    """Een struweel is een met struiken begroeide oppervlakte dat minimaal 5 m breed  is, minimaal 1 m hoog, maar meestal 2 tot 5 m hoog is. Een struweel is meestal meersoortig en vaak aan de rand van een bos terug te vinden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Struweel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.huidigNatuurbeeld = KeuzelijstField(naam="huidigNatuurbeeld",
                                                 label="huidig natuurbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Struweel.huidigNatuurbeeld",
                                                 definition="Bepaling van het vegetatietype op basis van terreininventarisatie.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""

        self.natuurstreefbeeld = KeuzelijstField(naam="natuurstreefbeeld",
                                                 label="natuurstreefbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Struweel.natuurstreefbeeld",
                                                 definition="Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden."""
