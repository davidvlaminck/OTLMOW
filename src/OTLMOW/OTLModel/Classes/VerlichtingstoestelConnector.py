# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from src.OTLMOW.OTLModel.Datatypes.KlVerlichtingstoestelconnectorBesturingsconnector import KlVerlichtingstoestelconnectorBesturingsconnector


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelConnector(ABC):
    """Abstracte om een besturingsconnector toe te voegen aan een WV-toestel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerlichtingstoestelConnector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._besturingsconnector = OTLAttribuut(field=KlVerlichtingstoestelconnectorBesturingsconnector,
                                                 naam='besturingsconnector',
                                                 label='besturingsconnector',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerlichtingstoestelConnector.besturingsconnector',
                                                 definition='Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.')

    @property
    def besturingsconnector(self):
        """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""
        return self._besturingsconnector.waarde

    @besturingsconnector.setter
    def besturingsconnector(self, value):
        self._besturingsconnector.set_waarde(value, owner=self)
