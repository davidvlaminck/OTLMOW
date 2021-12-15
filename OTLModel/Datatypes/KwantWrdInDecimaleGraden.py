from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInDecimaleGraden(KwantWrd):
    """Een kwantitatieve waarde die een getal in decimale graden uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInDecimaleGraden.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in decimale graden.",
                               constraints='"deg"^^cdt:ucumunit',
                               usagenote='"deg"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="deg")
        """De standaard eenheid bij dit datatype is uitgedrukt in decimale graden."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInDecimaleGraden.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInDecimaleGraden",
                         label="Kwantitatieve waarde in decimale graden",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInDecimaleGraden",
                         definition="Een kwantitatieve waarde die een getal in decimale graden uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
