# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Classes.Signalisatie import Signalisatie
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from src.OTLMOW.OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from src.OTLMOW.OTLModel.Datatypes.KlPositieSoort import KlPositieSoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordopstelling(AIMObject, Signalisatie):
    """Het geheel van verticale verkeerssignalisatie die bevestigd is aan één of meerdere draagconstructies op éénzelfde geolocatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.afbeelding',
                                        usagenote='Een bestand dat een afbeelding weergeeft.',
                                        kardinaliteit_max='*',
                                        definition='Grafische weergave van de opstelling geplaatst op het openbaar domein.')

        self._isBotsvriendelijk = OTLAttribuut(field=BooleanField,
                                               naam='isBotsvriendelijk',
                                               label='is botsvriendelijk',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.isBotsvriendelijk',
                                               definition='Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert.')

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.operationeleStatus',
                                                usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                definition='Operationele status van de Verkeersbordopstelling volgens keuzelijst.')

        self._positieTovRijweg = OTLAttribuut(field=KlPositieSoort,
                                              naam='positieTovRijweg',
                                              label='positie ten opzichte van de rijweg',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.positieTovRijweg',
                                              usagenote='Bijvoorbeeld: boven, rechts, links',
                                              definition='De plaatsing van de opstelling ten aanzien van de rijbaan.')

        self._wegSegment = OTLAttribuut(field=DtcExterneReferentie,
                                        naam='wegSegment',
                                        label='wegsegment',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.wegSegment',
                                        usagenote='Dit is niet noodzakelijk het wegsegment waarop het verkeersbord van toepassing is.',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Wegsegment waarbij de verkeersbordopstelling geplaatst is.')

    @property
    def afbeelding(self):
        """Grafische weergave van de opstelling geplaatst op het openbaar domein."""
        return self._afbeelding.waarde

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def isBotsvriendelijk(self):
        """Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert."""
        return self._isBotsvriendelijk.waarde

    @isBotsvriendelijk.setter
    def isBotsvriendelijk(self, value):
        self._isBotsvriendelijk.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self):
        """Operationele status van de Verkeersbordopstelling volgens keuzelijst."""
        return self._operationeleStatus.waarde

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def positieTovRijweg(self):
        """De plaatsing van de opstelling ten aanzien van de rijbaan."""
        return self._positieTovRijweg.waarde

    @positieTovRijweg.setter
    def positieTovRijweg(self, value):
        self._positieTovRijweg.set_waarde(value, owner=self)

    @property
    def wegSegment(self):
        """Wegsegment waarbij de verkeersbordopstelling geplaatst is."""
        return self._wegSegment.waarde

    @wegSegment.setter
    def wegSegment(self, value):
        self._wegSegment.set_waarde(value, owner=self)
