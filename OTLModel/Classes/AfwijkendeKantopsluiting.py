# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.Kantopsluiting import Kantopsluiting
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfwijkendeKantopsluiting(Kantopsluiting):
    """Abstracte voor een kantopsluiting die niet voldoet aan een bepaalde standaard."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInCentimeter()
        """De breedte van de afwijkende kantopsluiting in centimeter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.breedte"
        self.breedte.definition = "De breedte van de afwijkende kantopsluiting in centimeter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.dikte = KwantWrdInCentimeter()
        """De dikte van de afwijkende kantopsluiting in centimeter."""
        self.dikte.naam = "dikte"
        self.dikte.label = "dikte"
        self.dikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.dikte"
        self.dikte.definition = "De dikte van de afwijkende kantopsluiting in centimeter."
        self.dikte.constraints = ""
        self.dikte.usagenote = ""
        self.dikte.deprecated_version = ""

        self.heeftOppervlaktebehandeling = BooleanField(naam="heeftOppervlaktebehandeling",
                                                        label="heeft oppervlaktebehandeling",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.heeftOppervlaktebehandeling",
                                                        definition="Aanduiding of er een oppervlaktebehandeling is uitgevoerd op de afwijkende kantopsluiting.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Aanduiding of er een oppervlaktebehandeling is uitgevoerd op de afwijkende kantopsluiting."""

        technischeFicheAfwijkingField = DtcDocument()
        technischeFicheAfwijkingField.naam = "technischeFicheAfwijking"
        technischeFicheAfwijkingField.label = "technische fiche afwijking"
        technischeFicheAfwijkingField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.technischeFicheAfwijking"
        technischeFicheAfwijkingField.definition = "De technische fiche van de afwijkende kantopsluiting."
        technischeFicheAfwijkingField.constraints = ""
        technischeFicheAfwijkingField.usagenote = "Bestanden van het type xlsx of pdf."
        technischeFicheAfwijkingField.deprecated_version = ""
        self.technischeFicheAfwijking = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheAfwijkingField)
        """De technische fiche van de afwijkende kantopsluiting."""
