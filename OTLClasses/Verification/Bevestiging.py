from ModelGenerator.BaseClasses import URIField
from OTLClasses.Verification.NietDirectioneleRelatie import NietDirectioneleRelatie


class Bevestiging(NietDirectioneleRelatie):
    """Deze relatie geeft aan dat twee onderdelen direct fysiek op elkaar bevestigd zijn. Dit kan zowel aan de buitenkant als
    aan de binnenkant zijn zoals bv. een camera aan een paal of een laagspanningsbord in een kast. Deze relatie heeft geen
    richting. """

    def __init__(self):
        pass

    uri: URIField = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging"
