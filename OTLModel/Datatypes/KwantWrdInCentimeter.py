from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInCentimeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in centimeter uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in centimeter.",
                               constraints='"cm"^^cdt:ucumunit',
                               usagenote='"cm"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="cm")
        """De standaard eenheid bij dit datatype is uitgedrukt in centimeter."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInCentimeter",
                         label="Kwantitatieve waarde in centimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter",
                         definition="Een kwantitatieve waarde die een getal in centimeter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
