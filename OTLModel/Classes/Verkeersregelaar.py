# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRegelaarRegelaartype import KlRegelaarRegelaartype
from OTLModel.Datatypes.KlVerkeersregelaarCoordinatiewijze import KlVerkeersregelaarCoordinatiewijze
from OTLModel.Datatypes.KlVerkeersregelaarMerk import KlVerkeersregelaarMerk
from OTLModel.Datatypes.KlVerkeersregelaarModelnaam import KlVerkeersregelaarModelnaam
from OTLModel.Datatypes.KlVerkeersregelaarVoltage import KlVerkeersregelaarVoltage
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersregelaar(AIMNaamObject):
    """Een verkeersregelaar is een programmeerbaar toestel dat de verkeerslichten op kruispunten kan regelen overeenkomstig een goedgekeurd verkeersplan. Een verkeersregelaar is bedoeld om het verkeer verkeersafhankelijk te sturen overeenkomstig het gedetecteerde verkeer. Verkeersregelaars kunnen op zichzelf werken of in groep ingeschakeld worden, zodoende op een gecoördineerde wijze de verkeersstromen te verwerken.
Eveneens detecteert een verkeersregelaar defecte onderdelen, van zichzelf of van aangesloten installaties. Afhankelijk van het soort defect stuurt een verkeersregelaar een code uit opdat het euvel hersteld kan worden. Bij welbepaalde defecten worden verkeerslichten uitgeschakeld of op knipperstand gezet.
Volgende documenten zijn specifiek van toepassing voor verkeersregelaars:
*Koninklijk Besluit van 01.12.1975 (wegcode), aangevuld met alle officiële documenten hierover gepubliceerd;
*NBN EN 12675:2000 (Verkeersregelapparaten - Functionele veiligheidseisen);
*NBN EN 50556:2011 (Signalisatie voor wegverkeer;
*NBN EN 12368:2006 (Verkeersregelinstallaties - Verkeerslantaars);
*NBN EN 50293:2012 (Verkeersregelinstallaties - Elektromagnetische compatibiliteit)"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        coordinatiewijzeField = KeuzelijstField(naam="coordinatiewijze",
                                                label="coördinatiewijze",
                                                lijst=KlVerkeersregelaarCoordinatiewijze(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.coordinatiewijze",
                                                definition="Wijze waarop de coördinatie is opgezet en de eventuele rol die de verkeersregelaar hierin speelt.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.coordinatiewijze = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=coordinatiewijzeField)
        """Wijze waarop de coördinatie is opgezet en de eventuele rol die de verkeersregelaar hierin speelt."""

        externeReferentieField = DtcExterneReferentie()
        externeReferentieField.naam = "externeReferentie"
        externeReferentieField.label = "externe referentie"
        externeReferentieField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.externeReferentie"
        externeReferentieField.definition = "Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."
        externeReferentieField.constraints = ""
        externeReferentieField.usagenote = ""
        externeReferentieField.deprecated_version = ""
        self.externeReferentie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=externeReferentieField)
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""

        self.kabelaansluitschema = DtcDocument()
        """Document met het kabelaansluitschema."""
        self.kabelaansluitschema.naam = "kabelaansluitschema"
        self.kabelaansluitschema.label = "kabelaansluitschema"
        self.kabelaansluitschema.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.kabelaansluitschema"
        self.kabelaansluitschema.definition = "Document met het kabelaansluitschema."
        self.kabelaansluitschema.constraints = ""
        self.kabelaansluitschema.usagenote = ""
        self.kabelaansluitschema.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVerkeersregelaarMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.merk",
                                    definition="Het merk van een verkeersregelaar.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van een verkeersregelaar."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVerkeersregelaarModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.modelnaam",
                                         definition="De modelnaam/product range van een verkeersregelaar.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van een verkeersregelaar."""

        self.programmeertool = StringField(naam="programmeertool",
                                           label="programmeertool",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.programmeertool",
                                           definition="Software waarmee de verkeersregelaar geprogrammeerd kan worden.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Software waarmee de verkeersregelaar geprogrammeerd kan worden."""

        self.regelaartype = KeuzelijstField(naam="regelaartype",
                                            label="regelaartype",
                                            lijst=KlRegelaarRegelaartype(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.regelaartype",
                                            definition="Onderverdeling in type regelaar volgens het maximale aantal aan te sluiten seingroepen en kruispuntdetectoren.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Onderverdeling in type regelaar volgens het maximale aantal aan te sluiten seingroepen en kruispuntdetectoren."""

        self.technischeDocumentatie = DtcDocument()
        """Document met technische informatie."""
        self.technischeDocumentatie.naam = "technischeDocumentatie"
        self.technischeDocumentatie.label = "technische documentatie"
        self.technischeDocumentatie.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.technischeDocumentatie"
        self.technischeDocumentatie.definition = "Document met technische informatie."
        self.technischeDocumentatie.constraints = ""
        self.technischeDocumentatie.usagenote = ""
        self.technischeDocumentatie.deprecated_version = ""

        self.voltageLampen = KeuzelijstField(naam="voltageLampen",
                                             label="voltage lampen",
                                             lijst=KlVerkeersregelaarVoltage(),
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.voltageLampen",
                                             definition="Voltage van de verkeerslichten.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Voltage van de verkeerslichten."""

        self.vplanDatum = DateField(naam="vplanDatum",
                                    label="vplan datum",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.vplanDatum",
                                    definition="Datum van het V-plan.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Datum van het V-plan."""

        self.vplanNummer = StringField(naam="vplanNummer",
                                       label="vplan nummer",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.vplanNummer",
                                       definition="Nummer van het V-plan.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Nummer van het V-plan."""
