class DtcIdentificator:
    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""
    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'

    identificator: str
    """Een groep van tekens om een AIM object te identificeren of te benoemen."""
    toegekendDoor: str
    """Gegevens van de organisatie die de toekenning deed."""


# TODO bij inladen nakjken: usage note bevate informatie over uit gebruik