# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KlLEACKerendVermogen import KlLEACKerendVermogen
from OTLModel.Datatypes.KlLEACVoertuigOverhelling import KlLEACVoertuigOverhelling


# Generated with OTLClassCreator. To modify: extend, do not edit
class EigenschappenVoertuigkering(ABC):
    """Op deze abstracte worden attributen met betrekking tot voertuigkering bijgehouden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EigenschappenVoertuigkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._kerendVermogen = OTLAttribuut(field=KlLEACKerendVermogen,
                                            naam='kerendVermogen',
                                            label='kerend vermogen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EigenschappenVoertuigkering.kerendVermogen',
                                            definition='Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen.')

        self._voertuigOverhelling = OTLAttribuut(field=KlLEACVoertuigOverhelling,
                                                 naam='voertuigOverhelling',
                                                 label='voertuig overhelling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EigenschappenVoertuigkering.voertuigOverhelling',
                                                 definition="Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald.")

    @property
    def kerendVermogen(self):
        """Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen."""
        return self._kerendVermogen.waarde

    @kerendVermogen.setter
    def kerendVermogen(self, value):
        self._kerendVermogen.set_waarde(value, owner=self)

    @property
    def voertuigOverhelling(self):
        """Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald."""
        return self._voertuigOverhelling.waarde

    @voertuigOverhelling.setter
    def voertuigOverhelling(self, value):
        self._voertuigOverhelling.set_waarde(value, owner=self)
