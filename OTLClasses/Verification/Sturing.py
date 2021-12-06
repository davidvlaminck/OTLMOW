from ModelGenerator.BaseClasses import URIField
from OTLClasses.Verification.NietDirectioneleRelatie import NietDirectioneleRelatie


class Sturing(NietDirectioneleRelatie):
    """Deze relatie geeft aan of er een of andere vorm van dataverkeer is tussen 2 onderdelen. Een wegverlichtingstoestel dat
    aan staat wordt ook als sturing beschouwd, in dit geval is het een lang ononderbroken elektrisch aan-signaal. Deze relatie
    heeft geen richting. """

    def __init__(self):
        pass

    uri: URIField = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing"
