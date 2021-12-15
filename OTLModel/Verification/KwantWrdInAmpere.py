from OTLModel.Datatypes.DecimalField import DecimalField
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField


class KwantWrdInAmpere(KwantWrd):
    """Een kwantitatieve waarde die een getal in ampère uitdrukt."""

    def __init__(self, waarde=None):
        dec = DecimalField(naam="waarde", label="waarde",
                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInAmpere.waarde",
                              definition="Bevat een getal die bij het datatype hoort."
                              , constraints="", usagenote="", deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        standaardEenheid = LiteralField(naam="standaardEenheid", label="standaardEenheid",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid",
                                       definition="De standaard eenheid bij dit datatype is uitgedrukt in Ampere."
                                       , constraints="", usagenote="", deprecated_version="", readonlyValue="A")
        """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""

        super().__init__(naam="KwantWrdInAmpere", label="Kwantitatieve waarde in Ampere",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInAmpere",
                         definition="Een kwantitatieve waarde die een getal in Ampere uitdrukt.", usagenote="",
                         deprecated_version="", waardeVeld=dec, eenheidVeld=standaardEenheid, waarde=waarde)