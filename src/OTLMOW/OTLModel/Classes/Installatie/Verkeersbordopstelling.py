# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Signalisatie import Signalisatie
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLMOW.OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from OTLMOW.OTLModel.Datatypes.KlPositieSoort import KlPositieSoort
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordopstelling(Signalisatie, AIMObject, PuntGeometrie):
    """Het geheel van verticale verkeerssignalisatie die bevestigd is aan één of meerdere draagconstructies op éénzelfde geolocatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)
        PuntGeometrie.__init__(self)

        self._afbeelding = OTLAttribuut(field=DtcDocument,
                                        naam='afbeelding',
                                        label='afbeelding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.afbeelding',
                                        usagenote='Een bestand dat een afbeelding weergeeft.',
                                        kardinaliteit_max='*',
                                        definition='Grafische weergave van de opstelling geplaatst op het openbaar domein.',
                                        owner=self)

        self._isBotsvriendelijk = OTLAttribuut(field=BooleanField,
                                               naam='isBotsvriendelijk',
                                               label='is botsvriendelijk',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.isBotsvriendelijk',
                                               definition='Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert.',
                                               owner=self)

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.operationeleStatus',
                                                usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                definition='Operationele status van de Verkeersbordopstelling volgens keuzelijst.',
                                                owner=self)

        self._positieTovRijweg = OTLAttribuut(field=KlPositieSoort,
                                              naam='positieTovRijweg',
                                              label='positie ten opzichte van de rijweg',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.positieTovRijweg',
                                              usagenote='Bijvoorbeeld: boven, rechts, links',
                                              definition='De plaatsing van de opstelling ten aanzien van de rijbaan.',
                                              owner=self)

        self._wegSegment = OTLAttribuut(field=DtcExterneReferentie,
                                        naam='wegSegment',
                                        label='wegsegment',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.wegSegment',
                                        usagenote='Dit is niet noodzakelijk het wegsegment waarop het verkeersbord van toepassing is.',
                                        kardinaliteit_min='0',
                                        kardinaliteit_max='*',
                                        definition='Wegsegment waarbij de verkeersbordopstelling geplaatst is.',
                                        owner=self)

    @property
    def afbeelding(self):
        """Grafische weergave van de opstelling geplaatst op het openbaar domein."""
        return self._afbeelding.get_waarde()

    @afbeelding.setter
    def afbeelding(self, value):
        self._afbeelding.set_waarde(value, owner=self)

    @property
    def isBotsvriendelijk(self):
        """Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert."""
        return self._isBotsvriendelijk.get_waarde()

    @isBotsvriendelijk.setter
    def isBotsvriendelijk(self, value):
        self._isBotsvriendelijk.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self):
        """Operationele status van de Verkeersbordopstelling volgens keuzelijst."""
        return self._operationeleStatus.get_waarde()

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def positieTovRijweg(self):
        """De plaatsing van de opstelling ten aanzien van de rijbaan."""
        return self._positieTovRijweg.get_waarde()

    @positieTovRijweg.setter
    def positieTovRijweg(self, value):
        self._positieTovRijweg.set_waarde(value, owner=self)

    @property
    def wegSegment(self):
        """Wegsegment waarbij de verkeersbordopstelling geplaatst is."""
        return self._wegSegment.get_waarde()

    @wegSegment.setter
    def wegSegment(self, value):
        self._wegSegment.set_waarde(value, owner=self)
