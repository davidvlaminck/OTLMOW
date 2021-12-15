from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInAmpere(KwantWrd):
    """Een kwantitatieve waarde die een getal in ampère uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInAmpere.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in ampere.",
                               constraints='"A"^^cdt:ucumunit',
                               usagenote='"A"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="A")
        """De standaard eenheid bij dit datatype is uitgedrukt in ampere."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInAmpere.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInAmpere",
                         label="Kwantitatieve waarde in ampère",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInAmpere",
                         definition="Een kwantitatieve waarde die een getal in ampère uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
