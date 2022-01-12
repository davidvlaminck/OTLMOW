# coding=utf-8
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuLichtmastMasthoogte(UnionTypeField):
    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""

    def __init__(self):
        super().__init__(naam="DtuLichtmastMasthoogte",
                         label="Masthoogte",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte",
                         definition="Union datatype om een standaard of afwijkende masthoogte te bepalen.",
                         usagenote="",
                         deprecated_version="")

        field_afwijkendeHoogte = KwantWrdInMeter()
        """De afwijkende hoogte van de mast in meter."""
        field_afwijkendeHoogte.naam = "afwijkendeHoogte"
        field_afwijkendeHoogte.label = "afwijkende hoogte"
        field_afwijkendeHoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte"
        field_afwijkendeHoogte.definition = "De afwijkende hoogte van de mast in meter."
        field_afwijkendeHoogte.constraints = ""
        field_afwijkendeHoogte.usagenote = ""
        field_afwijkendeHoogte.deprecated_version = ""

        field_standaardHoogte = KeuzelijstField(naam="standaardHoogte",
                                                label="standaard hoogte",
                                                lijst=KlLichtmastMasthoogte(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte",
                                                definition="Bepaling van de standaard hoogte van een mast.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Bepaling van de standaard hoogte van een mast."""

        self.fieldsTuple = (field_afwijkendeHoogte, field_standaardHoogte)
