# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Behuizing(AIMNaamObject):
    """Abstracte voor alle types van behuizing voor het beschermen van technieken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.adres = DtcAdres()
        """Adres (aanduiding van de locatie) van de behuizing. Indien deze geen adres heeft, wordt net zoals door Fluvius voor cabines, het adres van een nabijgelegen straat genomen."""
        self.adres.naam = "adres"
        self.adres.label = "adres"
        self.adres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing.adres"
        self.adres.definition = "Adres (aanduiding van de locatie) van de behuizing. Indien deze geen adres heeft, wordt net zoals door Fluvius voor cabines, het adres van een nabijgelegen straat genomen."
        self.adres.constraints = ""
        self.adres.usagenote = ""
        self.adres.deprecated_version = ""

        self.risicoanalyse = DtcDocument()
        """Een bestandsbijlage met de risicoanalyse voor werken in en rond een behuizing."""
        self.risicoanalyse.naam = "risicoanalyse"
        self.risicoanalyse.label = "risicoanalyse"
        self.risicoanalyse.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing.risicoanalyse"
        self.risicoanalyse.definition = "Een bestandsbijlage met de risicoanalyse voor werken in en rond een behuizing."
        self.risicoanalyse.constraints = ""
        self.risicoanalyse.usagenote = "De risicoanalyse heeft in eerste instantie betrekking op werken in en rond een behuziing met elektrische installaties. Voor behuizingen met installaties van de distributienetbeheerder wordt de risicoanalyse bestemd voor die beheerder, bewaard in het gelijknamig attribuut van het onderdeel van die beheerder, bv. EnergiemeterDNB."
        self.risicoanalyse.deprecated_version = ""

        self.tabelUitwendigeInvloeden = DtcDocument()
        """Een bestandsbijlage met de ingevulde en actuele tabel uitwendige invloeden zoals vereist door het AREI voor bepaalde elektrische installaties."""
        self.tabelUitwendigeInvloeden.naam = "tabelUitwendigeInvloeden"
        self.tabelUitwendigeInvloeden.label = "tabel uitwendige invloeden"
        self.tabelUitwendigeInvloeden.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing.tabelUitwendigeInvloeden"
        self.tabelUitwendigeInvloeden.definition = "Een bestandsbijlage met de ingevulde en actuele tabel uitwendige invloeden zoals vereist door het AREI voor bepaalde elektrische installaties."
        self.tabelUitwendigeInvloeden.constraints = ""
        self.tabelUitwendigeInvloeden.usagenote = "De tabel is in eerste instantie enkel vereist voor behuizingen die elektrische installaties bevatten die onder het AREI vallen. "
        self.tabelUitwendigeInvloeden.deprecated_version = ""
