from UnitTests.OTLFieldTests.FloatOrDecimalField import FloatOrDecimalField
from UnitTests.OTLFieldTests.KwantWrd import KwantWrd
from UnitTests.OTLFieldTests.KwantWrdEenheid import KwantWrdEenheid
from UnitTests.OTLFieldTests.OTLAttribuut import OTLAttribuut
from UnitTests.OTLFieldTests.StringField import StringField


class LiteralField(StringField):
    pass


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


class KwantWrdInMeter(FloatOrDecimalField, KwantWrd):
    naam = "KwantWrdInMeter"
    label = "Kwantitatieve waarde in meter"
    objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter"
    definition = "Een kwantitatieve waarde die een getal in meter uitdrukt."
    eenheid = KwantWrdInMeterEenheid()
