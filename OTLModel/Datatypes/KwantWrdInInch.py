# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInInch(KwantWrd):
    """Een kwantitatieve waarde die een getal in inches uitdrukt."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in inch als internationale eenheid (eengemaakte Britse en Amerikaanse systeem).",
                                    constraints='"[in_i]"^^cdt:ucumunit',
                                    usagenote='"[in_i]"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="[in_i]")
        """De standaard eenheid bij dit datatype is uitgedrukt in inch als internationale eenheid (eengemaakte Britse en Amerikaanse systeem)."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInInch",
                         label="Kwantitatieve waarde in inch",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch",
                         definition="Een kwantitatieve waarde die een getal in inches uitdrukt.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
