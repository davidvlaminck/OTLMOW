from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInWatt(KwantWrd):
    """Een kwantitatieve waarde die een getal in watt uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in Watt.",
                               constraints='"W"^^cdt:ucumunit',
                               usagenote='"W"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="W")
        """De standaard eenheid bij dit datatype is uitgedrukt in Watt."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInWatt",
                         label="Kwantitatieve waarde in watt",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt",
                         definition="Een kwantitatieve waarde die een getal in watt uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
