# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMilliAmpere(KwantWrd):
    """Een kwantitatieve waarde die een getal in milliampère uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in milliAmpere.",
                                    constraints='"mA"^^cdt:ucumunit',
                                    usagenote='"mA"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="mA")
        """De standaard eenheid bij dit datatype is uitgedrukt in milliAmpere."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMilliAmpere",
                         label="Kwantitatieve waarde in milliampère",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere",
                         definition="Een kwantitatieve waarde die een getal in milliampère uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
