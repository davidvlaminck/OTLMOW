from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInTon(KwantWrd):
    """Een kwantitatieve waarde die een getal in ton uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInTon.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in ton.",
                                    constraints='"t"^^cdt:ucumunit',
                                    usagenote='"t"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="t")
        """De standaard eenheid bij dit datatype is uitgedrukt in ton."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInTon.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInTon",
                         label="Kwantitatieve waarde in ton",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInTon",
                         definition="Een kwantitatieve waarde die een getal in ton uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
