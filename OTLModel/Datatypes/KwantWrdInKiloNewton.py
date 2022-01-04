from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInKiloNewton(KwantWrd):
    """Een kwantitatieve waarde die een getal in KiloNewton uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewton.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in kiloNewton.",
                                    constraints='"kN"^^cdt:ucumunit',
                                    usagenote='"kN"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="kN")
        """De standaard eenheid bij dit datatype is uitgedrukt in kiloNewton."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewton.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInKiloNewton",
                         label="Kwantitatieve waarde in kN",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewton",
                         definition="Een kwantitatieve waarde die een getal in KiloNewton uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
