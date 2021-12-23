from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGCMeetMethode import KlGCMeetMethode
from OTLModel.Datatypes.KlLEGCNorm import KlLEGCNorm
from OTLModel.Datatypes.KlLEGCTestType import KlLEGCTestType


# Generated with OTLComplexDatatypeCreator
class DtcGeluidstestRapport(ComplexField):
    """Complex datatype voor een verslag dat de resultaten van de geluidsmetingen weergeeft."""

    def __init__(self):
        super().__init__(naam="DtcGeluidstestRapport",
                         label="Geluidstest rapport",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport",
                         definition="Complex datatype voor een verslag dat de resultaten van de geluidsmetingen weergeeft.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.geluidsabsorptieReflectie = IntegerField(naam="geluidsabsorptieReflectie",
                                                             label="geluidsabsorptie reflectie",
                                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.geluidsabsorptieReflectie",
                                                             definition="De absorptie- of reflectiewaarde van het geluidsscherm als geheel getal.",
                                                             constraints="",
                                                             usagenote="",
                                                             deprecated_version="")
        self.geluidsabsorptieReflectie = self.waarde.geluidsabsorptieReflectie
        """De absorptie- of reflectiewaarde van het geluidsscherm als geheel getal."""

        self.waarde.gemetenWaarde = IntegerField(naam="gemetenWaarde",
                                                 label="gemeten waarde",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.gemetenWaarde",
                                                 definition="De sterkte van het geluid in dB.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        self.gemetenWaarde = self.waarde.gemetenWaarde
        """De sterkte van het geluid in dB."""

        self.waarde.locatieInSitulabo = KeuzelijstField(naam="locatieInSitulabo",
                                                        label="locatie in situlabo",
                                                        lijst=KlGCMeetMethode(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.locatieInSitulabo",
                                                        definition="Locatie waar de geluidstest is uitgevoerd (terrein of labo).",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.locatieInSitulabo = self.waarde.locatieInSitulabo
        """Locatie waar de geluidstest is uitgevoerd (terrein of labo)."""

        self.waarde.luchtgeluidsisolatie = IntegerField(naam="luchtgeluidsisolatie",
                                                        label="luchtgeluidsisolatie",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.luchtgeluidsisolatie",
                                                        definition="De gemeten waarde van het  luchtgeluidsisiolatie van het geluidsscherm.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.luchtgeluidsisolatie = self.waarde.luchtgeluidsisolatie
        """De gemeten waarde van het  luchtgeluidsisiolatie van het geluidsscherm."""

        self.waarde.norm = KeuzelijstField(naam="norm",
                                           label="norm",
                                           lijst=KlLEGCNorm(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.norm",
                                           definition="De proef volgens de beschreven standaard.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.norm = self.waarde.norm
        """De proef volgens de beschreven standaard."""

        testrapportField = DtcDocument()
        testrapportField.naam = "testrapport"
        testrapportField.label = "testrapport"
        testrapportField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.testrapport"
        testrapportField.definition = "Documentbijlage met de resultaten van de test."
        testrapportField.constraints = ""
        testrapportField.usagenote = "Bestanden van het type xlsx of pdf."
        testrapportField.deprecated_version = ""
        self.waarde.testrapport = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=testrapportField)
        self.testrapport = self.waarde.testrapport
        """Documentbijlage met de resultaten van de test."""

        self.waarde.type = KeuzelijstField(naam="type",
                                           label="type",
                                           lijst=KlLEGCTestType(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#DtcGeluidstestRapport.type",
                                           definition="Het type van de test.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.type = self.waarde.type
        """Het type van de test."""
