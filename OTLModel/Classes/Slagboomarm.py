# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSlagboomarmMerk import KlSlagboomarmMerk
from OTLModel.Datatypes.KlSlagboomarmModelnaam import KlSlagboomarmModelnaam
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboomarm(AIMObject):
    """De bewegende arm van een slagboominstallatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.lengteBoom = KwantWrdInMeter()
        """De lengte van de slagboomarm uitgedrukt in meter."""
        self.lengteBoom.naam = "lengteBoom"
        self.lengteBoom.label = "lengte boom"
        self.lengteBoom.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.lengteBoom"
        self.lengteBoom.definition = "De lengte van de slagboomarm uitgedrukt in meter."
        self.lengteBoom.constraints = ""
        self.lengteBoom.usagenote = ""
        self.lengteBoom.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlSlagboomarmMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.merk",
                                    definition="Het merk van de slagboom installatie.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de slagboom installatie."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlSlagboomarmModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.modelnaam",
                                         definition="Naam van het model van de slagboominstallatie.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam van het model van de slagboominstallatie."""

        self.technischeFiche = DtcDocument()
        """Technische fiche van de slagboominstallatie."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.technischeFiche"
        self.technischeFiche.definition = "Technische fiche van de slagboominstallatie."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
