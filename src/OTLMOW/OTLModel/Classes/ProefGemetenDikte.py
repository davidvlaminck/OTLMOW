# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGemetenDikte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De effectieve dikte van de laag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._gemetenDikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='gemetenDikte',
                                          label='gemeten dikte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte.gemetenDikte',
                                          definition='De gemeten dikte van de laag in centimeter.',
                                          owner=self)

    @property
    def gemetenDikte(self):
        """De gemeten dikte van de laag in centimeter."""
        return self._gemetenDikte.waarde

    @gemetenDikte.setter
    def gemetenDikte(self, value):
        self._gemetenDikte.set_waarde(value, owner=self)
