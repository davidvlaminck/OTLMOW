# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dieselgenerator(Voedingspunt):
    """Dieselmotor die een generator (machine die mechanische energie omzet in elektrische energie) aandrijft,typisch gebruikt als noodstroom aggregaat bij het wegvallen van de normale netvoeding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieselgenerator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieselgenerator.afmetingen',
                                        definition='De afmetingen van de dieselgenerator.')

    @property
    def afmetingen(self):
        """De afmetingen van de dieselgenerator."""
        return self._afmetingen.waarde

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)
