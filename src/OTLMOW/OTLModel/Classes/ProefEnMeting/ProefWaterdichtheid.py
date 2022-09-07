# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWaterdichtheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Testen van het waterverlies van het beproefde leidingsvak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put')

        self._waterdichtheid = OTLAttribuut(field=DtcDocument,
                                            naam='waterdichtheid',
                                            label='waterdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid.waterdichtheid',
                                            definition='Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak.',
                                            owner=self)

    @property
    def waterdichtheid(self):
        """Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak."""
        return self._waterdichtheid.get_waarde()

    @waterdichtheid.setter
    def waterdichtheid(self, value):
        self._waterdichtheid.set_waarde(value, owner=self)
