from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHSBeveiligingscelHoogspanningszekering import KlHSBeveiligingscelHoogspanningszekering
from OTLModel.Datatypes.KlHSBeveiligingscelMerk import KlHSBeveiligingscelMerk
from OTLModel.Datatypes.KlHSBeveiligingscelModelnaam import KlHSBeveiligingscelModelnaam
from OTLModel.Datatypes.KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar import KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar
from OTLModel.Datatypes.KlHSBeveiligingscelSchakelmateriaalKlasse import KlHSBeveiligingscelSchakelmateriaalKlasse
from OTLModel.Datatypes.KlHSBeveiligingscelSchakelmateriaalType import KlHSBeveiligingscelSchakelmateriaalType
from OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere
from OTLModel.Datatypes.KwantWrdInJaar import KwantWrdInJaar
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class HSBeveiligingscel(AIMNaamObject):
    """Cel die de hoogspanningsschakelinrichting omvat. Hieronder vallen onder meer de lastscheidingsschakelaar, smeltveiligheden, aardingsschakelaar,..."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.elektrischSchema = DtcDocument()
        """Elektrisch aansluitschema van de HS beveiligingscel."""
        self.elektrischSchema.naam = "elektrischSchema"
        self.elektrischSchema.label = "elektrisch schema"
        self.elektrischSchema.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.elektrischSchema"
        self.elektrischSchema.definition = "Elektrisch aansluitschema van de HS beveiligingscel."
        self.elektrischSchema.constraints = ""
        self.elektrischSchema.usagenote = ""
        self.elektrischSchema.deprecated_version = ""

        self.heeftreserveZekering = BooleanField(naam="heeftreserveZekering",
                                                 label="heeft reserve zekering",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.heeftreserveZekering",
                                                 definition="Is er een reserve zekering aanwezig?",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Is er een reserve zekering aanwezig?"""

        self.hoogspanningszekering = KeuzelijstField(naam="hoogspanningszekering",
                                                     label="hoogspanningszekering",
                                                     lijst=KlHSBeveiligingscelHoogspanningszekering(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.hoogspanningszekering",
                                                     definition="Waarde van de hoogspanningszekering.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        """Waarde van de hoogspanningszekering."""

        self.keuringsfrequentie = KwantWrdInJaar()
        """Frequentie (in jaar) waarmee de installatie moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."""
        self.keuringsfrequentie.naam = "keuringsfrequentie"
        self.keuringsfrequentie.label = "keuringsfrequentie"
        self.keuringsfrequentie.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.keuringsfrequentie"
        self.keuringsfrequentie.definition = "Frequentie (in jaar) waarmee de installatie moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."
        self.keuringsfrequentie.constraints = ""
        self.keuringsfrequentie.usagenote = ""
        self.keuringsfrequentie.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlHSBeveiligingscelMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.merk",
                                    definition="Merk van de HS beveiligingscel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van de HS beveiligingscel."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlHSBeveiligingscelModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.modelnaam",
                                         definition="Modelnaam van de HS beveiligingscel.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van de HS beveiligingscel."""

        self.overstroombeveiligingInstelwaarde = KwantWrdInAmpere()
        """Instelwaarde van de overstroombeveiliging."""
        self.overstroombeveiligingInstelwaarde.naam = "overstroombeveiligingInstelwaarde"
        self.overstroombeveiligingInstelwaarde.label = "overstroombeveiliging instelwaarde"
        self.overstroombeveiligingInstelwaarde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingInstelwaarde"
        self.overstroombeveiligingInstelwaarde.definition = "Instelwaarde van de overstroombeveiliging."
        self.overstroombeveiligingInstelwaarde.constraints = ""
        self.overstroombeveiligingInstelwaarde.usagenote = ""
        self.overstroombeveiligingInstelwaarde.deprecated_version = ""

        self.overstroombeveiligingType = StringField(naam="overstroombeveiligingType",
                                                     label="overstroombeveiliging type",
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingType",
                                                     definition="Type overstroombeveiliging.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        """Type overstroombeveiliging."""

        self.overstroombeveiligingVermogenschakelaar = KeuzelijstField(naam="overstroombeveiligingVermogenschakelaar",
                                                                       label="overstroombeveiliging vermogenschakelaar",
                                                                       lijst=KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar(),
                                                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingVermogenschakelaar",
                                                                       definition="Directe of indirecte overstroombeveiliging van de vermogenschakelaar.",
                                                                       constraints="",
                                                                       usagenote="",
                                                                       deprecated_version="")
        """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""

        self.schakelmateriaalKlasse = KeuzelijstField(naam="schakelmateriaalKlasse",
                                                      label="schakelmateriaal klasse",
                                                      lijst=KlHSBeveiligingscelSchakelmateriaalKlasse(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.schakelmateriaalKlasse",
                                                      definition="Klasse van het schakelmateriaal volgens Synergrid.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        """Klasse van het schakelmateriaal volgens Synergrid."""

        self.schakelmateriaalType = KeuzelijstField(naam="schakelmateriaalType",
                                                    label="schakelmateriaal type",
                                                    lijst=KlHSBeveiligingscelSchakelmateriaalType(),
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.schakelmateriaalType",
                                                    definition="Type van schakelmateriaal.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Type van schakelmateriaal."""
