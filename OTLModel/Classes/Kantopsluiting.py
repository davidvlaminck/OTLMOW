from abc import abstractmethod
from OTLModel.Classes.LijnvormigElement import LijnvormigElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEKantopsluitingKleur import KlLEKantopsluitingKleur
from OTLModel.Datatypes.KlLEKantopsluitingSoort import KlLEKantopsluitingSoort
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator
class Kantopsluiting(LijnvormigElement):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties voor de kantopsluiting."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.isGeprefabriceerd = BooleanField(naam="isGeprefabriceerd",
                                              label="is geprefabriceerd",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.isGeprefabriceerd",
                                              definition="Aanduiding of de kantopsluiting al dan niet is geprefabriceerd.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Aanduiding of de kantopsluiting al dan niet is geprefabriceerd."""

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlLEKantopsluitingKleur(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.kleur",
                                     definition="De kleur van kantopsluiting.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De kleur van kantopsluiting."""

        self.soort = KeuzelijstField(naam="soort",
                                     label="soort",
                                     lijst=KlLEKantopsluitingSoort(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.soort",
                                     definition="De soort van kantopsluiting.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De soort van kantopsluiting."""

        self.totaleLengte = KwantWrdInMeter()
        """De totale lengte van de geplaatste constructie van kantopsluitingen in meter."""
        self.totaleLengte.naam = "totaleLengte"
        self.totaleLengte.label = "lengte"
        self.totaleLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.totaleLengte"
        self.totaleLengte.definition = "De totale lengte van de geplaatste constructie van kantopsluitingen in meter."
        self.totaleLengte.constraints = ""
        self.totaleLengte.usagenote = ""
        self.totaleLengte.deprecated_version = ""
