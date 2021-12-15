from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInPromille(KwantWrd):
    """Een kwantitatieve waarde die een getal in promille uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInPromille.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in promille.",
                               constraints='"‰"^^cdt:ucumunit',
                               usagenote='"‰"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="‰")
        """De standaard eenheid bij dit datatype is uitgedrukt in promille."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInPromille.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInPromille",
                         label="Kwantitatieve waarde in promille",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInPromille",
                         definition="Een kwantitatieve waarde die een getal in promille uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
