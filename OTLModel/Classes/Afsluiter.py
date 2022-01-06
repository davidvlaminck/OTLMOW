# coding=utf-8
from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAfsluiterType import KlAfsluiterType
from OTLModel.Datatypes.KlTsklepAfsluiterMateriaal import KlTsklepAfsluiterMateriaal
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afsluiter(LinkendElement):
    """Een afsluiter dient om rioolstrengen af te sluiten bij bv. gebreken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.actueleHoogte = KwantWrdInMillimeter()
        """De afstand tussen het vloeipeil van de opening en de laagste positie van de schuif."""
        self.actueleHoogte.naam = "actueleHoogte"
        self.actueleHoogte.label = "actuele hoogte"
        self.actueleHoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.actueleHoogte"
        self.actueleHoogte.definition = "De afstand tussen het vloeipeil van de opening en de laagste positie van de schuif."
        self.actueleHoogte.constraints = ""
        self.actueleHoogte.usagenote = ""
        self.actueleHoogte.deprecated_version = ""

        self.breedte = KwantWrdInMillimeter()
        """De afstand tussen de uiterste zijden van de afsluiter in millimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.breedte"
        self.breedte.definition = "De afstand tussen de uiterste zijden van de afsluiter in millimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.hoogte = KwantWrdInMillimeter()
        """De afstand tussen het hoogste en laagste punt van de afsluiter met uitzondering van de spindel in millimeter."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.hoogte"
        self.hoogte.definition = "De afstand tussen het hoogste en laagste punt van de afsluiter met uitzondering van de spindel in millimeter."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlTsklepAfsluiterMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.materiaal",
                                         definition="Materiaal waaruit de afsluiter is vervaardigd.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Materiaal waaruit de afsluiter is vervaardigd."""

        self.peil = KwantWrdInMeterTAW()
        """BOK-peil in meter-TAW van de onderkant van de doorlaat van de afsluiter."""
        self.peil.naam = "peil"
        self.peil.label = "peil"
        self.peil.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.peil"
        self.peil.definition = "BOK-peil in meter-TAW van de onderkant van de doorlaat van de afsluiter."
        self.peil.constraints = ""
        self.peil.usagenote = ""
        self.peil.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlAfsluiterType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.type",
                                    definition="Bepaalt het type van de afsluiter.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaalt het type van de afsluiter."""
