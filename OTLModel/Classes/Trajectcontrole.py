# coding=utf-8
from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgRijrichting import KlAlgRijrichting
from OTLModel.Datatypes.KlAlgSnelheidsregime import KlAlgSnelheidsregime


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trajectcontrole(NaampadObject):
    """Trajectcontrole is een systeem waarbij de gemiddelde snelheid over een langere afstand wordt gemeten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.attest = DtcDocument()
        """Het ijkingsattest van de trajectcontrole in zijn geheel."""
        self.attest.naam = "attest"
        self.attest.label = "attest"
        self.attest.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.attest"
        self.attest.definition = "Het ijkingsattest van de trajectcontrole in zijn geheel."
        self.attest.constraints = ""
        self.attest.usagenote = "Bestanden van het type pdf."
        self.attest.deprecated_version = ""

        self.nTP = BooleanField(naam="nTP",
                                label="NTP",
                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.nTP",
                                definition="Aanduiding of het systeem voor zijn tijdsaanduiding gebruik maakt van NTP.",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """Aanduiding of het systeem voor zijn tijdsaanduiding gebruik maakt van NTP."""

        self.rijrichting = KeuzelijstField(naam="rijrichting",
                                           label="rijrichting",
                                           lijst=KlAlgRijrichting(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.rijrichting",
                                           definition="De rijrichting van de voertuigen die gecontroleerd worden.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De rijrichting van de voertuigen die gecontroleerd worden."""

        self.snelheidsregime = KeuzelijstField(naam="snelheidsregime",
                                               label="snelheidsregime",
                                               lijst=KlAlgSnelheidsregime(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.snelheidsregime",
                                               definition="Het snelheidsregime waarop de voertuigen worden gecontroleerd.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Het snelheidsregime waarop de voertuigen worden gecontroleerd."""
