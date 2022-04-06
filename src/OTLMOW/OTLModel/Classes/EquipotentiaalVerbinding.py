# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class EquipotentiaalVerbinding(AIMNaamObject, LijnGeometrie):
    """Een equipotentiaal verbinding, ook wel equipotentiaalgeleider genoemd, voorziet de galvanische verbinding van een metalen object, dat in normale toestand niet stroomvoerend is, met het aardingsstelsel. Deze verbinding mag als aardingsgeleider derhalve nooit verbroken worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EquipotentiaalVerbinding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._isGeisoleerd = OTLAttribuut(field=BooleanField,
                                          naam='isGeisoleerd',
                                          label='is geïsoleerd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EquipotentiaalVerbinding.isGeisoleerd',
                                          definition='Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is. ',
                                          owner=self)

    @property
    def isGeisoleerd(self):
        """Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is. """
        return self._isGeisoleerd.waarde

    @isGeisoleerd.setter
    def isGeisoleerd(self, value):
        self._isGeisoleerd.set_waarde(value, owner=self)
