# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.KabelAarding import KabelAarding
from OTLMOW.OTLModel.Classes.KabelAardingSamenstelling import KabelAardingSamenstelling
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingskabel(KabelAarding, KabelAardingSamenstelling, AIMNaamObject):
    """Een aardingskabel is een geleidende verbinding, typisch uit koper, die ervoor zorgt dat een ongewenste elektrische stroom (foutstroom) op een installatie naar de aarde kan afgeleid worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        KabelAarding.__init__(self)
        KabelAardingSamenstelling.__init__(self)

        self._isGeisoleerd = OTLAttribuut(field=BooleanField,
                                          naam='isGeisoleerd',
                                          label='is geïsoleerd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel.isGeisoleerd',
                                          definition='Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is. ',
                                          owner=self)

    @property
    def isGeisoleerd(self):
        """Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is. """
        return self._isGeisoleerd.get_waarde()

    @isGeisoleerd.setter
    def isGeisoleerd(self, value):
        self._isGeisoleerd.set_waarde(value, owner=self)
