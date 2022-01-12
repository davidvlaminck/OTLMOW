# coding=utf-8
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtuAfmetingVerkeersbord import DtuAfmetingVerkeersbord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbord(ABC):
    """Abstracte klasse voor borden die een fysieke drager van verkeerstekens kunnen zijn waarvan de betekenis bepaald wordt door een verkeersbordconcept."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.aanzicht = KwantWrdInDecimaleGraden()
        """De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as (het ware noorden). De hoek wordt gemeten in radialen of graden ten opzichte van het noorden in wijzerzin."""
        self.aanzicht.naam = "aanzicht"
        self.aanzicht.label = "aanzicht"
        self.aanzicht.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.aanzicht"
        self.aanzicht.definition = "De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as (het ware noorden). De hoek wordt gemeten in radialen of graden ten opzichte van het noorden in wijzerzin."
        self.aanzicht.constraints = ""
        self.aanzicht.usagenote = "In radialen of graden ten opzichte van het noorden in wijzerzin."
        self.aanzicht.deprecated_version = ""

        afbeeldingField = DtcDocument()
        afbeeldingField.naam = "afbeelding"
        afbeeldingField.label = "afbeelding"
        afbeeldingField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afbeelding"
        afbeeldingField.definition = "De afbeelding van het verkeersbord."
        afbeeldingField.constraints = ""
        afbeeldingField.usagenote = ""
        afbeeldingField.deprecated_version = ""
        self.afbeelding = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=afbeeldingField)
        """De afbeelding van het verkeersbord."""

        self.afmeting = DtuAfmetingVerkeersbord()
        """De afmeting(en) van het verkeersbord."""
        self.afmeting.naam = "afmeting"
        self.afmeting.label = "afmeting"
        self.afmeting.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afmeting"
        self.afmeting.definition = "De afmeting(en) van het verkeersbord."
        self.afmeting.constraints = ""
        self.afmeting.usagenote = ""
        self.afmeting.deprecated_version = ""

        self.fabricagevoorschrift = StringField(naam="fabricagevoorschrift",
                                                label="fabricagevoorschrift",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.fabricagevoorschrift",
                                                definition="Het fabricagevoorschrift op het verkeersbord.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Het fabricagevoorschrift op het verkeersbord."""

        self.operationeleStatus = KeuzelijstField(naam="operationeleStatus",
                                                  label="operationele status",
                                                  lijst=KlOperationeleStatus(),
                                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.operationeleStatus",
                                                  definition="De operationele status van het verkeersbord.",
                                                  constraints="",
                                                  usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                  deprecated_version="")
        """De operationele status van het verkeersbord."""

        self.opstelhoogte = KwantWrdInMeter()
        """Afstand tussen het maaiveld en de onderrand van het bord."""
        self.opstelhoogte.naam = "opstelhoogte"
        self.opstelhoogte.label = "opstelhoogte"
        self.opstelhoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.opstelhoogte"
        self.opstelhoogte.definition = "Afstand tussen het maaiveld en de onderrand van het bord."
        self.opstelhoogte.constraints = ""
        self.opstelhoogte.usagenote = ""
        self.opstelhoogte.deprecated_version = ""
