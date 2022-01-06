# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in vierkante meter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in vierkante meter.",
                                    constraints='"m2"^^cdt:ucumunit',
                                    usagenote='"m2"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="m2")
        """De standaard eenheid bij dit datatype is uitgedrukt in vierkante meter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInVierkanteMeter",
                         label="Kwantitatieve waarde in vierkante meter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter",
                         definition="Een kwantitatieve waarde die een getal in vierkante meter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
