# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlTypeLandhoofd import KlTypeLandhoofd


# Generated with OTLClassCreator. To modify: extend, do not edit
class Landhoofd(AIMObject):
    """Eindsteunpunt van een brug die de overgang vormt tussen de brug en het aan het landhoofd achterliggend grondlichaam."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._funderingsAanzetOnderDeBodemVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                                       naam='funderingsAanzetOnderDeBodemVanDeWaterweg',
                                                                       label='funderingsaanzet onder de bodem van de waterweg',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd.funderingsAanzetOnderDeBodemVanDeWaterweg',
                                                                       definition='Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet.',
                                                                       owner=self)

        self._inOfOpDeRandVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                       naam='inOfOpDeRandVanDeWaterweg',
                                                       label='in of op de rand van de waterweg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd.inOfOpDeRandVanDeWaterweg',
                                                       definition='Geeft aan of het landhoofd in of op de rand van de waterweg staat, al dan niet.',
                                                       owner=self)

        self._typeLandhoofd = OTLAttribuut(field=KlTypeLandhoofd,
                                           naam='typeLandhoofd',
                                           label='type landhoofd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd.typeLandhoofd',
                                           definition='Het soort landhoofd.',
                                           owner=self)

    @property
    def funderingsAanzetOnderDeBodemVanDeWaterweg(self):
        """Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet."""
        return self._funderingsAanzetOnderDeBodemVanDeWaterweg.get_waarde()

    @funderingsAanzetOnderDeBodemVanDeWaterweg.setter
    def funderingsAanzetOnderDeBodemVanDeWaterweg(self, value):
        self._funderingsAanzetOnderDeBodemVanDeWaterweg.set_waarde(value, owner=self)

    @property
    def inOfOpDeRandVanDeWaterweg(self):
        """Geeft aan of het landhoofd in of op de rand van de waterweg staat, al dan niet."""
        return self._inOfOpDeRandVanDeWaterweg.get_waarde()

    @inOfOpDeRandVanDeWaterweg.setter
    def inOfOpDeRandVanDeWaterweg(self, value):
        self._inOfOpDeRandVanDeWaterweg.set_waarde(value, owner=self)

    @property
    def typeLandhoofd(self):
        """Het soort landhoofd."""
        return self._typeLandhoofd.get_waarde()

    @typeLandhoofd.setter
    def typeLandhoofd(self, value):
        self._typeLandhoofd.set_waarde(value, owner=self)
