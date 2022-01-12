# coding=utf-8
from OTLModel.Classes.HoutigeVegetatie import HoutigeVegetatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGroeiplaatsverbetering import KlGroeiplaatsverbetering
from OTLModel.Datatypes.KlHoutigeType import KlHoutigeType
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class OpgaandeHoutigeVegetatie(HoutigeVegetatie):
    """Een houtkant of een bos."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        groeiplaatsverbeteringField = KeuzelijstField(naam="groeiplaatsverbetering",
                                                      label="groeiplaatsverbetering",
                                                      lijst=KlGroeiplaatsverbetering(),
                                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.groeiplaatsverbetering",
                                                      definition="De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.groeiplaatsverbetering = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=groeiplaatsverbeteringField)
        """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""

        self.huidigNatuurbeeld = KeuzelijstField(naam="huidigNatuurbeeld",
                                                 label="huidig natuurbeeld",
                                                 lijst=KlNSB(),
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.huidigNatuurbeeld",
                                                 definition="Bepaling van het vegetatietype op basis van terreininventarisatie.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""

        self.natuurstreefbeeld = KeuzelijstField(naam="natuurstreefbeeld",
                                                 label="natuurstreefbeeld",
                                                 lijst=KlNSB(),
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.natuurstreefbeeld",
                                                 definition="Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer.In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlHoutigeType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeHoutigeVegetatie.type",
                                    definition="Het type van de opgaande houtige vegetatie.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de opgaande houtige vegetatie."""
