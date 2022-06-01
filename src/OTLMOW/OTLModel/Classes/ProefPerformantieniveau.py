# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPerformantieniveau(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van het performantieniveau."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0-RC3'

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau.performantieniveau',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0-RC3',
                                                deprecated_version='2.0.0-RC3',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.',
                                                owner=self)

    @property
    def performantieniveau(self):
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.get_waarde()

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)
