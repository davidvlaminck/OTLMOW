# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in kubieke meter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in kubieke meter.",
                                    constraints='"m3"^^cdt:ucumunit',
                                    usagenote='"m3"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="m3")
        """De standaard eenheid bij dit datatype is uitgedrukt in kubieke meter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKubiekeMeter",
                         label="Kwantitatieve waarde in kubieke meter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter",
                         definition="Een kwantitatieve waarde die een getal in kubieke meter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
