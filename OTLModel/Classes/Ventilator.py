from OTLModel.Classes.Ventilatie import Ventilatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVentilatorGebruik import KlVentilatorGebruik
from OTLModel.Datatypes.KlVentilatorRichting import KlVentilatorRichting
from OTLModel.Datatypes.KwantWrdInProcent import KwantWrdInProcent


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilator(Ventilatie):
    """Onderdeel voor het creëren van luchtcirculatie binnen een open of gesloten ruimte met het oog op het vervangen van vervuilde door zuivere lucht. Voor een gesloten ruimte kan de luchtcirculatie ook zorgen voor afkoeling."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.draairichting = KeuzelijstField(naam="draairichting",
                                             label="draairichting",
                                             lijst=KlVentilatorRichting(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.draairichting",
                                             definition="Geeft aan of de bladen van de ventilator met de wijzers mee of tegen de wijzers in draaien.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan of de bladen van de ventilator met de wijzers mee of tegen de wijzers in draaien."""

        self.gebruik = KeuzelijstField(naam="gebruik",
                                       label="gebruik",
                                       lijst=KlVentilatorGebruik(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.gebruik",
                                       definition="Geeft aan op welke manier de ventilator ingezet wordt.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Geeft aan op welke manier de ventilator ingezet wordt."""

        self.heefDrukverschilmeting = BooleanField(naam="heefDrukverschilmeting",
                                                   label="heeft drukverschilmeting",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.heefDrukverschilmeting",
                                                   definition="Geeft aan of de ventilator uitgerust is met een drukverschilmeters.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Geeft aan of de ventilator uitgerust is met een drukverschilmeters."""

        self.heeftTemperatuurmeting = BooleanField(naam="heeftTemperatuurmeting",
                                                   label="heeft temperatuurmeting",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.heeftTemperatuurmeting",
                                                   definition="Geeft aan of de ventilator uitgerust is met temperatuurmeting.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Geeft aan of de ventilator uitgerust is met temperatuurmeting."""

        self.heeftTrillingsmeting = BooleanField(naam="heeftTrillingsmeting",
                                                 label="heeft trillingsmeting",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.heeftTrillingsmeting",
                                                 definition="Geeft aan of de ventilator uitgerust is met trillingsmeting.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Geeft aan of de ventilator uitgerust is met trillingsmeting."""

        standenField = KwantWrdInProcent()
        standenField.naam = "standen"
        standenField.label = "standen"
        standenField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.standen"
        standenField.definition = "Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden."
        standenField.constraints = ""
        standenField.usagenote = ""
        standenField.deprecated_version = ""
        self.standen = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=standenField)
        """Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden."""
