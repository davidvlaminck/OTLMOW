from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlTransformatorIsolatiemedium import KlTransformatorIsolatiemedium
from OTLModel.Datatypes.KlTransformatorTrafobeveiliging import KlTransformatorTrafobeveiliging
from OTLModel.Datatypes.KwantWrdInKiloVolt import KwantWrdInKiloVolt
from OTLModel.Datatypes.KwantWrdInKiloVoltAmpere import KwantWrdInKiloVoltAmpere
from OTLModel.Datatypes.KwantWrdInProcent import KwantWrdInProcent
from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Transformator(AIMNaamObject):
    """Elektrische apparatuur, bestaande uit magnetisch gekoppelde spoelen, die instaat voor het transformeren van de voedingsspanning."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isolatiemedium = KeuzelijstField(naam="isolatiemedium",
                                              label="isolatiemedium",
                                              lijst=KlTransformatorIsolatiemedium(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.isolatiemedium",
                                              definition="Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator."""

        self.kortsluitspanning = KwantWrdInProcent()
        """Kortsluitspanning van de transformator (in %)."""
        self.kortsluitspanning.naam = "kortsluitspanning"
        self.kortsluitspanning.label = "kortsluitspanning"
        self.kortsluitspanning.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.kortsluitspanning"
        self.kortsluitspanning.definition = "Kortsluitspanning van de transformator (in %)."
        self.kortsluitspanning.constraints = ""
        self.kortsluitspanning.usagenote = ""
        self.kortsluitspanning.deprecated_version = ""

        self.nominaalVermogen = KwantWrdInKiloVoltAmpere()
        """nominale vermogen van de transformator."""
        self.nominaalVermogen.naam = "nominaalVermogen"
        self.nominaalVermogen.label = "nominaal vermogen"
        self.nominaalVermogen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominaalVermogen"
        self.nominaalVermogen.definition = "nominale vermogen van de transformator."
        self.nominaalVermogen.constraints = ""
        self.nominaalVermogen.usagenote = ""
        self.nominaalVermogen.deprecated_version = ""

        self.nominalePrimaireSpanning = KwantWrdInKiloVolt()
        """Nominale spanning van de primaire wikkeling in kV."""
        self.nominalePrimaireSpanning.naam = "nominalePrimaireSpanning"
        self.nominalePrimaireSpanning.label = "nominale primaire spanning"
        self.nominalePrimaireSpanning.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominalePrimaireSpanning"
        self.nominalePrimaireSpanning.definition = "Nominale spanning van de primaire wikkeling in kV."
        self.nominalePrimaireSpanning.constraints = ""
        self.nominalePrimaireSpanning.usagenote = ""
        self.nominalePrimaireSpanning.deprecated_version = ""

        self.nominaleSecundaireSpanning = KwantWrdInVolt()
        """Nominale spanning van de secundaire wikkeling in V."""
        self.nominaleSecundaireSpanning.naam = "nominaleSecundaireSpanning"
        self.nominaleSecundaireSpanning.label = "nominale secundaire spanning"
        self.nominaleSecundaireSpanning.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominaleSecundaireSpanning"
        self.nominaleSecundaireSpanning.definition = "Nominale spanning van de secundaire wikkeling in V."
        self.nominaleSecundaireSpanning.constraints = ""
        self.nominaleSecundaireSpanning.usagenote = ""
        self.nominaleSecundaireSpanning.deprecated_version = ""

        self.schakelgroep = StringField(naam="schakelgroep",
                                        label="schakelgroep",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.schakelgroep",
                                        definition="Verzameling van 3 schakelcombinaties waarbij de hoofdletter de schakelwijze van de primaire weergeeft, de kleine letter(s) de schakelwijze van de secundaire weergeeft (en eventueel het feit dat het sterpunt naar buiten werd gebracht) en het getal geeft het klokgetal (of het aantal keer dat er 30° faseverschuiving tussen HS- en LS-spanning is) vb Dyn11",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Verzameling van 3 schakelcombinaties waarbij de hoofdletter de schakelwijze van de primaire weergeeft, de kleine letter(s) de schakelwijze van de secundaire weergeeft (en eventueel het feit dat het sterpunt naar buiten werd gebracht) en het getal geeft het klokgetal (of het aantal keer dat er 30° faseverschuiving tussen HS- en LS-spanning is) vb Dyn11"""

        self.typeBeveiliging = KeuzelijstField(naam="typeBeveiliging",
                                               label="type beveiliging",
                                               lijst=KlTransformatorTrafobeveiliging(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.typeBeveiliging",
                                               definition="Type transformatorbeveiliging.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Type transformatorbeveiliging."""
