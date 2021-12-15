from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInProcent(KwantWrd):
    """Een kwantitatieve waarde die een getal in procent uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInProcent.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in procent.",
                               constraints='"%"^^cdt:ucumunit',
                               usagenote='"%"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="%")
        """De standaard eenheid bij dit datatype is uitgedrukt in procent."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInProcent.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInProcent",
                         label="Kwantitatieve waarde in procent",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInProcent",
                         definition="Een kwantitatieve waarde die een getal in procent uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
