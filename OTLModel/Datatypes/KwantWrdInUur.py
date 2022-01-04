from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInUur(KwantWrd):
    """Een kwantitatieve waarde die een getal in uur uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInUur.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in uur.",
                                    constraints='"h"^^cdt:ucumunit',
                                    usagenote='"h"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="h")
        """De standaard eenheid bij dit datatype is uitgedrukt in uur."""

        self.waardeVeld = NonNegIntegerField(naam="waarde",
                                             label="waarde",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInUur.waarde",
                                             definition="Bevat een getal die bij het datatype hoort.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInUur",
                         label="Kwantitatieve waarde in uur",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInUur",
                         definition="Een kwantitatieve waarde die een getal in uur uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
