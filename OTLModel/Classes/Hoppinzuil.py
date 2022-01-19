# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlWeergegevenVervoersmodiOpKaart import KlWeergegevenVervoersmodiOpKaart
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoppinzuil(AIMObject, AttributeInfo):
    """Abstracte om de gemeenschappelijke eigenschappen van de verschillende hoppinzuilen onder 1 noemer te plaatsen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._weergegevenVervoersmodiOpKaart = OTLAttribuut(field=KlWeergegevenVervoersmodiOpKaart,
                                                            naam='weergegevenVervoersmodiOpKaart',
                                                            label='weergegeven vervoersmodi op kaart',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil.weergegevenVervoersmodiOpKaart',
                                                            kardinaliteit_max='*',
                                                            definition='De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden weergegeven.')

        self._zuilnaam = OTLAttribuut(field=StringField,
                                      naam='zuilnaam',
                                      label='zuilnaam',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil.zuilnaam',
                                      definition='Naam van het hoppinpunt die verwijst naar een duidelijke en herkenbare plaatsnaam.')

        self._zuilnummer = OTLAttribuut(field=StringField,
                                        naam='zuilnummer',
                                        label='zuilnummer',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil.zuilnummer',
                                        definition='Uniek identificatienummer dat elke zuil krijgt en dat wordt opgenomen in de hoppinpuntendatabank.')

    @property
    def weergegevenVervoersmodiOpKaart(self):
        """De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden weergegeven."""
        return self._weergegevenVervoersmodiOpKaart.waarde

    @weergegevenVervoersmodiOpKaart.setter
    def weergegevenVervoersmodiOpKaart(self, value):
        self._weergegevenVervoersmodiOpKaart.set_waarde(value, owner=self)

    @property
    def zuilnaam(self):
        """Naam van het hoppinpunt die verwijst naar een duidelijke en herkenbare plaatsnaam."""
        return self._zuilnaam.waarde

    @zuilnaam.setter
    def zuilnaam(self, value):
        self._zuilnaam.set_waarde(value, owner=self)

    @property
    def zuilnummer(self):
        """Uniek identificatienummer dat elke zuil krijgt en dat wordt opgenomen in de hoppinpuntendatabank."""
        return self._zuilnummer.waarde

    @zuilnummer.setter
    def zuilnummer(self, value):
        self._zuilnummer.set_waarde(value, owner=self)
