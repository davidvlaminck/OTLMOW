# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.KlLEACPerformantieklasse import KlLEACPerformantieklasse
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPerformantieklasse(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef die de performantie (bij impact) bepaalt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie', deprecated='2.0.0')

        self._performantieklasse = OTLAttribuut(field=KlLEACPerformantieklasse,
                                                naam='performantieklasse',
                                                label='performantieklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse.performantieklasse',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='De aanduiding hoe (performantie) de beginconstructie is getest.',
                                                owner=self)

    @property
    def performantieklasse(self):
        """De aanduiding hoe (performantie) de beginconstructie is getest."""
        return self._performantieklasse.get_waarde()

    @performantieklasse.setter
    def performantieklasse(self, value):
        self._performantieklasse.set_waarde(value, owner=self)
