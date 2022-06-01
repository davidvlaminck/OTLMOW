# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.KlLEACSchokindex import KlLEACSchokindex
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefSchokindex(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef voor de bepaling van de schokindex parameter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0-RC3'

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._schokindex = OTLAttribuut(field=KlLEACSchokindex,
                                        naam='schokindex',
                                        label='schokindex',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex.schokindex',
                                        usagenote='Klasse uit gebruik sinds versie 2.0.0-RC3',
                                        deprecated_version='2.0.0-RC3',
                                        definition='De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding.',
                                        owner=self)

    @property
    def schokindex(self):
        """De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding."""
        return self._schokindex.get_waarde()

    @schokindex.setter
    def schokindex(self, value):
        self._schokindex.set_waarde(value, owner=self)
