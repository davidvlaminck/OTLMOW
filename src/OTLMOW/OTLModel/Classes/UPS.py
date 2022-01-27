# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLMOW.OTLModel.Datatypes.KlUPSMerk import KlUPSMerk
from OTLMOW.OTLModel.Datatypes.KlUPSModelnaam import KlUPSModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLMOW.OTLModel.Datatypes.KwantWrdInkWh import KwantWrdInkWh
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class UPS(Voedingspunt):
    """Toestel (Uninterruptible Power Supply = niet onderbreekbare voeding) voor het leveren van  elektrische energie van een vastgelegde kwaliteit, onafhankelijk van de beschikbaarheid van een betrouwbare netspanning. Indien het openbare net niet langer bruikbaar is om als energiebron te fungeren, wordt de energievoorziening overgenomen door de accubatterij. Deze zal gedurende een bepaalde tijd, afhankelijk van de capaciteit, de stroomvoorziening verzorgen. De UPS dient om de (minimale) voeding ononderbroken te verzekeren"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._autonomie = OTLAttribuut(field=KwantWrdInkWh,
                                       naam='autonomie',
                                       label='autonomie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.autonomie',
                                       definition='De tijd die de UPS een installatie van voeding kan voorzien.')

        self._maxContinuVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                                naam='maxContinuVermogen',
                                                label='maximaal continu vermogen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.maxContinuVermogen',
                                                definition='Maximale continu vermogen van de UPS.')

        self._maxPiekVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                             naam='maxPiekVermogen',
                                             label='max piekvermogen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.maxPiekVermogen',
                                             definition='Het maximale piekvermogen van de UPS.')

        self._merk = OTLAttribuut(field=KlUPSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.merk',
                                  definition='Merk waarmee de fabrikant de UPS identificeert.')

        self._modelnaam = OTLAttribuut(field=KlUPSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.modelnaam',
                                       definition='Modelnaam van de UPS volgens de fabrikant.')

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.')

    @property
    def autonomie(self):
        """De tijd die de UPS een installatie van voeding kan voorzien."""
        return self._autonomie.waarde

    @autonomie.setter
    def autonomie(self, value):
        self._autonomie.set_waarde(value, owner=self)

    @property
    def maxContinuVermogen(self):
        """Maximale continu vermogen van de UPS."""
        return self._maxContinuVermogen.waarde

    @maxContinuVermogen.setter
    def maxContinuVermogen(self, value):
        self._maxContinuVermogen.set_waarde(value, owner=self)

    @property
    def maxPiekVermogen(self):
        """Het maximale piekvermogen van de UPS."""
        return self._maxPiekVermogen.waarde

    @maxPiekVermogen.setter
    def maxPiekVermogen(self, value):
        self._maxPiekVermogen.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk waarmee de fabrikant de UPS identificeert."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de UPS volgens de fabrikant."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.waarde

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
