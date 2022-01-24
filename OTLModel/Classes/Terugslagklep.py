# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LinkendElement import LinkendElement
from OTLModel.Datatypes.KlTerugslagklepType import KlTerugslagklepType
from OTLModel.Datatypes.KlTsklepAfsluiterMateriaal import KlTsklepAfsluiterMateriaal
from OTLModel.Datatypes.KlVormTerugslagklep import KlVormTerugslagklep
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugslagklep(LinkendElement):
    """Een terugslagklep is een klep die dient om water, vloeistof, granulaat, poeder of gas in één richting door te laten. Meestal duwt het medium de klep bij het heenstromen open en sluit een veer of de zwaartekracht de klep."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedteOpening = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='breedteOpening',
                                            label='breedte opening',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.breedteOpening',
                                            definition='Breedte van de opening die door de terugslagklep wordt afgesloten in millimeter.')

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.diameter',
                                      definition='De diameter van de terugslagklep in millimeter.')

        self._hoogteOpening = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='hoogteOpening',
                                           label='hoogte opening',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.hoogteOpening',
                                           definition='De hoogte van de opening die door de terugslagklep wordt afgesloten in millimeter.')

        self._materiaal = OTLAttribuut(field=KlTsklepAfsluiterMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.materiaal',
                                       definition='Het materiaal waaruit de terugslagklep is vervaardigd.')

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.peil',
                                  definition='Niveau van de doorlaatopening van de terugslagklep uitgedrukt in meter-TAW.')

        self._type = OTLAttribuut(field=KlTerugslagklepType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.type',
                                  definition='Bepaalt het type van terugslagklep.')

        self._vorm = OTLAttribuut(field=KlVormTerugslagklep,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugslagklep.vorm',
                                  definition='De vorm van de terugslagklep.')

    @property
    def breedteOpening(self):
        """Breedte van de opening die door de terugslagklep wordt afgesloten in millimeter."""
        return self._breedteOpening.waarde

    @breedteOpening.setter
    def breedteOpening(self, value):
        self._breedteOpening.set_waarde(value, owner=self)

    @property
    def diameter(self):
        """De diameter van de terugslagklep in millimeter."""
        return self._diameter.waarde

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def hoogteOpening(self):
        """De hoogte van de opening die door de terugslagklep wordt afgesloten in millimeter."""
        return self._hoogteOpening.waarde

    @hoogteOpening.setter
    def hoogteOpening(self, value):
        self._hoogteOpening.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de terugslagklep is vervaardigd."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def peil(self):
        """Niveau van de doorlaatopening van de terugslagklep uitgedrukt in meter-TAW."""
        return self._peil.waarde

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)

    @property
    def type(self):
        """Bepaalt het type van terugslagklep."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de terugslagklep."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
