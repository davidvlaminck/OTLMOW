from OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlUPSMerk import KlUPSMerk
from OTLModel.Datatypes.KlUPSModelnaam import KlUPSModelnaam
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLModel.Datatypes.KwantWrdInkWh import KwantWrdInkWh
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class UPS(Voedingspunt):
    """Toestel (Uninterruptible Power Supply = niet onderbreekbare voeding) voor het leveren van  elektrische energie van een vastgelegde kwaliteit, onafhankelijk van de beschikbaarheid van een betrouwbare netspanning. Indien het openbare net niet langer bruikbaar is om als energiebron te fungeren, wordt de energievoorziening overgenomen door de accubatterij. Deze zal gedurende een bepaalde tijd, afhankelijk van de capaciteit, de stroomvoorziening verzorgen. De UPS dient om de (minimale) voeding ononderbroken te verzekeren"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.autonomie = KwantWrdInkWh()
        """De tijd die de UPS een installatie van voeding kan voorzien."""
        self.autonomie.naam = "autonomie"
        self.autonomie.label = "autonomie"
        self.autonomie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.autonomie"
        self.autonomie.definition = "De tijd die de UPS een installatie van voeding kan voorzien."
        self.autonomie.constraints = ""
        self.autonomie.usagenote = ""
        self.autonomie.deprecated_version = ""

        self.maxContinuVermogen = KwantWrdInWatt()
        """Maximale continu vermogen van de UPS."""
        self.maxContinuVermogen.naam = "maxContinuVermogen"
        self.maxContinuVermogen.label = "maximaal continu vermogen"
        self.maxContinuVermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.maxContinuVermogen"
        self.maxContinuVermogen.definition = "Maximale continu vermogen van de UPS."
        self.maxContinuVermogen.constraints = ""
        self.maxContinuVermogen.usagenote = ""
        self.maxContinuVermogen.deprecated_version = ""

        self.maxPiekVermogen = KwantWrdInWatt()
        """Het maximale piekvermogen van de UPS."""
        self.maxPiekVermogen.naam = "maxPiekVermogen"
        self.maxPiekVermogen.label = "max piekvermogen"
        self.maxPiekVermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.maxPiekVermogen"
        self.maxPiekVermogen.definition = "Het maximale piekvermogen van de UPS."
        self.maxPiekVermogen.constraints = ""
        self.maxPiekVermogen.usagenote = ""
        self.maxPiekVermogen.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlUPSMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.merk",
                                    definition="Merk waarmee de fabrikant de UPS identificeert.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk waarmee de fabrikant de UPS identificeert."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlUPSModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.modelnaam",
                                         definition="Modelnaam van de UPS volgens de fabrikant.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van de UPS volgens de fabrikant."""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.serienummer",
                                       definition="Unieke identificatiecode van het toestel, toegekend door de fabrikant.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
