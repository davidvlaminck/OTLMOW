# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.KlLocatieWaterdichting import KlLocatieWaterdichting
from OTLMOW.OTLModel.Datatypes.KlTypeUitkraging import KlTypeUitkraging
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Uitkraging(ConstructiefObject):
    """Deel dat van de rand uitkraagt ten opzichte van het randprofiel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Uitkraging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._installatieDatum = OTLAttribuut(field=DateField,
                                              naam='installatieDatum',
                                              label='installatiedatum',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Uitkraging.installatieDatum',
                                              definition='De datum van installatie',
                                              owner=self)

        self._locatieWaterdichting = OTLAttribuut(field=KlLocatieWaterdichting,
                                                  naam='locatieWaterdichting',
                                                  label='locatie waterdichting',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Uitkraging.locatieWaterdichting',
                                                  definition='Plaats waar de waterdichting op de constructie is aangebracht.',
                                                  owner=self)

        self._sterkte = OTLAttribuut(field=KwantWrdInKiloNewton,
                                     naam='sterkte',
                                     label='sterkte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Uitkraging.sterkte',
                                     definition='De draagkracht van de uitkraging.',
                                     owner=self)

        self._type = OTLAttribuut(field=KlTypeUitkraging,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Uitkraging.type',
                                  definition='De soort uitkraging.',
                                  owner=self)

        self._uitkragingslengte = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='uitkragingslengte',
                                               label='uitkragingslengte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Uitkraging.uitkragingslengte',
                                               definition='De lengte van het deel dat uitkraagt.',
                                               owner=self)

    @property
    def installatieDatum(self):
        """De datum van installatie"""
        return self._installatieDatum.get_waarde()

    @installatieDatum.setter
    def installatieDatum(self, value):
        self._installatieDatum.set_waarde(value, owner=self)

    @property
    def locatieWaterdichting(self):
        """Plaats waar de waterdichting op de constructie is aangebracht."""
        return self._locatieWaterdichting.get_waarde()

    @locatieWaterdichting.setter
    def locatieWaterdichting(self, value):
        self._locatieWaterdichting.set_waarde(value, owner=self)

    @property
    def sterkte(self):
        """De draagkracht van de uitkraging."""
        return self._sterkte.get_waarde()

    @sterkte.setter
    def sterkte(self, value):
        self._sterkte.set_waarde(value, owner=self)

    @property
    def type(self):
        """De soort uitkraging."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def uitkragingslengte(self):
        """De lengte van het deel dat uitkraagt."""
        return self._uitkragingslengte.get_waarde()

    @uitkragingslengte.setter
    def uitkragingslengte(self, value):
        self._uitkragingslengte.set_waarde(value, owner=self)
