from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.NonNegIntField import NonNegIntField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInMinuut(KwantWrd):
    """Een kwantitatieve waarde die een getal in minuten uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMinuut.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in minuten.",
                               constraints='"min"^^cdt:ucumunit',
                               usagenote='"min"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="min")
        """De standaard eenheid bij dit datatype is uitgedrukt in minuten."""

        waardeVeld = NonNegIntField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMinuut.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMinuut",
                         label="Kwantitatieve waarde in minuten",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMinuut",
                         definition="Een kwantitatieve waarde die een getal in minuten uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
