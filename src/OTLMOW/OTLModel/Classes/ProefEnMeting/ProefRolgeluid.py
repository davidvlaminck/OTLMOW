# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefRolgeluid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Het rolgeluid wordt gemeten met de CPX-methode volgens ISO/CEN 11819-2."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._rolgeluid = OTLAttribuut(field=DtcDocument,
                                       naam='rolgeluid',
                                       label='rolgeluid',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid.rolgeluid',
                                       definition='Proefresultaten van het rolgeluid van de toplaag.',
                                       owner=self)

    @property
    def rolgeluid(self):
        """Proefresultaten van het rolgeluid van de toplaag."""
        return self._rolgeluid.get_waarde()

    @rolgeluid.setter
    def rolgeluid(self, value):
        self._rolgeluid.set_waarde(value, owner=self)
