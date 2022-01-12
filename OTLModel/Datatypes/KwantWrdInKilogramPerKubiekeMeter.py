# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKilogramPerKubiekeMeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in kilogram per kubieke meter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in kilogram per kubieke meter.",
                                    constraints='"kg/m3"^^cdt:ucumunit',
                                    usagenote='"kg/m3"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="kg/m3")
        """De standaard eenheid bij dit datatype is uitgedrukt in kilogram per kubieke meter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKilogramPerKubiekeMeter",
                         label="Kwantitatieve waarde in kilogram per kubieke meter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter",
                         definition="Een kwantitatieve waarde die een getal in kilogram per kubieke meter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
