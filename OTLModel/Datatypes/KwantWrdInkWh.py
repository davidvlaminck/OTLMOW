from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInkWh(KwantWrd):
    """Een kwantitatieve waarde die een getal in kiloWattUur uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInkWh.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in kiloWattUur.",
                               constraints='"kWh"^^cdt:ucumunit',
                               usagenote='"kWh"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="kWh")
        """De standaard eenheid bij dit datatype is uitgedrukt in kiloWattUur."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInkWh.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInkWh",
                         label="Kwantitatieve waarde in kWh",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInkWh",
                         definition="Een kwantitatieve waarde die een getal in kiloWattUur uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
