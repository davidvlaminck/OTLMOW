# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCentimeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in centimeter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in centimeter.",
                                    constraints='"cm"^^cdt:ucumunit',
                                    usagenote='"cm"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="cm")
        """De standaard eenheid bij dit datatype is uitgedrukt in centimeter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInCentimeter",
                         label="Kwantitatieve waarde in centimeter",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter",
                         definition="Een kwantitatieve waarde die een getal in centimeter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
