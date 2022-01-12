# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from OTLModel.Datatypes.KlPositieSoort import KlPositieSoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordopstelling(AIMObject, Signalisatie):
    """Het geheel van verticale verkeerssignalisatie die bevestigd is aan één of meerdere draagconstructies op éénzelfde geolocatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        afbeeldingField = DtcDocument()
        afbeeldingField.naam = "afbeelding"
        afbeeldingField.label = "afbeelding"
        afbeeldingField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.afbeelding"
        afbeeldingField.definition = "Grafische weergave van de opstelling geplaatst op het openbaar domein."
        afbeeldingField.constraints = ""
        afbeeldingField.usagenote = "Een bestand dat een afbeelding weergeeft."
        afbeeldingField.deprecated_version = ""
        self.afbeelding = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=afbeeldingField)
        """Grafische weergave van de opstelling geplaatst op het openbaar domein."""

        self.isBotsvriendelijk = BooleanField(naam="isBotsvriendelijk",
                                              label="is botsvriendelijk",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.isBotsvriendelijk",
                                              definition="Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Een botsvriendelijk obstakel is een voorwerp dat bij aanrijding door een voertuig de letselernst voor de inzittenden reduceert."""

        self.operationeleStatus = KeuzelijstField(naam="operationeleStatus",
                                                  label="operationele status",
                                                  lijst=KlOperationeleStatus(),
                                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.operationeleStatus",
                                                  definition="Operationele status van de Verkeersbordopstelling volgens keuzelijst.",
                                                  constraints="",
                                                  usagenote="Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                  deprecated_version="")
        """Operationele status van de Verkeersbordopstelling volgens keuzelijst."""

        self.positieTovRijweg = KeuzelijstField(naam="positieTovRijweg",
                                                label="positie ten opzichte van de rijweg",
                                                lijst=KlPositieSoort(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.positieTovRijweg",
                                                definition="De plaatsing van de opstelling ten aanzien van de rijbaan.",
                                                constraints="",
                                                usagenote="Bijvoorbeeld: boven, rechts, links",
                                                deprecated_version="")
        """De plaatsing van de opstelling ten aanzien van de rijbaan."""

        wegSegmentField = DtcExterneReferentie()
        wegSegmentField.naam = "wegSegment"
        wegSegmentField.label = "wegsegment"
        wegSegmentField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling.wegSegment"
        wegSegmentField.definition = "Wegsegment waarbij de verkeersbordopstelling geplaatst is."
        wegSegmentField.constraints = ""
        wegSegmentField.usagenote = "Dit is niet noodzakelijk het wegsegment waarop het verkeersbord van toepassing is."
        wegSegmentField.deprecated_version = ""
        self.wegSegment = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=wegSegmentField)
        """Wegsegment waarbij de verkeersbordopstelling geplaatst is."""
