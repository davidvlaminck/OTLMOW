# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlBeheerBoomvorm import KlBeheerBoomvorm
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerBoomvorm(AIMObject, PuntGeometrie, VlakGeometrie):
    """Het beheerobject voor de solitaire boom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._beheeroptie = OTLAttribuut(field=KlBeheerBoomvorm,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Behandelingswijzen van bomen.',
                                         owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen grond rond de boom.',
                                         owner=self)

    @property
    def beheeroptie(self):
        """Behandelingswijzen van bomen."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte in vierkante meter van de te behandelen grond rond de boom."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
