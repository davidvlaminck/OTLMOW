# coding=utf-8
from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWegkantkastType import KlWegkantkastType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegkantkast(Buitenkast):
    """Behuizing in de vorm van een kast typisch gebruikt buiten, langs de kant van de weg."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.elektrischSchema = DtcDocument()
        """Elektrisch aansluitschema van de kast."""
        self.elektrischSchema.naam = "elektrischSchema"
        self.elektrischSchema.label = "elektrisch schema"
        self.elektrischSchema.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.elektrischSchema"
        self.elektrischSchema.definition = "Elektrisch aansluitschema van de kast."
        self.elektrischSchema.constraints = ""
        self.elektrischSchema.usagenote = ""
        self.elektrischSchema.deprecated_version = ""

        self.heeftMaaibescherming = BooleanField(naam="heeftMaaibescherming",
                                                 label="heeft maaibescherming",
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.heeftMaaibescherming",
                                                 definition="Geeft aan of de kast voorzien is van bescherming tegen schade bij het maaien van de omgeving rond de kast.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Geeft aan of de kast voorzien is van bescherming tegen schade bij het maaien van de omgeving rond de kast."""

        mplanField = DtcDocument()
        mplanField.naam = "mplan"
        mplanField.label = "m-plan"
        mplanField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.mplan"
        mplanField.definition = "Mechanisch plan van de volledige installatie. Er wordt één plan toegevoegd per installatie/techniek die op de kast is aangesloten."
        mplanField.constraints = ""
        mplanField.usagenote = "Bestanden van het type dwg of pdf."
        mplanField.deprecated_version = ""
        self.mplan = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=mplanField)
        """Mechanisch plan van de volledige installatie. Er wordt één plan toegevoegd per installatie/techniek die op de kast is aangesloten."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWegkantkastType(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast.type",
                                    definition="Type van de wegkantkast volgens de gangbare types.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Type van de wegkantkast volgens de gangbare types."""
