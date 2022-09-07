# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verwarmingslint(AIMObject, LijnGeometrie):
    """Verwarmbare omwikkeling voor onderdelen die moeten beschermd worden tegen bevriezing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding')

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint.vermogen',
                                      definition='Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint.',
                                      owner=self)

    @property
    def vermogen(self):
        """Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
