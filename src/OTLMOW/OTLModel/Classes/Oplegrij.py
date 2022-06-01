# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegrij(AIMNaamObject):
    """Een rij van opleggingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalOpleggingenOpRij = OTLAttribuut(field=NonNegIntegerField,
                                                    naam='aantalOpleggingenOpRij',
                                                    label='aantal opleggingen op rij',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij.aantalOpleggingenOpRij',
                                                    definition='Het aantal opleggingen die op een rij liggen.',
                                                    owner=self)

    @property
    def aantalOpleggingenOpRij(self):
        """Het aantal opleggingen die op een rij liggen."""
        return self._aantalOpleggingenOpRij.get_waarde()

    @aantalOpleggingenOpRij.setter
    def aantalOpleggingenOpRij(self, value):
        self._aantalOpleggingenOpRij.set_waarde(value, owner=self)
