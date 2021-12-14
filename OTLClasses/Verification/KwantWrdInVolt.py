from ModelGenerator.BaseClasses.DecimalField import DecimalField
from ModelGenerator.BaseClasses.LiteralField import LiteralField
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.KwantWrd import KwantWrd


class KwantWrdInVolt(KwantWrd):
    def __init__(self, waarde=None):
        dec = DecimalField(naam="waarde", label="waarde",
                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde",
                           definition="Bevat een getal die bij het datatype hoort.", constraints="", usagenote="",
                           deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        eenheid = LiteralField(naam="standaardEenheid", label="standaardEenheid",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid",
                                        definition="De standaard eenheid bij dit datatype is uitgedrukt in Volt.", constraints="",
                                        usagenote="", deprecated_version="", readonlyValue="V")

        """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""
        super().__init__(naam="KwantWrdInVolt", label="Kwantitatieve waarde in volt",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt",
                         definition="Een kwantitatieve waarde die een getal in volt uitdrukt.", usagenote="",
                         deprecated_version="", waardeVeld=dec, eenheidVeld=eenheid, waarde=waarde)
