from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInKiloNewtonPerMeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in  kiloNewton per meter uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerMeter.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in kiloNewton per meter.",
                               constraints='"kN/m"^^cdt:ucumunit',
                               usagenote='"kN/m"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="kN/m")
        """De standaard eenheid bij dit datatype is uitgedrukt in kiloNewton per meter."""

        waardeVeld = DecimalFloatField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerMeter.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKiloNewtonPerMeter",
                         label="Kwantitatieve waarde in kiloNewton per meter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerMeter",
                         definition="Een kwantitatieve waarde die een getal in  kiloNewton per meter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
