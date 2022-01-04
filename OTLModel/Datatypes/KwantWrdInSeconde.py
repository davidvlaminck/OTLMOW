from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInSeconde(KwantWrd):
    """Een kwantitatieve waarde die een getal in seconde uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in seconde.",
                                    constraints='"s"^^cdt:ucumunit',
                                    usagenote='"s"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="s")
        """De standaard eenheid bij dit datatype is uitgedrukt in seconde."""

        self.waardeVeld = NonNegIntegerField(naam="waarde",
                                             label="waarde",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde.waarde",
                                             definition="Bevat een getal die bij het datatype hoort.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInSeconde",
                         label="Kwantitatieve waarde in seconde",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde",
                         definition="Een kwantitatieve waarde die een getal in seconde uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
