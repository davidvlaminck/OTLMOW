# coding=utf-8
from OTLModel.Datatypes.KwantWrd import KwantWrd
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeterTAW(KwantWrd):
    """Een kwantitatieve waarde die de hoogte weergeeft in meter van een locatie tov het TAW-referentiepeil."""

    def __init__(self, waarde=None):
        self.eenheid = LiteralField(naam="standaardEenheid",
                                    label="standaard eenheid",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterTAW.standaardEenheid",
                                    definition="De standaard eenheid bij dit datatype is uitgedrukt in meter.",
                                    constraints='"m"^^cdt:ucumunit',
                                    usagenote='"m"^^cdt:ucumunit',
                                    deprecated_version="",
                                    readonlyValue="m")
        """De standaard eenheid bij dit datatype is uitgedrukt in meter."""

        self.waardeVeld = DecimalFloatField(naam="waarde",
                                            label="waarde",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterTAW.waarde",
                                            definition="Bevat een getal die bij het datatype hoort.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bevat een getal die bij het datatype hoort."""

        super().__init__(naam="KwantWrdInMeterTAW",
                         label="Kwantitatieve waarde in meter TAW",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeterTAW",
                         definition="Een kwantitatieve waarde die de hoogte weergeeft in meter van een locatie tov het TAW-referentiepeil.",
                         usagenote="",
                         deprecated_version="",
                         waardeVeld=self.waardeVeld,
                         eenheidVeld=self.eenheid,
                         waarde=waarde)
