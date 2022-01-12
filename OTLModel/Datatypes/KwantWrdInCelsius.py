# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCelsius(KwantWrd):
    """Een kwantitatieve waarde die een getal in graden celsius uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCelsius.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in celsius.",
                                    constraints='"Cel"^^cdt:ucumunit',
                                    usagenote='"Cel"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="Cel")
        """De standaard eenheid bij dit datatype is uitgedrukt in celsius."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCelsius.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInCelsius",
                         label="Kwantitatieve waarde in Celsius",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCelsius",
                         definition="Een kwantitatieve waarde die een getal in graden celsius uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
