# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInEuro(KwantWrd):
    """Een kwantitatieve waarde die een getal in Euro uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in Euro.",
                                    constraints='"{Euro}"^^cdt:ucumunit',
                                    usagenote='"{Euro}"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="{Euro}")
        """De standaard eenheid bij dit datatype is uitgedrukt in Euro."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInEuro",
                         label="Kwantitatieve waarde in euro",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro",
                         definition="Een kwantitatieve waarde die een getal in Euro uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
