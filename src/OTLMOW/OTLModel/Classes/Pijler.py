# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pijler(AIMObject):
    """Een pijler is een steunpilaar die fungeert als vrijstaande drager en een steunpunt vormt tussen landhoofden voor de liggers of gewelven van een kunstwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._funderingsaanzetOnderDeBodemVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                                       naam='funderingsaanzetOnderDeBodemVanDeWaterweg',
                                                                       label='funderingsaanzet onder de bodem van de waterweg',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler.funderingsaanzetOnderDeBodemVanDeWaterweg',
                                                                       definition='Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet.',
                                                                       owner=self)

        self._inOfOpDeRandVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                       naam='inOfOpDeRandVanDeWaterweg',
                                                       label='in of op de rand van de waterweg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler.inOfOpDeRandVanDeWaterweg',
                                                       definition='Geeft aan of de pijler in of op de rand van de waterweg staat, al dan niet.',
                                                       owner=self)

    @property
    def funderingsaanzetOnderDeBodemVanDeWaterweg(self):
        """Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet."""
        return self._funderingsaanzetOnderDeBodemVanDeWaterweg.get_waarde()

    @funderingsaanzetOnderDeBodemVanDeWaterweg.setter
    def funderingsaanzetOnderDeBodemVanDeWaterweg(self, value):
        self._funderingsaanzetOnderDeBodemVanDeWaterweg.set_waarde(value, owner=self)

    @property
    def inOfOpDeRandVanDeWaterweg(self):
        """Geeft aan of de pijler in of op de rand van de waterweg staat, al dan niet."""
        return self._inOfOpDeRandVanDeWaterweg.get_waarde()

    @inOfOpDeRandVanDeWaterweg.setter
    def inOfOpDeRandVanDeWaterweg(self, value):
        self._inOfOpDeRandVanDeWaterweg.set_waarde(value, owner=self)
