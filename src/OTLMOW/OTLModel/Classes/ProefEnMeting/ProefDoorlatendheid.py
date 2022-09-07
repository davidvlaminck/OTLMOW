# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDoorlatendheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De controle van de doorlatendheid van het oppervlak met behulp van de dubbele ringmethode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating')

        self._doorlatendheid = OTLAttribuut(field=DtcDocument,
                                            naam='doorlatendheid',
                                            label='doorlatendheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid.doorlatendheid',
                                            definition='Proefresultaten van de waterdoorlatendheid.',
                                            owner=self)

    @property
    def doorlatendheid(self):
        """Proefresultaten van de waterdoorlatendheid."""
        return self._doorlatendheid.get_waarde()

    @doorlatendheid.setter
    def doorlatendheid(self, value):
        self._doorlatendheid.set_waarde(value, owner=self)
