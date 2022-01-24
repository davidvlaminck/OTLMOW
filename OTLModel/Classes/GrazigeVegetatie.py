# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KlGrazigeVegetatieAanleg import KlGrazigeVegetatieAanleg


# Generated with OTLClassCreator. To modify: extend, do not edit
class GrazigeVegetatie(BegroeidVoorkomen):
    """Begroeiingen die uit grassen en (bloeiende) kruiden bestaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._aanleg = OTLAttribuut(field=KlGrazigeVegetatieAanleg,
                                    naam='aanleg',
                                    label='aanleg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.aanleg',
                                    definition='De wijze van aanleg/aanplanting van de grazige vegetatie.')

        self._heeftBolgewassen = OTLAttribuut(field=BooleanField,
                                              naam='heeftBolgewassen',
                                              label='heeft bolgewassen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.heeftBolgewassen',
                                              definition='Grasland met bol- en knolgewassen die in het voorjaar bloeien.')

        self._isOvergroeienRandVerharding = OTLAttribuut(field=BooleanField,
                                                         naam='isOvergroeienRandVerharding',
                                                         label='is overgroeien rand verharding',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GrazigeVegetatie.isOvergroeienRandVerharding',
                                                         definition='Geeft aan of de rand van de verharding al dan niet wordt overgroeid door de grazige vegetatie.')

    @property
    def aanleg(self):
        """De wijze van aanleg/aanplanting van de grazige vegetatie."""
        return self._aanleg.waarde

    @aanleg.setter
    def aanleg(self, value):
        self._aanleg.set_waarde(value, owner=self)

    @property
    def heeftBolgewassen(self):
        """Grasland met bol- en knolgewassen die in het voorjaar bloeien."""
        return self._heeftBolgewassen.waarde

    @heeftBolgewassen.setter
    def heeftBolgewassen(self, value):
        self._heeftBolgewassen.set_waarde(value, owner=self)

    @property
    def isOvergroeienRandVerharding(self):
        """Geeft aan of de rand van de verharding al dan niet wordt overgroeid door de grazige vegetatie."""
        return self._isOvergroeienRandVerharding.waarde

    @isOvergroeienRandVerharding.setter
    def isOvergroeienRandVerharding(self, value):
        self._isOvergroeienRandVerharding.set_waarde(value, owner=self)
