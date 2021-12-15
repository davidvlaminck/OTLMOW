from OTLModel.Datatypes.DecimalField import DecimalField
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField


class KwantWrdInVolt(KwantWrd):
    """Een kwantitatieve waarde die een getal in volt uitdrukt."""

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

