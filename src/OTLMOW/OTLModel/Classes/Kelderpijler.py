# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kelderpijler(AIMObject):
    """Pijler uitgerust met een kelder voor het herbergen van bewegende delen of onderhoudsvoorzieningen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._funderingsaanzetonderdebodemvandewaterweg = OTLAttribuut(field=BooleanField,
                                                                       naam='funderingsaanzetonderdebodemvandewaterweg',
                                                                       label='funderingsaanzet onder de bodem van de waterweg',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler.funderingsaanzetonderdebodemvandewaterweg',
                                                                       definition='Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet.',
                                                                       owner=self)

        self._inofopderandvandewaterweg = OTLAttribuut(field=BooleanField,
                                                       naam='inofopderandvandewaterweg',
                                                       label='in of op de rand van de waterweg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler.inofopderandvandewaterweg',
                                                       definition='Geeft aan of de pijler in of op de rand van de waterweg staat, al dan niet.',
                                                       owner=self)

    @property
    def funderingsaanzetonderdebodemvandewaterweg(self):
        """Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet."""
        return self._funderingsaanzetonderdebodemvandewaterweg.get_waarde()

    @funderingsaanzetonderdebodemvandewaterweg.setter
    def funderingsaanzetonderdebodemvandewaterweg(self, value):
        self._funderingsaanzetonderdebodemvandewaterweg.set_waarde(value, owner=self)

    @property
    def inofopderandvandewaterweg(self):
        """Geeft aan of de pijler in of op de rand van de waterweg staat, al dan niet."""
        return self._inofopderandvandewaterweg.get_waarde()

    @inofopderandvandewaterweg.setter
    def inofopderandvandewaterweg(self, value):
        self._inofopderandvandewaterweg.set_waarde(value, owner=self)
