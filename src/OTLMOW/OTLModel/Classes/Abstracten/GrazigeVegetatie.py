# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlGrazigeVegetatieAanleg import KlGrazigeVegetatieAanleg
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GrazigeVegetatie(BegroeidVoorkomen, VlakGeometrie):
    """Begroeiingen die uit grassen en (bloeiende) kruiden bestaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        BegroeidVoorkomen.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel')

        self._aanleg = OTLAttribuut(field=KlGrazigeVegetatieAanleg,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.aanleg',
                                    definition='De wijze van aanleg/aanplanting van de grazige vegetatie.',
                                    owner=self)

        self._heeftBolgewassen = OTLAttribuut(field=BooleanField,
                                              naam='heeftBolgewassen',
                                              label='heeft bolgewassen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.heeftBolgewassen',
                                              definition='Grasland met bol- en knolgewassen die in het voorjaar bloeien.',
                                              owner=self)

        self._isOvergroeienRandVerharding = OTLAttribuut(field=BooleanField,
                                                         naam='isOvergroeienRandVerharding',
                                                         label='is overgroeien rand verharding',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.isOvergroeienRandVerharding',
                                                         definition='Geeft aan of de rand van de verharding al dan niet wordt overgroeid door de grazige vegetatie.',
                                                         owner=self)

    @property
    def aanleg(self):
        """De wijze van aanleg/aanplanting van de grazige vegetatie."""
        return self._aanleg.get_waarde()

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def heeftBolgewassen(self):
        """Grasland met bol- en knolgewassen die in het voorjaar bloeien."""
        return self._heeftBolgewassen.get_waarde()

    @heeftBolgewassen.setter
    def heeftBolgewassen(self, value):
        self._heeftBolgewassen.set_waarde(value, owner=self)

    @property
    def isOvergroeienRandVerharding(self):
        """Geeft aan of de rand van de verharding al dan niet wordt overgroeid door de grazige vegetatie."""
        return self._isOvergroeienRandVerharding.get_waarde()

    @isOvergroeienRandVerharding.setter
    def isOvergroeienRandVerharding(self, value):
        self._isOvergroeienRandVerharding.set_waarde(value, owner=self)
