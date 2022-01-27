# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.DtuAfmetingVerkeersbord import DtuAfmetingVerkeersbord
from src.OTLMOW.OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbord(ABC):
    """Abstracte klasse voor borden die een fysieke drager van verkeerstekens kunnen zijn waarvan de betekenis bepaald wordt door een verkeersbordconcept."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._aanzicht = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                      naam='aanzicht',
                                      label='aanzicht',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.aanzicht',
                                      usagenote='In radialen of graden ten opzichte van het noorden in wijzerzin.',
                                      definition='De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as (het ware noorden). De hoek wordt gemeten in radialen of graden ten opzichte van het noorden in wijzerzin.')

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afbeelding',
                                        kardinaliteit_max='*',
                                        definition='De afbeelding van het verkeersbord.')

        self._afmeting = OTLAttribuut(field=DtuAfmetingVerkeersbord,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.afmeting',
                                      definition='De afmeting(en) van het verkeersbord.')

        self._fabricagevoorschrift = OTLAttribuut(field=StringField,
                                                  naam='fabricagevoorschrift',
                                                  label='fabricagevoorschrift',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.fabricagevoorschrift',
                                                  definition='Het fabricagevoorschrift op het verkeersbord.')

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.operationeleStatus',
                                                usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                definition='De operationele status van het verkeersbord.')

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord.opstelhoogte',
                                          definition='Afstand tussen het maaiveld en de onderrand van het bord.')

    @property
    def aanzicht(self):
        """De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as (het ware noorden). De hoek wordt gemeten in radialen of graden ten opzichte van het noorden in wijzerzin."""
        return self._aanzicht.waarde

    @aanzicht.setter
    def aanzicht(self, value):
        self._aanzicht.set_waarde(value, owner=self)

    @property
    def afbeelding(self):
        """De afbeelding van het verkeersbord."""
        return self._afbeelding.waarde

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def afmeting(self):
        """De afmeting(en) van het verkeersbord."""
        return self._afmeting.waarde

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def fabricagevoorschrift(self):
        """Het fabricagevoorschrift op het verkeersbord."""
        return self._fabricagevoorschrift.waarde

    @fabricagevoorschrift.setter
    def fabricagevoorschrift(self, value):
        self._fabricagevoorschrift.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self):
        """De operationele status van het verkeersbord."""
        return self._operationeleStatus.waarde

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self):
        """Afstand tussen het maaiveld en de onderrand van het bord."""
        return self._opstelhoogte.waarde

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)
