# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMillimeter(KwantWrd):
    """Een kwantitatieve waarde die een getal in millimeter uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMillimeter.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in millimeter.",
                                    constraints='"mm"^^cdt:ucumunit',
                                    usagenote='"mm"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="mm")
        """De standaard eenheid bij dit datatype is uitgedrukt in millimeter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMillimeter.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMillimeter",
                         label="Kwantitatieve waarde in millimeter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMillimeter",
                         definition="Een kwantitatieve waarde die een getal in millimeter uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
