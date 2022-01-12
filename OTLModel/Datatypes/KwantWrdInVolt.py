# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVolt(KwantWrd):
    """Een kwantitatieve waarde die een getal in volt uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in Volt.",
                                    constraints='"V"^^cdt:ucumunit',
                                    usagenote='"V"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="V")
        """De standaard eenheid bij dit datatype is uitgedrukt in Volt."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInVolt",
                         label="Kwantitatieve waarde in volt",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVolt",
                         definition="Een kwantitatieve waarde die een getal in volt uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
