from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInMilliAmpere(KwantWrd):
    """Een kwantitatieve waarde die een getal in milliampère uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in milliAmpere.",
                               constraints='"mA"^^cdt:ucumunit',
                               usagenote='"mA"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="mA")
        """De standaard eenheid bij dit datatype is uitgedrukt in milliAmpere."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMilliAmpere",
                         label="Kwantitatieve waarde in milliampère",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere",
                         definition="Een kwantitatieve waarde die een getal in milliampère uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
