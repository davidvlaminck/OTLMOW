from OTLModel.Classes.NietDirectioneleRelatie import NietDirectioneleRelatie


# Generated with OTLClassCreator
class Sturing(NietDirectioneleRelatie):
    """Deze relatie geeft aan of er een of andere vorm van dataverkeer is tussen 2 onderdelen. Een wegverlichtingstoestel dat aan staat wordt ook als sturing beschouwd, in dit geval is het een lang ononderbroken elektrisch aan-signaal. Deze relatie heeft geen richting."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
