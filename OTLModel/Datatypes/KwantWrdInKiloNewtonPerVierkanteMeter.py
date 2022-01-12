# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerVierkanteMeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in KiloNewton per vierkante meter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in KiloNewton per vierkante meter.",
                                    constraints='"kN/m2"^^cdt:ucumunit',
                                    usagenote='"kN/m2"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="kN/m2")
        """De standaard eenheid bij dit datatype is uitgedrukt in KiloNewton per vierkante meter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKiloNewtonPerVierkanteMeter",
                         label="Kwantitatieve waarde in kN per vierkante meter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter",
                         definition="Een kwantitatieve waarde die een getal in KiloNewton per vierkante meter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
