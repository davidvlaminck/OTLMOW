# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeCentimeterPerMeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in kubieke centimeter per meter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in kubieke centimeter per meter.",
                                    constraints='"cm3/m"^^cdt:ucumunit',
                                    usagenote='"cm3/m"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="cm3/m")
        """De standaard eenheid bij dit datatype is uitgedrukt in kubieke centimeter per meter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKubiekeCentimeterPerMeter",
                         label="Kwantitatieve waarde in kubieke centimeter per meter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter",
                         definition="Een kwantitatieve waarde die een getal in kubieke centimeter per meter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
