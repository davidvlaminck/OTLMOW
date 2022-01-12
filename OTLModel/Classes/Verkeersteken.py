# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerkeerstekenWettelijkeStatus import KlVerkeerstekenWettelijkeStatus
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersteken(AIMObject):
    """Abstracte klasse voor aanwijzingen ten behoeve van de weggebruikers die verbonden wordt aan het aankondigen of opleggen van een bepaalde verkeersmaatregel zoals bepaald in de wegcode."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.adres = DtcAdres()
        """Adres van het verkeersteken."""
        self.adres.naam = "adres"
        self.adres.label = "adres"
        self.adres.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.adres"
        self.adres.definition = "Adres van het verkeersteken."
        self.adres.constraints = ""
        self.adres.usagenote = ""
        self.adres.deprecated_version = ""

        afbeeldingField = DtcDocument()
        afbeeldingField.naam = "afbeelding"
        afbeeldingField.label = "afbeelding"
        afbeeldingField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.afbeelding"
        afbeeldingField.definition = "Foto van het verkeersteken."
        afbeeldingField.constraints = ""
        afbeeldingField.usagenote = ""
        afbeeldingField.deprecated_version = ""
        self.afbeelding = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=afbeeldingField)
        """Foto van het verkeersteken."""

        mobiliteitsMaatregelField = DtcExterneReferentie()
        mobiliteitsMaatregelField.naam = "mobiliteitsMaatregel"
        mobiliteitsMaatregelField.label = "mobiliteitsmaatregel"
        mobiliteitsMaatregelField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.mobiliteitsMaatregel"
        mobiliteitsMaatregelField.definition = "Externe referentie naar een maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren."
        mobiliteitsMaatregelField.constraints = ""
        mobiliteitsMaatregelField.usagenote = ""
        mobiliteitsMaatregelField.deprecated_version = ""
        self.mobiliteitsMaatregel = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=mobiliteitsMaatregelField)
        """Externe referentie naar een maatregel om de beweging en verplaatsing van de weggebruiker op het openbaar domein of privé domein met openbaar karakter te organiseren."""

        self.plaatsbeschrijving = StringField(naam="plaatsbeschrijving",
                                              label="plaatsbeschrijving",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.plaatsbeschrijving",
                                              definition="Tekstuele beschrijving waar het verkeersteken zal komen.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Tekstuele beschrijving waar het verkeersteken zal komen."""

        signalisatieVergunningField = DtcExterneReferentie()
        signalisatieVergunningField.naam = "signalisatieVergunning"
        signalisatieVergunningField.label = "signalisatievergunning"
        signalisatieVergunningField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.signalisatieVergunning"
        signalisatieVergunningField.definition = "Externe referentie naar een vergunning voor het tijdelijk aanbrengen of wijzigen van signalisatie op het openbaar domein of privaat domein met openbaar karakter."
        signalisatieVergunningField.constraints = ""
        signalisatieVergunningField.usagenote = ""
        signalisatieVergunningField.deprecated_version = ""
        self.signalisatieVergunning = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=signalisatieVergunningField)
        """Externe referentie naar een vergunning voor het tijdelijk aanbrengen of wijzigen van signalisatie op het openbaar domein of privaat domein met openbaar karakter."""

        self.variabelOpschrift = StringField(naam="variabelOpschrift",
                                             label="variabel opschrift",
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.variabelOpschrift",
                                             definition="Variabele tekst die op het verkeersbordconcept komt te staan.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Variabele tekst die op het verkeersbordconcept komt te staan."""

        self.wettelijkeStatus = KeuzelijstField(naam="wettelijkeStatus",
                                                label="wettelijke status",
                                                lijst=KlVerkeerstekenWettelijkeStatus(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken.wettelijkeStatus",
                                                definition="Duidt de wettelijke status aan van het verkeersteken.",
                                                constraints="",
                                                usagenote="Bijvoorbeeld: vergund, niet-vergund, in ontwerp",
                                                deprecated_version="")
        """Duidt de wettelijke status aan van het verkeersteken."""
