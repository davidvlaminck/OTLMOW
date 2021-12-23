from abc import abstractmethod
from OTLModel.Classes.Behuizing import Behuizing
from OTLModel.Datatypes.DtcAfmetingBxlxhInM import DtcAfmetingBxlxhInM
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLModel.Datatypes.KlCabineMerk import KlCabineMerk
from OTLModel.Datatypes.KlCabineModelnaam import KlCabineModelnaam
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Inloopbehuizing(Behuizing):
    """Een behuizing voor het beschermen van technieken en materialen waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.afmeting = DtcAfmetingBxlxhInM()
        """Buitenafmetingen van het bovengronds gedeelte van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."""
        self.afmeting.naam = "afmeting"
        self.afmeting.label = "afmeting"
        self.afmeting.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.afmeting"
        self.afmeting.definition = "Buitenafmetingen van het bovengronds gedeelte van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."
        self.afmeting.constraints = ""
        self.afmeting.usagenote = ""
        self.afmeting.deprecated_version = ""

        self.beschrijvingBereikbaarheid = StringField(naam="beschrijvingBereikbaarheid",
                                                      label="beschrijving bereikbaarheid",
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.beschrijvingBereikbaarheid",
                                                      definition="Een beschrijving van de omgeving van de behuizing in functie van de bereikbaarheid en toegankelijkheid voor werken en toezicht.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        """Een beschrijving van de omgeving van de behuizing in functie van de bereikbaarheid en toegankelijkheid voor werken en toezicht."""

        self.grondplan = DtcDocument()
        """Plattegrond van de behuizing met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""
        self.grondplan.naam = "grondplan"
        self.grondplan.label = "grondplan"
        self.grondplan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.grondplan"
        self.grondplan.definition = "Plattegrond van de behuizing met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."
        self.grondplan.constraints = ""
        self.grondplan.usagenote = ""
        self.grondplan.deprecated_version = ""

        self.inloopbehuizingMateriaal = KeuzelijstField(naam="inloopbehuizingMateriaal",
                                                        label="Cabine materiaal",
                                                        lijst=KlAlgMateriaal(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.inloopbehuizingMateriaal",
                                                        definition="Materiaal waaruit de cabine vervaardigd is zonder buitenafwerking van dak of wanden.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Materiaal waaruit de cabine vervaardigd is zonder buitenafwerking van dak of wanden."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlCabineMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.merk",
                                    definition="De merknaam volgens de fabrikant van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam volgens de fabrikant van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlCabineModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.modelnaam",
                                         definition="Naam waarmee de fabrikant het model identificeert van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Naam waarmee de fabrikant het model identificeert van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."""
