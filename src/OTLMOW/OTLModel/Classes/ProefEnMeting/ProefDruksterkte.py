# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDruksterkte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De spanning waarbij het materiaal van de laag onder invloed van (druk)belasting bezwijkt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Walsbetonverharding')

        self._druksterkte = OTLAttribuut(field=DtcDocument,
                                         naam='druksterkte',
                                         label='druksterkte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte.druksterkte',
                                         definition='Proefresultaten van de druksterkte van de laag.',
                                         owner=self)

    @property
    def druksterkte(self):
        """Proefresultaten van de druksterkte van de laag."""
        return self._druksterkte.get_waarde()

    @druksterkte.setter
    def druksterkte(self, value):
        self._druksterkte.set_waarde(value, owner=self)
