from abc import abstractmethod
from OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLModel.Datatypes.KwantWrdInKiloVoltAmpere import KwantWrdInKiloVoltAmpere
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNB(Voedingspunt):
    """Een abstracte die de gegevens van de distributienetbeheerder bevat die bij een aansluiting horen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.aansluitvermogen = KwantWrdInKiloVoltAmpere()
        """Vermogen van de aansluiting."""
        self.aansluitvermogen.naam = "aansluitvermogen"
        self.aansluitvermogen.label = "aansluitvermogen"
        self.aansluitvermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.aansluitvermogen"
        self.aansluitvermogen.definition = "Vermogen van de aansluiting."
        self.aansluitvermogen.constraints = ""
        self.aansluitvermogen.usagenote = ""
        self.aansluitvermogen.deprecated_version = ""

        self.adresVolgensDNB = DtcAdres()
        """Het adres van de aansluiting volgens de distributienetbeheerder."""
        self.adresVolgensDNB.naam = "adresVolgensDNB"
        self.adresVolgensDNB.label = "adres volgens DNB"
        self.adresVolgensDNB.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.adresVolgensDNB"
        self.adresVolgensDNB.definition = "Het adres van de aansluiting volgens de distributienetbeheerder."
        self.adresVolgensDNB.constraints = ""
        self.adresVolgensDNB.usagenote = ""
        self.adresVolgensDNB.deprecated_version = ""

        self.datumEnergieleveringscontract = DateField(naam="datumEnergieleveringscontract",
                                                       label="datum energieleveringscontract",
                                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.datumEnergieleveringscontract",
                                                       definition="De datum waarop het energieleveringscontract afgesloten is.",
                                                       constraints="",
                                                       usagenote="",
                                                       deprecated_version="")
        """De datum waarop het energieleveringscontract afgesloten is."""

        self.datumOprichting = DateField(naam="datumOprichting",
                                         label="datum oprichting",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.datumOprichting",
                                         definition="Datum waarop de DNB het voedingsbord koppelt met het net.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Datum waarop de DNB het voedingsbord koppelt met het net."""

        self.datumStartEnergielevering = DateField(naam="datumStartEnergielevering",
                                                   label="datum start energielevering",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.datumStartEnergielevering",
                                                   definition="De datum waarop de energielevering effectief aanvangt. Dit gebeurt zodra zowel de aansluiting op het DNB-net als het energieleveringscontract in orde zijn.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """De datum waarop de energielevering effectief aanvangt. Dit gebeurt zodra zowel de aansluiting op het DNB-net als het energieleveringscontract in orde zijn."""

        self.eanNummer = StringField(naam="eanNummer",
                                     label="ean nummer",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.eanNummer",
                                     definition="Uniek identificatienummer van de elektrische aansluiting, bestaande uit 18 cijfers.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Uniek identificatienummer van de elektrische aansluiting, bestaande uit 18 cijfers."""

        self.energieleverancier = DtcRechtspersoon()
        """Leverancier van de energie."""
        self.energieleverancier.naam = "energieleverancier"
        self.energieleverancier.label = "energieleverancier"
        self.energieleverancier.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.energieleverancier"
        self.energieleverancier.definition = "Leverancier van de energie."
        self.energieleverancier.constraints = ""
        self.energieleverancier.usagenote = ""
        self.energieleverancier.deprecated_version = ""

        self.netbeheerder = DtcRechtspersoon()
        """Lokale instantie die instaat voor het beheer van het elektriciteitsnet."""
        self.netbeheerder.naam = "netbeheerder"
        self.netbeheerder.label = "netbeheerder"
        self.netbeheerder.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.netbeheerder"
        self.netbeheerder.definition = "Lokale instantie die instaat voor het beheer van het elektriciteitsnet."
        self.netbeheerder.constraints = ""
        self.netbeheerder.usagenote = ""
        self.netbeheerder.deprecated_version = ""

        self.referentieDNB = StringField(naam="referentieDNB",
                                         label="referentie distributienetbeheerder",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.referentieDNB",
                                         definition="De wijze waarop, de referentie waarmee de aansluiting gekend is bij de distributienetbeheerder.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De wijze waarop, de referentie waarmee de aansluiting gekend is bij de distributienetbeheerder."""

        self.risicoAnalyse = DtcDocument()
        """Document met de risicoanalyse."""
        self.risicoAnalyse.naam = "risicoAnalyse"
        self.risicoAnalyse.label = "risico analyse"
        self.risicoAnalyse.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.risicoAnalyse"
        self.risicoAnalyse.definition = "Document met de risicoanalyse."
        self.risicoAnalyse.constraints = ""
        self.risicoAnalyse.usagenote = ""
        self.risicoAnalyse.deprecated_version = ""
