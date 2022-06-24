# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Ventilatie import Ventilatie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlVentilatorGebruik import KlVentilatorGebruik
from OTLMOW.OTLModel.Datatypes.KlVentilatorRichting import KlVentilatorRichting
from OTLMOW.OTLModel.Datatypes.KwantWrdInProcent import KwantWrdInProcent


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilator(Ventilatie):
    """Onderdeel voor het creëren van luchtcirculatie binnen een open of gesloten ruimte met het oog op het vervangen van vervuilde door zuivere lucht. Voor een gesloten ruimte kan de luchtcirculatie ook zorgen voor afkoeling."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._draairichting = OTLAttribuut(field=KlVentilatorRichting,
                                           naam='draairichting',
                                           label='draairichting',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.draairichting',
                                           definition='Geeft aan of de bladen van de ventilator met de wijzers mee of tegen de wijzers in draaien.',
                                           owner=self)

        self._gebruik = OTLAttribuut(field=KlVentilatorGebruik,
                                     naam='gebruik',
                                     label='gebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.gebruik',
                                     definition='Geeft aan op welke manier de ventilator ingezet wordt.',
                                     owner=self)

        self._heefDrukverschilmeting = OTLAttribuut(field=BooleanField,
                                                    naam='heefDrukverschilmeting',
                                                    label='heeft drukverschilmeting',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.heefDrukverschilmeting',
                                                    definition='Geeft aan of de ventilator uitgerust is met een drukverschilmeters.',
                                                    owner=self)

        self._heeftTemperatuurmeting = OTLAttribuut(field=BooleanField,
                                                    naam='heeftTemperatuurmeting',
                                                    label='heeft temperatuurmeting',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.heeftTemperatuurmeting',
                                                    definition='Geeft aan of de ventilator uitgerust is met temperatuurmeting.',
                                                    owner=self)

        self._heeftTrillingsmeting = OTLAttribuut(field=BooleanField,
                                                  naam='heeftTrillingsmeting',
                                                  label='heeft trillingsmeting',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.heeftTrillingsmeting',
                                                  definition='Geeft aan of de ventilator uitgerust is met trillingsmeting.',
                                                  owner=self)

        self._standen = OTLAttribuut(field=KwantWrdInProcent,
                                     naam='standen',
                                     label='standen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.standen',
                                     kardinaliteit_max='*',
                                     definition='Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden.',
                                     owner=self)

    @property
    def draairichting(self):
        """Geeft aan of de bladen van de ventilator met de wijzers mee of tegen de wijzers in draaien."""
        return self._draairichting.get_waarde()

    @draairichting.setter
    def draairichting(self, value):
        self._draairichting.set_waarde(value, owner=self)

    @property
    def gebruik(self):
        """Geeft aan op welke manier de ventilator ingezet wordt."""
        return self._gebruik.get_waarde()

    @gebruik.setter
    def gebruik(self, value):
        self._gebruik.set_waarde(value, owner=self)

    @property
    def heefDrukverschilmeting(self):
        """Geeft aan of de ventilator uitgerust is met een drukverschilmeters."""
        return self._heefDrukverschilmeting.get_waarde()

    @heefDrukverschilmeting.setter
    def heefDrukverschilmeting(self, value):
        self._heefDrukverschilmeting.set_waarde(value, owner=self)

    @property
    def heeftTemperatuurmeting(self):
        """Geeft aan of de ventilator uitgerust is met temperatuurmeting."""
        return self._heeftTemperatuurmeting.get_waarde()

    @heeftTemperatuurmeting.setter
    def heeftTemperatuurmeting(self, value):
        self._heeftTemperatuurmeting.set_waarde(value, owner=self)

    @property
    def heeftTrillingsmeting(self):
        """Geeft aan of de ventilator uitgerust is met trillingsmeting."""
        return self._heeftTrillingsmeting.get_waarde()

    @heeftTrillingsmeting.setter
    def heeftTrillingsmeting(self, value):
        self._heeftTrillingsmeting.set_waarde(value, owner=self)

    @property
    def standen(self):
        """Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden."""
        return self._standen.get_waarde()

    @standen.setter
    def standen(self, value):
        self._standen.set_waarde(value, owner=self)
