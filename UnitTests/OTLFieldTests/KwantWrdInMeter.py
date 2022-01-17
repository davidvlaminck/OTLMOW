﻿from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam="standaardEenheid",
                                              label="standaard eenheid",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter.standaardEenheid",
                                              definition="De standaard eenheid bij dit datatype is uitgedrukt in meter.",
                                              constraints='"m"^^cdt:ucumunit',
                                              usagenote='"m"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMeter(FloatOrDecimalField, KwantWrd):
    naam = "KwantWrdInMeter"
    label = "Kwantitatieve waarde in meter"
    objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter"
    definition = "Een kwantitatieve waarde die een getal in meter uitdrukt."
    eenheid = KwantWrdInMeterEenheid()
