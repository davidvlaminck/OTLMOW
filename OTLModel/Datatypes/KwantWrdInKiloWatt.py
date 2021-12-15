from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInKiloWatt(KwantWrd):
    """Een kwantitatieve waarde die een getal in kilowatt uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloWatt.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in kilowatt.",
                               constraints='"kW"^^cdt:ucumunit',
                               usagenote='"kW"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="kW")
        """De standaard eenheid bij dit datatype is uitgedrukt in kilowatt."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloWatt.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKiloWatt",
                         label="Kwantitatieve waarde in kilowatt",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloWatt",
                         definition="Een kwantitatieve waarde die een getal in kilowatt uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
