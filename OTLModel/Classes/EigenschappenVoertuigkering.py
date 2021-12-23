from abc import abstractmethod, ABC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACKerendVermogen import KlLEACKerendVermogen
from OTLModel.Datatypes.KlLEACVoertuigOverhelling import KlLEACVoertuigOverhelling


# Generated with OTLClassCreator
class EigenschappenVoertuigkering(ABC):
    """Op deze abstracte worden attributen met betrekking tot voertuigkering bijgehouden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EigenschappenVoertuigkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.kerendVermogen = KeuzelijstField(naam="kerendVermogen",
                                              label="kerend vermogen",
                                              lijst=KlLEACKerendVermogen(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EigenschappenVoertuigkering.kerendVermogen",
                                              definition="Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen."""

        self.voertuigOverhelling = KeuzelijstField(naam="voertuigOverhelling",
                                                   label="voertuig overhelling",
                                                   lijst=KlLEACVoertuigOverhelling(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EigenschappenVoertuigkering.voertuigOverhelling",
                                                   definition="Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald."""
