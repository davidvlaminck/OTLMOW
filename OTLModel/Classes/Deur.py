from abc import abstractmethod, ABC
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingBxhInM import DtcAfmetingBxhInM
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDeurFabrikant import KlDeurFabrikant
from OTLModel.Datatypes.KlDeurHandgreeptype import KlDeurHandgreeptype
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLModel.Datatypes.KwantWrdInSeconde import KwantWrdInSeconde
from OTLModel.Datatypes.KwantWrdInUur import KwantWrdInUur


# Generated with OTLClassCreator. To modify: extend, do not edit
class Deur(ABC):
    """Een beweegbaar element ter afsluiting van een ruimte. In een gebouw is een deur meestal bevestigd in een kozijn,dat weer in een muur of wand is aangebracht."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.afmetingDeuropening = DtcAfmetingBxhInM()
        """Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is."""
        self.afmetingDeuropening.naam = "afmetingDeuropening"
        self.afmetingDeuropening.label = "afmeting deuropening"
        self.afmetingDeuropening.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.afmetingDeuropening"
        self.afmetingDeuropening.definition = "Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is."
        self.afmetingDeuropening.constraints = ""
        self.afmetingDeuropening.usagenote = ""
        self.afmetingDeuropening.deprecated_version = ""

        self.brandweerstand = KwantWrdInUur()
        """Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand."""
        self.brandweerstand.naam = "brandweerstand"
        self.brandweerstand.label = "brandweerstand"
        self.brandweerstand.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.brandweerstand"
        self.brandweerstand.definition = "Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand."
        self.brandweerstand.constraints = ""
        self.brandweerstand.usagenote = ""
        self.brandweerstand.deprecated_version = ""

        self.breedte = KwantWrdInMillimeter()
        """De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.breedte"
        self.breedte.definition = "De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.dikte = KwantWrdInMillimeter()
        """De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere."""
        self.dikte.naam = "dikte"
        self.dikte.label = "dikte"
        self.dikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.dikte"
        self.dikte.definition = "De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere."
        self.dikte.constraints = ""
        self.dikte.usagenote = ""
        self.dikte.deprecated_version = ""

        self.fabrikant = KeuzelijstField(naam="fabrikant",
                                         label="fabrikant",
                                         lijst=KlDeurFabrikant(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.fabrikant",
                                         definition="Naam van de producent van de deur.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam van de producent van de deur."""

        self.handgreeptype = KeuzelijstField(naam="handgreeptype",
                                             label="handgreeptype",
                                             lijst=KlDeurHandgreeptype(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.handgreeptype",
                                             definition="Soort greep aan waarmee de deur geopend wordt.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Soort greep aan waarmee de deur geopend wordt."""

        self.heeftDeurcontact = BooleanField(naam="heeftDeurcontact",
                                             label="heeft deurcontact",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.heeftDeurcontact",
                                             definition="Geeft aan of de deur voorzien is van een contact dat bewaakt of de deur open of dicht is.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan of de deur voorzien is van een contact dat bewaakt of de deur open of dicht is."""

        self.hoogte = KwantWrdInMillimeter()
        """De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.hoogte"
        self.hoogte.definition = "De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.isZelfsluitend = BooleanField(naam="isZelfsluitend",
                                           label="is zelfsluitend",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.isZelfsluitend",
                                           definition="Geeft aan of de deur voorzien is van een mechanisme dat er voor zorgt dat de deur sluit zonder tussenkomst van een gebruiker.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of de deur voorzien is van een mechanisme dat er voor zorgt dat de deur sluit zonder tussenkomst van een gebruiker."""

        self.ophangconstructie = DtcDocument()
        """Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt."""
        self.ophangconstructie.naam = "ophangconstructie"
        self.ophangconstructie.label = "ophangconstructie"
        self.ophangconstructie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.ophangconstructie"
        self.ophangconstructie.definition = "Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt."
        self.ophangconstructie.constraints = ""
        self.ophangconstructie.usagenote = ""
        self.ophangconstructie.deprecated_version = ""

        self.sluitingstijd = KwantWrdInSeconde()
        """Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat."""
        self.sluitingstijd.naam = "sluitingstijd"
        self.sluitingstijd.label = "sluitingstijd"
        self.sluitingstijd.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.sluitingstijd"
        self.sluitingstijd.definition = "Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat."
        self.sluitingstijd.constraints = ""
        self.sluitingstijd.usagenote = ""
        self.sluitingstijd.deprecated_version = ""
