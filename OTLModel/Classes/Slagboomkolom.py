# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSlagboomkolomMerk import KlSlagboomkolomMerk
from OTLModel.Datatypes.KlSlagboomkolomModelnaam import KlSlagboomkolomModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboomkolom(AIMObject):
    """De koker van een slagboominstallatie die de motor bevat en waaraan de slagboomarm bevestigd is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingen = DtcAfmetingBxlxhInMm()
        """De afmetingen van de slagboomkolom."""
        self.afmetingen.naam = "afmetingen"
        self.afmetingen.label = "afmetingen"
        self.afmetingen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.afmetingen"
        self.afmetingen.definition = "De afmetingen van de slagboomkolom."
        self.afmetingen.constraints = ""
        self.afmetingen.usagenote = ""
        self.afmetingen.deprecated_version = ""

        self.isPivoterend = BooleanField(naam="isPivoterend",
                                         label="is pivoterend",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.isPivoterend",
                                         definition="Attribuut waarmee kan aangegeven worden of de koker van de slagboominstallatie al dan niet pivoteert.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Attribuut waarmee kan aangegeven worden of de koker van de slagboominstallatie al dan niet pivoteert."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlSlagboomkolomMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.merk",
                                    definition="Het merk van de slagboom installatie.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de slagboom installatie."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlSlagboomkolomModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.modelnaam",
                                         definition="Naam van het model van de slagboominstallatie.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam van het model van de slagboominstallatie."""

        self.technischeFiche = DtcDocument()
        """Technische fiche van de slagboominstallatie."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.technischeFiche"
        self.technischeFiche.definition = "Technische fiche van de slagboominstallatie."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
