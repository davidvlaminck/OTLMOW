# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.BijlageVoertuigkering import BijlageVoertuigkering
from OTLModel.Classes.LijnvormigElement import LijnvormigElement
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACMateriaal import KlLEACMateriaal
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class AfschermendeConstructie(BijlageVoertuigkering, LijnvormigElement):
    """Abstracte die een lijn- of puntvormige constructie,geïnstalleerd langs de weg om een kerend vermogen te bieden aan een dwalend voertuig,samenvat."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        BijlageVoertuigkering.__init__(self)
        LijnvormigElement.__init__(self)
        self.certificaathouder = StringField(naam="certificaathouder",
                                             label="certificaathouder",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.certificaathouder",
                                             definition="De houder van het uitvoeringscertificaat.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """De houder van het uitvoeringscertificaat."""

        self.isPermanent = BooleanField(naam="isPermanent",
                                        label="is permanent",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.isPermanent",
                                        definition="Vermelding of de afschermende constructie al dan niet van permanente aard is.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Vermelding of de afschermende constructie al dan niet van permanente aard is."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlLEACMateriaal(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.materiaal",
                                         definition="Het gebruikte materiaal voor de afschermende constructie.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het gebruikte materiaal voor de afschermende constructie."""

        self.metTandGroef = BooleanField(naam="metTandGroef",
                                         label="met tand-groef",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.metTandGroef",
                                         definition="Geeft aan of de afschermende constructie bevestigd is aan de onderliggende laag door middel van een tand-groef aansluiting.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Geeft aan of de afschermende constructie bevestigd is aan de onderliggende laag door middel van een tand-groef aansluiting."""

        self.productidentificatiecode = DtcProductidentificatiecode()
        """De productidentificatiecode voor het bepalen van de code van het gebruikte product (bv. COPRO/BENOR)."""
        self.productidentificatiecode.naam = "productidentificatiecode"
        self.productidentificatiecode.label = "productidentificatiecode"
        self.productidentificatiecode.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.productidentificatiecode"
        self.productidentificatiecode.definition = "De productidentificatiecode voor het bepalen van de code van het gebruikte product (bv. COPRO/BENOR)."
        self.productidentificatiecode.constraints = ""
        self.productidentificatiecode.usagenote = ""
        self.productidentificatiecode.deprecated_version = ""

        self.productnaam = StringField(naam="productnaam",
                                       label="productnaam",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.productnaam",
                                       definition="Dit is de commerciële naam van de afschermende constructie.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Dit is de commerciële naam van de afschermende constructie."""

        self.uitvoeringscertificatie = DtcDocument()
        """Documentatie van het certificaat."""
        self.uitvoeringscertificatie.naam = "uitvoeringscertificatie"
        self.uitvoeringscertificatie.label = "uitvoeringscertificatie"
        self.uitvoeringscertificatie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie.uitvoeringscertificatie"
        self.uitvoeringscertificatie.definition = "Documentatie van het certificaat."
        self.uitvoeringscertificatie.constraints = ""
        self.uitvoeringscertificatie.usagenote = "Bestanden van het type xlsx of pdf."
        self.uitvoeringscertificatie.deprecated_version = ""
