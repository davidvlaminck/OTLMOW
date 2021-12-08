from ModelGenerator.BaseClasses.StringField import StringField


class DtcIdentificator:
    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""
    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'

    identificator = StringField(naam="identificator", label="identificator",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                                   definition="Een groep van tekens om een AIM object te identificeren of te benoemen."
                                   , constraints="", usagenote="", deprecated_version="")
    """Een groep van tekens om een AIM object te identificeren of te benoemen."""

    toegekendDoor = StringField(naam="toegekendDoor", label="toegekend door",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor",
                                   definition="Gegevens van de organisatie die de toekenning deed."
                                   , constraints="", usagenote="", deprecated_version="")
    """Gegevens van de organisatie die de toekenning deed."""


# TODO bij inladen nakjken: usage note bevate informatie over uit gebruik