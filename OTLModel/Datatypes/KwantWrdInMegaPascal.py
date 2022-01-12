# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMegaPascal(KwantWrd):
    """Een kwantitatieve waarde die een getal in megapascal uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMegaPascal.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in mega pascal.",
                                    constraints='"MPa"^^cdt:ucumunit',
                                    usagenote='"MPa"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="MPa")
        """De standaard eenheid bij dit datatype is uitgedrukt in mega pascal."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMegaPascal.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMegaPascal",
                         label="Kwantitatieve waarde in MPa",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMegaPascal",
                         definition="Een kwantitatieve waarde die een getal in megapascal uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
