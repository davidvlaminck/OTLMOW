from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.NonNegIntField import NonNegIntField


# Generated with OTLPrimitiveDatatypeCreator
class KwantWrdInMaand(KwantWrd):
    """Een kwantitatieve waarde die een getal in aantal maanden uitdrukt."""

    def __init__(self, waarde=None):
        eenheid = LiteralField(naam="standaardEenheid",
                               label="standaard eenheid",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMaand.standaardEenheid",
                               definition="De standaard eenheid bij dit datatype is uitgedrukt in maand.",
                               constraints='"mo"^^cdt:ucumunit',
                               usagenote='"mo"^^cdt:ucumunit',
                               deprecated_version="",
                               readonlyValue="mo")
        """De standaard eenheid bij dit datatype is uitgedrukt in maand."""

        waardeVeld = NonNegIntField(naam="waarde",
                                       label="waarde",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMaand.waarde",
                                       definition="Bevat een getal die bij het datatype hoort.",
                                       constraints='',
                                       usagenote='',
                                       deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMaand",
                         label="Kwantitatieve waarde in maand",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMaand",
                         definition="Een kwantitatieve waarde die een getal in aantal maanden uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=waardeVeld,
                         eenheidVeld=eenheid,
                         waarde=waarde)
