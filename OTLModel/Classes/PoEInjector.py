from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPoEInjectorMerk import KlPoEInjectorMerk
from OTLModel.Datatypes.KlPoEInjectorModelnaam import KlPoEInjectorModelnaam


# Generated with OTLClassCreator
class PoEInjector(AIMNaamObject):
    """Een toestel waarmee stroom/voeding voor een ander toestel over een datakabel kan gestuurd worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlPoEInjectorMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector.merk",
                                    definition="Het merk van de PoE-injector.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de PoE-injector."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlPoEInjectorModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector.modelnaam",
                                         definition="De modelnaam van de PoE-injector.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de PoE-injector."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de PoE-injector."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PoEInjector.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de PoE-injector."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
