from UnitTests.OTLFieldTests.AttributeInfo import AttributeInfo
from UnitTests.OTLFieldTests.OTLAttribuut import OTLAttribuut
from UnitTests.OTLFieldTests.StringField import StringField
from UnitTests.OTLFieldTests.ComplexField import ComplexField


class DtcIdentificatorWaarden(AttributeInfo):
    def __init__(self):
        self._identificator = OTLAttribuut(field=StringField,
                                           naam="identificator",
                                           label="identificator",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                                           definition="Een groep van tekens om een AIM object te identificeren of te benoemen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")

        self._toegekendDoor = OTLAttribuut(field=StringField,
                                           naam="toegekendDoor",
                                           label="toegekend door",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor",
                                           definition="Gegevens van de organisatie die de toekenning deed.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")

    @property
    def identificator(self):
        """Een groep van tekens om een AIM object te identificeren of te benoemen."""
        return self._identificator.waarde

    @identificator.setter
    def identificator(self, value):
        self._identificator.set_waarde(value)

    @property
    def toegekendDoor(self):
        """Gegevens van de organisatie die de toekenning deed."""
        return self._toegekendDoor.waarde

    @toegekendDoor.setter
    def toegekendDoor(self, value):
        self._toegekendDoor.set_waarde(value)


class DtcIdentificator(ComplexField, AttributeInfo):
    naam = "DtcIdentificator",
    label = "Identificator",
    objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",
    definition = "Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.",
    usagenote = "",
    deprecated_version = ""
    waardeObject = DtcIdentificatorWaarden

