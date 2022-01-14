# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKilogram(KwantWrd):
    """Een kwantitatieve waarde die een getal in kilogram uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaardeenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogram.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in kilogram.",
                                    constraints='"kg"^^cdt:ucumunit',
                                    usagenote='"kg"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="kg")
        """De standaard eenheid bij dit datatype is uitgedrukt in kilogram."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogram.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKilogram",
                         label="Kwantitatieve waarde in kilogram",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogram",
                         definition="Een kwantitatieve waarde die een getal in kilogram uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
