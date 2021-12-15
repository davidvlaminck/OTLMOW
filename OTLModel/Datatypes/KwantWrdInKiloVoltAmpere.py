from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInKiloVoltAmpere(KwantWrd):
    """Een kwantitatieve waarde die een getal in kilovoltampère uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVoltAmpere.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in kiloVoltAmpere.",
                               constraints='"kVA*"^^cdt:ucumunit',
                               usagenote='"kVA*"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="kVA*")
        """De standaard eenheid bij dit datatype is uitgedrukt in kiloVoltAmpere."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVoltAmpere.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKiloVoltAmpere",
                         label="Kwantitatieve waarde in kilovoltampère",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVoltAmpere",
                         definition="Een kwantitatieve waarde die een getal in kilovoltampère uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
