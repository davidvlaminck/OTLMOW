from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInGigabyte(KwantWrd):
    """Een kwantitatieve waarde die een getal in gigabyte uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInGigabyte.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in gigabyte.",
                               constraints='"GBy"^^cdt:ucumunit',
                               usagenote='"GBy"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="GBy")
        """De standaard eenheid bij dit datatype is uitgedrukt in gigabyte."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInGigabyte.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInGigabyte",
                         label="Kwantitatieve waarde in gigabyte",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInGigabyte",
                         definition="Een kwantitatieve waarde die een getal in gigabyte uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
