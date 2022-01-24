# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.KlHelling import KlHelling
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gronddam(AIMObject):
    """Gronddammen zijn trapeziumvormige constructies bestaande uit zand, grond of steenachtige materialen.
De onderkant van de gronddam wordt direct op het bestaand maaiveld aangebracht of op een vooraf aangebrachte grondverbetering.
Een gronddam kan volgende functies vervullen: geluidswering, geleiding van dieren, veiligheid en lichtwering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._basisbreedte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='basisbreedte',
                                          label='basisbreedte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.basisbreedte',
                                          definition='De breedte van de basis van de gronddam in meter.')

        self._gronddichtheid = OTLAttribuut(field=FloatOrDecimalField,
                                            naam='gronddichtheid',
                                            label='gronddichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.gronddichtheid',
                                            definition='De gronddichtheid van de gronddam.')

        self._hellingAchterzijde = OTLAttribuut(field=KlHelling,
                                                naam='hellingAchterzijde',
                                                label='helling achterzijde',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.hellingAchterzijde',
                                                definition='De hellingsgraad van de achterzijde gronddam in kwarten.')

        self._hellingVoorzijde = OTLAttribuut(field=KlHelling,
                                              naam='hellingVoorzijde',
                                              label='helling voorzijde',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.hellingVoorzijde',
                                              definition='De hellingsgraad van de voorzijde van de gronddam in kwarten.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.hoogte',
                                    definition='De hoogte van de gronddam in meter.')

        self._kruinbreedte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='kruinbreedte',
                                          label='kruinbreedte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gronddam.kruinbreedte',
                                          definition='De breedte van de kruin van de gronddam in meter.')

    @property
    def basisbreedte(self):
        """De breedte van de basis van de gronddam in meter."""
        return self._basisbreedte.waarde

    @basisbreedte.setter
    def basisbreedte(self, value):
        self._basisbreedte.set_waarde(value, owner=self)

    @property
    def gronddichtheid(self):
        """De gronddichtheid van de gronddam."""
        return self._gronddichtheid.waarde

    @gronddichtheid.setter
    def gronddichtheid(self, value):
        self._gronddichtheid.set_waarde(value, owner=self)

    @property
    def hellingAchterzijde(self):
        """De hellingsgraad van de achterzijde gronddam in kwarten."""
        return self._hellingAchterzijde.waarde

    @hellingAchterzijde.setter
    def hellingAchterzijde(self, value):
        self._hellingAchterzijde.set_waarde(value, owner=self)

    @property
    def hellingVoorzijde(self):
        """De hellingsgraad van de voorzijde van de gronddam in kwarten."""
        return self._hellingVoorzijde.waarde

    @hellingVoorzijde.setter
    def hellingVoorzijde(self, value):
        self._hellingVoorzijde.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De hoogte van de gronddam in meter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def kruinbreedte(self):
        """De breedte van de kruin van de gronddam in meter."""
        return self._kruinbreedte.waarde

    @kruinbreedte.setter
    def kruinbreedte(self, value):
        self._kruinbreedte.set_waarde(value, owner=self)
