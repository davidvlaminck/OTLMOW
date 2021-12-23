from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBoomConditiebeoordeling import KlBoomConditiebeoordeling
from OTLModel.Datatypes.KlBoomConditiewaarde import KlBoomConditiewaarde
from OTLModel.Datatypes.KlBoomConflicten import KlBoomConflicten
from OTLModel.Datatypes.KlBoomGebreken import KlBoomGebreken
from OTLModel.Datatypes.KlBoomOnderhoudstoestand import KlBoomOnderhoudstoestand
from OTLModel.Datatypes.KlBoomPlantwijzewaarde import KlBoomPlantwijzewaarde
from OTLModel.Datatypes.KlBoomStandplaatswaarde import KlBoomStandplaatswaarde
from OTLModel.Datatypes.KlBoomtoestandMeerwaardefactor import KlBoomtoestandMeerwaardefactor
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInEuro import KwantWrdInEuro


# Generated with OTLClassCreator
class ProefBoomtoestand(Proef):
    """De toestand met waarnemingen per inspectie van een boom."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.basiswaarde = KwantWrdInEuro()
        """Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."""
        self.basiswaarde.naam = "basiswaarde"
        self.basiswaarde.label = "rapportage onderzoek"
        self.basiswaarde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.basiswaarde"
        self.basiswaarde.definition = "Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."
        self.basiswaarde.constraints = ""
        self.basiswaarde.usagenote = ""
        self.basiswaarde.deprecated_version = ""

        self.conditiebeoordeling = KeuzelijstField(naam="conditiebeoordeling",
                                                   label="conditiebeoordeling",
                                                   lijst=KlBoomConditiebeoordeling(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conditiebeoordeling",
                                                   definition="De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout."""

        self.conditiewaarde = KeuzelijstField(naam="conditiewaarde",
                                              label="conditiewaarde",
                                              lijst=KlBoomConditiewaarde(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conditiewaarde",
                                              definition="Een coëfficiënt die iets vertelt over de gezondheidstoestand (vitaliteit, conditie) en de levensverwachting van een boom.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Een coëfficiënt die iets vertelt over de gezondheidstoestand (vitaliteit, conditie) en de levensverwachting van een boom."""

        self.conflicten = KeuzelijstField(naam="conflicten",
                                          label="conflicten",
                                          lijst=KlBoomConflicten(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conflicten",
                                          definition="Mogelijke standplaatsconflicten die de condities of structuur van de boom negatief kunnen beïnvloeden.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Mogelijke standplaatsconflicten die de condities of structuur van de boom negatief kunnen beïnvloeden."""

        gebrekenField = KeuzelijstField(naam="gebreken",
                                        label="gebreken",
                                        lijst=KlBoomGebreken(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.gebreken",
                                        definition="Een visueel defect aan een boom wat dient gemonitord te worden.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        self.gebreken = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=gebrekenField)
        """Een visueel defect aan een boom wat dient gemonitord te worden."""

        self.krooninspectie = DtcDocument()
        """Controle van gebrekssymptomen in de kroon."""
        self.krooninspectie.naam = "krooninspectie"
        self.krooninspectie.label = "krooninspectie"
        self.krooninspectie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.krooninspectie"
        self.krooninspectie.definition = "Controle van gebrekssymptomen in de kroon."
        self.krooninspectie.constraints = ""
        self.krooninspectie.usagenote = ""
        self.krooninspectie.deprecated_version = ""

        self.meerwaarde = KeuzelijstField(naam="meerwaarde",
                                          label="meerwaarde",
                                          lijst=KlBoomtoestandMeerwaardefactor(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.meerwaarde",
                                          definition="Mogelijkheid om de boom een waarde toe te kennen op basis van hun uitzonderlijke ecologische of erfgoedwaarde .",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Mogelijkheid om de boom een waarde toe te kennen op basis van hun uitzonderlijke ecologische of erfgoedwaarde ."""

        self.onderhoudstoestand = KeuzelijstField(naam="onderhoudstoestand",
                                                  label="onderhoudstoestand",
                                                  lijst=KlBoomOnderhoudstoestand(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.onderhoudstoestand",
                                                  definition="De toestand van een boom die de eventuele snoeiachterstand aangeeft.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """De toestand van een boom die de eventuele snoeiachterstand aangeeft."""

        self.onderzoekVisueleBoomcontrole = DtcDocument()
        """Visueel bepalen van de veiligheid en conditie van een boom."""
        self.onderzoekVisueleBoomcontrole.naam = "onderzoekVisueleBoomcontrole"
        self.onderzoekVisueleBoomcontrole.label = "Onderzoek visuele boomcontrole"
        self.onderzoekVisueleBoomcontrole.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.onderzoekVisueleBoomcontrole"
        self.onderzoekVisueleBoomcontrole.definition = "Visueel bepalen van de veiligheid en conditie van een boom."
        self.onderzoekVisueleBoomcontrole.constraints = ""
        self.onderzoekVisueleBoomcontrole.usagenote = ""
        self.onderzoekVisueleBoomcontrole.deprecated_version = ""

        self.plantwijzewaarde = KeuzelijstField(naam="plantwijzewaarde",
                                                label="plantwijzewaarde",
                                                lijst=KlBoomPlantwijzewaarde(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.plantwijzewaarde",
                                                definition="Een factor die de ontwikkeling van het uiterlijk (de habitus) van een boom relateert met de manier waarop hij geplant wordt.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Een factor die de ontwikkeling van het uiterlijk (de habitus) van een boom relateert met de manier waarop hij geplant wordt."""

        self.rapportageOnderzoek = DtcDocument()
        """Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."""
        self.rapportageOnderzoek.naam = "rapportageOnderzoek"
        self.rapportageOnderzoek.label = "rapportage onderzoek"
        self.rapportageOnderzoek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.rapportageOnderzoek"
        self.rapportageOnderzoek.definition = "Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."
        self.rapportageOnderzoek.constraints = ""
        self.rapportageOnderzoek.usagenote = ""
        self.rapportageOnderzoek.deprecated_version = ""

        self.soortwaarde = DecimalFloatField(naam="soortwaarde",
                                             label="soortwaarde",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.soortwaarde",
                                             definition="Geeft voor een bepaalde boomsoort of -variëteit de verhouding weer tussen de prijs per cm² van die soort en de eenheidsprijs.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft voor een bepaalde boomsoort of -variëteit de verhouding weer tussen de prijs per cm² van die soort en de eenheidsprijs."""

        self.stamomtrek = KwantWrdInCentimeter()
        """Omtrek van de stam van de boom in cm, gemeten op 1 meter boven de grond."""
        self.stamomtrek.naam = "stamomtrek"
        self.stamomtrek.label = "stamomtrek"
        self.stamomtrek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.stamomtrek"
        self.stamomtrek.definition = "Omtrek van de stam van de boom in cm, gemeten op 1 meter boven de grond."
        self.stamomtrek.constraints = ""
        self.stamomtrek.usagenote = ""
        self.stamomtrek.deprecated_version = ""

        self.standplaatswaarde = KeuzelijstField(naam="standplaatswaarde",
                                                 label="standplaatswaarde",
                                                 lijst=KlBoomStandplaatswaarde(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.standplaatswaarde",
                                                 definition="De waarde van de boom afhankelijk van de bebouwingsdichtheid en de aanplantingsmogelijkheden rondom en voor de boom.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De waarde van de boom afhankelijk van de bebouwingsdichtheid en de aanplantingsmogelijkheden rondom en voor de boom."""

        self.tijdstempelBoomtoestand = DateTimeField(naam="tijdstempelBoomtoestand",
                                                     label="tijdstempel boomtoestand",
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.tijdstempelBoomtoestand",
                                                     definition="Datum van laatste snoeibeurt.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        """Datum van laatste snoeibeurt."""

        self.uitgebreidPlaatsonderzoek = DtcDocument()
        """Grondige beoordeling van de textuur en structuur van de bodem, met als doel een voorstel tot conditieverbeterende maatregelen."""
        self.uitgebreidPlaatsonderzoek.naam = "uitgebreidPlaatsonderzoek"
        self.uitgebreidPlaatsonderzoek.label = "uitgebreid plaatsonderzoek"
        self.uitgebreidPlaatsonderzoek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.uitgebreidPlaatsonderzoek"
        self.uitgebreidPlaatsonderzoek.definition = "Grondige beoordeling van de textuur en structuur van de bodem, met als doel een voorstel tot conditieverbeterende maatregelen."
        self.uitgebreidPlaatsonderzoek.constraints = ""
        self.uitgebreidPlaatsonderzoek.usagenote = ""
        self.uitgebreidPlaatsonderzoek.deprecated_version = ""

        self.wortelonderzoek = DtcDocument()
        """Bepalen van de kwaliteit van de wortels (bv. aantasting door schimmels) of het bepalen van de reikwijdte van de wortels (bv. om een wortelbeschermingszone op te zetten in de buurt van werken van de  bomen)."""
        self.wortelonderzoek.naam = "wortelonderzoek"
        self.wortelonderzoek.label = "Wortelonderzoek"
        self.wortelonderzoek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.wortelonderzoek"
        self.wortelonderzoek.definition = "Bepalen van de kwaliteit van de wortels (bv. aantasting door schimmels) of het bepalen van de reikwijdte van de wortels (bv. om een wortelbeschermingszone op te zetten in de buurt van werken van de  bomen)."
        self.wortelonderzoek.constraints = ""
        self.wortelonderzoek.usagenote = ""
        self.wortelonderzoek.deprecated_version = ""
