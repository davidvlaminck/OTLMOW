# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtdichtheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Testen van de drukval van het beproefde leidingsvak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._luchtdichtheid = OTLAttribuut(field=DtcDocument,
                                            naam='luchtdichtheid',
                                            label='luchtdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid.luchtdichtheid',
                                            definition='Testresultaten van de opgemeten drukval van het beproefde leidingsvak.',
                                            owner=self)

    @property
    def luchtdichtheid(self):
        """Testresultaten van de opgemeten drukval van het beproefde leidingsvak."""
        return self._luchtdichtheid.get_waarde()

    @luchtdichtheid.setter
    def luchtdichtheid(self, value):
        self._luchtdichtheid.set_waarde(value, owner=self)
