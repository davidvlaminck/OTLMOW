from ModelGenerator.BaseClasses.ComplexField import ComplexField, ComplexAttributen
from ModelGenerator.BaseClasses.OTLField import OTLField
from ModelGenerator.BaseClasses.StringField import StringField


class DtcIdentificator(ComplexField):
    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""

    def __init__(self):
        super().__init__(naam="DtcIdentificator", label="Identificator",
                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",
                       definition="Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.",
                       usagenote="", deprecated_version="")
        self.waarde = ComplexAttributen()

        self.waarde.identificator = StringField(naam="identificator", label="identificator",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                                                definition="Een groep van tekens om een AIM object te identificeren of te benoemen.",
                                                constraints="", usagenote="", deprecated_version="")
        """Een groep van tekens om een AIM object te identificeren of te benoemen."""

        self.waarde.toegekendDoor = StringField(naam="toegekendDoor", label="toegekend door",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor",
                                                definition="Gegevens van de organisatie die de toekenning deed.",
                                                constraints="", usagenote="", deprecated_version="")
        """Gegevens van de organisatie die de toekenning deed."""

        self.identificator = self.waarde.identificator
        self.toegekendDoor = self.waarde.toegekendDoor

    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'


# TODO bij inladen nakjken: usage note bevate informatie over uit gebruik