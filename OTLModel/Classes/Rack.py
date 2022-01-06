from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRackMerk import KlRackMerk
from OTLModel.Datatypes.KlRackModelnaam import KlRackModelnaam
from OTLModel.Datatypes.KlRackType import KlRackType
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rack(AIMNaamObject):
    """Interne draagstructuur binnen een behuizing voor (elektromechanische) toestellen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.diepte = KwantWrdInCentimeter()
        """De diepte van het rack tussen de voorste en achterste rails."""
        self.diepte.naam = "diepte"
        self.diepte.label = "diepte"
        self.diepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.diepte"
        self.diepte.definition = "De diepte van het rack tussen de voorste en achterste rails."
        self.diepte.constraints = ""
        self.diepte.usagenote = ""
        self.diepte.deprecated_version = ""

        self.hoogteInRU = IntegerField(naam="hoogteInRU",
                                       label="hoogte in RU",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.hoogteInRU",
                                       definition="Bruikbare ruimte om toestellen te monteren, uitgedrukt in RU (rack units).",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Bruikbare ruimte om toestellen te monteren, uitgedrukt in RU (rack units)."""

        self.huidigBeeld = DtcDocument()
        """Foto of schematische voorstelling van de huidige samenstelling van de samenstelling in het rack."""
        self.huidigBeeld.naam = "huidigBeeld"
        self.huidigBeeld.label = "huidig beeld"
        self.huidigBeeld.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.huidigBeeld"
        self.huidigBeeld.definition = "Foto of schematische voorstelling van de huidige samenstelling van de samenstelling in het rack."
        self.huidigBeeld.constraints = ""
        self.huidigBeeld.usagenote = ""
        self.huidigBeeld.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlRackMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.merk",
                                    definition="Merk waarmee de fabrikant dit type rack identificeert.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk waarmee de fabrikant dit type rack identificeert."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlRackModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.modelnaam",
                                         definition="Modelnaam waarmee de fabrikant dit type toestel identificeert.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""

        self.rackType = KeuzelijstField(naam="rackType",
                                        label="Rack type",
                                        lijst=KlRackType(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.rackType",
                                        definition="Geeft het type aan voor een rack volgens een keuzelijst van beschikbare types.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Geeft het type aan voor een rack volgens een keuzelijst van beschikbare types."""
