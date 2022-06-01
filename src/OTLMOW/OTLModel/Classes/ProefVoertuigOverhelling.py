# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.KlLEACVoertuigOverhelling import KlLEACVoertuigOverhelling
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVoertuigOverhelling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om de overhelling over de bebakening van het voertuig te bepalen bij impact."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0-RC3'

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._voertuigOverhelling = OTLAttribuut(field=KlLEACVoertuigOverhelling,
                                                 naam='voertuigOverhelling',
                                                 label='voertuig overhelling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVoertuigOverhelling.voertuigOverhelling',
                                                 usagenote='Klasse uit gebruik sinds versie 2.0.0-RC3',
                                                 deprecated_version='2.0.0-RC3',
                                                 definition="Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald.",
                                                 owner=self)

    @property
    def voertuigOverhelling(self):
        """Naast het horizontaal verplaatsen van de veiligheidsafbakening bij een impact, kan een voertuig bij impact ook over de afbakening hellen.  De maximale overhelling wordt op basis van foto's en video-opnames van de test bepaald."""
        return self._voertuigOverhelling.get_waarde()

    @voertuigOverhelling.setter
    def voertuigOverhelling(self, value):
        self._voertuigOverhelling.set_waarde(value, owner=self)
