from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPompMerk import KlPompMerk
from OTLModel.Datatypes.KlPompModelnaam import KlPompModelnaam
from OTLModel.Datatypes.KlPompSoort import KlPompSoort
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator
class Pomp(LinkendElement):
    """Een pomp is een werktuig dat water verplaatst door er energie aan af te geven in de vorm van een drukverhoging of snelheidsverhoging."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.binnenDiameter = KwantWrdInMillimeter()
        """Afmeting van de binnenkant van de opening waardoor het opgepompte water loopt."""
        self.binnenDiameter.naam = "binnenDiameter"
        self.binnenDiameter.label = "binnendiameter"
        self.binnenDiameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.binnenDiameter"
        self.binnenDiameter.definition = "Afmeting van de binnenkant van de opening waardoor het opgepompte water loopt."
        self.binnenDiameter.constraints = ""
        self.binnenDiameter.usagenote = ""
        self.binnenDiameter.deprecated_version = ""

        self.buitenDiameter = KwantWrdInMillimeter()
        """Afmeting van de buitenkant van de opening waarlangs het opgepomte water loopt in functie van een aansluiting van een afvoer."""
        self.buitenDiameter.naam = "buitenDiameter"
        self.buitenDiameter.label = "buitendiameter"
        self.buitenDiameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.buitenDiameter"
        self.buitenDiameter.definition = "Afmeting van de buitenkant van de opening waarlangs het opgepomte water loopt in functie van een aansluiting van een afvoer."
        self.buitenDiameter.constraints = ""
        self.buitenDiameter.usagenote = ""
        self.buitenDiameter.deprecated_version = ""

        self.maximaalDebiet = KwantWrdInKubiekeMeter()
        """Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant."""
        self.maximaalDebiet.naam = "maximaalDebiet"
        self.maximaalDebiet.label = "maximaal debiet"
        self.maximaalDebiet.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.maximaalDebiet"
        self.maximaalDebiet.definition = "Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant."
        self.maximaalDebiet.constraints = ""
        self.maximaalDebiet.usagenote = ""
        self.maximaalDebiet.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlPompMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.merk",
                                    definition="De naam van het merk volgens de fabrikant.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De naam van het merk volgens de fabrikant."""

        self.metSoftstarter = BooleanField(naam="metSoftstarter",
                                           label="met softstarter",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.metSoftstarter",
                                           definition="Geeft aan of het toestel voorzien is van een eigen softstarter.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of het toestel voorzien is van een eigen softstarter."""

        self.metTempSensor = BooleanField(naam="metTempSensor",
                                          label="met temperatuur sensor",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.metTempSensor",
                                          definition="Geeft aan of het toestel uitgerust is met een temperatuur sensor in functie van de bewaking van de correcte werking.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Geeft aan of het toestel uitgerust is met een temperatuur sensor in functie van de bewaking van de correcte werking."""

        self.metVochtsensor = BooleanField(naam="metVochtsensor",
                                           label="met vocht sensor",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.metVochtsensor",
                                           definition="Geeft aan of het toestel uitgerust is met een vocht sensor in functie van de bewaking van de correcte werking.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of het toestel uitgerust is met een vocht sensor in functie van de bewaking van de correcte werking."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlPompModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.modelnaam",
                                         definition="Naam van het model van het toestel volgens de fabrikant.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam van het model van het toestel volgens de fabrikant."""

        self.soort = KeuzelijstField(naam="soort",
                                     label="soort",
                                     lijst=KlPompSoort(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.soort",
                                     definition="Bepaalt de aard van de pomp volgens haar werkingsprincipe.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Bepaalt de aard van de pomp volgens haar werkingsprincipe."""

        self.vermogen = KwantWrdInWatt()
        """Elektrisch vermogen van het toestels volgens de specificaties van de fabrikant."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomp.vermogen"
        self.vermogen.definition = "Elektrisch vermogen van het toestels volgens de specificaties van de fabrikant."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
