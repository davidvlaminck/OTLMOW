from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlTerugslagklepType import KlTerugslagklepType
from OTLModel.Datatypes.KlTsklepAfsluiterMateriaal import KlTsklepAfsluiterMateriaal
from OTLModel.Datatypes.KlVormTerugslagklep import KlVormTerugslagklep
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugslagklep(LinkendElement):
    """Een terugslagklep is een klep die dient om water, vloeistof, granulaat, poeder of gas in één richting door te laten. Meestal duwt het medium de klep bij het heenstromen open en sluit een veer of de zwaartekracht de klep."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedteOpening = KwantWrdInMillimeter()
        """Breedte van de opening die door de terugslagklep wordt afgesloten in millimeter."""
        self.breedteOpening.naam = "breedteOpening"
        self.breedteOpening.label = "breedte opening"
        self.breedteOpening.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.breedteOpening"
        self.breedteOpening.definition = "Breedte van de opening die door de terugslagklep wordt afgesloten in millimeter."
        self.breedteOpening.constraints = ""
        self.breedteOpening.usagenote = ""
        self.breedteOpening.deprecated_version = ""

        self.diameter = KwantWrdInMillimeter()
        """De diameter van de terugslagklep in millimeter."""
        self.diameter.naam = "diameter"
        self.diameter.label = "diameter"
        self.diameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.diameter"
        self.diameter.definition = "De diameter van de terugslagklep in millimeter."
        self.diameter.constraints = ""
        self.diameter.usagenote = ""
        self.diameter.deprecated_version = ""

        self.hoogteOpening = KwantWrdInMillimeter()
        """De hoogte van de opening die door de terugslagklep wordt afgesloten in millimeter."""
        self.hoogteOpening.naam = "hoogteOpening"
        self.hoogteOpening.label = "hoogte opening"
        self.hoogteOpening.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.hoogteOpening"
        self.hoogteOpening.definition = "De hoogte van de opening die door de terugslagklep wordt afgesloten in millimeter."
        self.hoogteOpening.constraints = ""
        self.hoogteOpening.usagenote = ""
        self.hoogteOpening.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlTsklepAfsluiterMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.materiaal",
                                         definition="Het materiaal waaruit de terugslagklep is vervaardigd.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit de terugslagklep is vervaardigd."""

        self.peil = KwantWrdInMeterTAW()
        """Niveau van de doorlaatopening van de terugslagklep uitgedrukt in meter-TAW."""
        self.peil.naam = "peil"
        self.peil.label = "peil"
        self.peil.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.peil"
        self.peil.definition = "Niveau van de doorlaatopening van de terugslagklep uitgedrukt in meter-TAW."
        self.peil.constraints = ""
        self.peil.usagenote = ""
        self.peil.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlTerugslagklepType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.type",
                                    definition="Bepaalt het type van terugslagklep.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaalt het type van terugslagklep."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlVormTerugslagklep(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.vorm",
                                    definition="De vorm van de terugslagklep.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van de terugslagklep."""
