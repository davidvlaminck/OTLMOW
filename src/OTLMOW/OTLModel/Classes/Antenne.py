# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Communicatieapparatuur import Communicatieapparatuur
from OTLMOW.OTLModel.Datatypes.KlAntenneFrequentierange import KlAntenneFrequentierange
from OTLMOW.OTLModel.Datatypes.KlAntenneMerk import KlAntenneMerk
from OTLMOW.OTLModel.Datatypes.KlAntenneModelnaam import KlAntenneModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Antenne(Communicatieapparatuur):
    """Toestel verbonden met een zender of ontvanger ten behoeve van het opvangen of verspreiden van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._frequentierange = OTLAttribuut(field=KlAntenneFrequentierange,
                                             naam='frequentierange',
                                             label='frequentierange',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.frequentierange',
                                             definition='Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlAntenneMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.merk',
                                  definition='Het merk van de antenne.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAntenneModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.modelnaam',
                                       definition='De modelnaam/product range van een antenne.',
                                       owner=self)

    @property
    def frequentierange(self):
        """Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden."""
        return self._frequentierange.waarde

    @frequentierange.setter
    def frequentierange(self, value):
        self._frequentierange.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de antenne."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van een antenne."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
