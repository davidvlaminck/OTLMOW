from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInkVARh(KwantWrd):
    """Een kwantitatieve waarde die een getal in KiloVoltAmpereReactiefUur uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInkVARh.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in kVARh.",
                                    constraints='"kVARh"^^cdt:ucumunit',
                                    usagenote='"kVARh"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="kVARh")
        """De standaard eenheid bij dit datatype is uitgedrukt in kVARh."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInkVARh.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInkVARh",
                         label="Kwantitatieve waarde in kVARh",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInkVARh",
                         definition="Een kwantitatieve waarde die een getal in KiloVoltAmpereReactiefUur uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
