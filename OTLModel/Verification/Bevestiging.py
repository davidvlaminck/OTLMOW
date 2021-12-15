from OTLModel.Verification.NietDirectioneleRelatie import NietDirectioneleRelatie


class Bevestiging(NietDirectioneleRelatie):
    """Deze relatie geeft aan dat twee onderdelen direct fysiek op elkaar bevestigd zijn. Dit kan zowel aan de buitenkant als
    aan de binnenkant zijn zoals bv. een camera aan een paal of een laagspanningsbord in een kast. Deze relatie heeft geen
    richting. """

    def __init__(self):
        pass

    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""
