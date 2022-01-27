# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.KlLEACVoertuigOverhelling import KlLEACVoertuigOverhelling


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVoertuigOverhelling(Proef):
    """Proef om de overhelling over de bebakening van het voertuig te bepalen bij impact."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self._voertuigOverhelling = OTLAttribuut(field=KlLEACVoertuigOverhelling,
                                                 naam='voertuigOverhelling',
                                                 label='voertuig overhelling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling.voertuigOverhelling',
                                                 usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                 deprecated_version='2.0.0',
                                                 definition="Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald.")

    @property
    def voertuigOverhelling(self):
        """Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald."""
        return self._voertuigOverhelling.waarde

    @voertuigOverhelling.setter
    def voertuigOverhelling(self, value):
        self._voertuigOverhelling.set_waarde(value, owner=self)
