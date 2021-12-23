from abc import abstractmethod, ABC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerlichtingstoestelconnectorBesturingsconnector import KlVerlichtingstoestelconnectorBesturingsconnector


# Generated with OTLClassCreator
class VerlichtingstoestelConnector(ABC):
    """Abstracte om een besturingsconnector toe te voegen aan een WV-toestel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerlichtingstoestelConnector"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.besturingsconnector = KeuzelijstField(naam="besturingsconnector",
                                                   label="besturingsconnector",
                                                   lijst=KlVerlichtingstoestelconnectorBesturingsconnector(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerlichtingstoestelConnector.besturingsconnector",
                                                   definition="Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""
