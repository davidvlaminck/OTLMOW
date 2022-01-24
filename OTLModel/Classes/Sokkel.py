# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm
from OTLModel.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak
from OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sokkel(AIMNaamObject):
    """Onderdeel dat zich voornamelijk voornamelijk boven het maaiveld bevindt en als doel heeft het object dat er op rust te verhogen, het object te omhullen ter bescherming of de ondergrond te nivelleren. Afhankelijk van de grootte van dat object en van de omvang van de sokkel, kan die ook zorgen voor nodige stabiliteit zoals een fundering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingGrondvlak = OTLAttribuut(field=DtuAfmetingGrondvlak,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.afmetingGrondvlak',
                                               definition='De afmeting van het grondvlak van de sokkel volgens zijn vorm.')

        self._heeftMaaibescherming = OTLAttribuut(field=BooleanField,
                                                  naam='heeftMaaibescherming',
                                                  label='heeft maaibescherming',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.heeftMaaibescherming',
                                                  definition='Geeft aan of de sokkel (en daarmee het object dat er bovenop geplaatst is) beschermd is tegen schade als gevolg van het maaien van omliggende begroeiing.')

        self._hoogteBovenMaaiveld = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='hoogteBovenMaaiveld',
                                                 label='hoogte boven het maaiveld',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.hoogteBovenMaaiveld',
                                                 definition='Hoogte in centimeters van het hoogste punt van de sokkel gemeten vanaf het maaiveld.')

        self._hoogteSokkel = OTLAttribuut(field=DtcAfmetingDiameterInCm,
                                          naam='hoogteSokkel',
                                          label='hoogte van de sokkel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.hoogteSokkel',
                                          usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                          deprecated_version='2.0.0',
                                          definition='De totale hoogte van de sokkel wanneer die rechtop staat.')

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.materiaal',
                                       definition='De grondstof waaruit de sokkel (voornamelijk) vervaardigd is.')

        self._sokkelhoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='sokkelhoogte',
                                          label='hoogte van de sokkel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.sokkelhoogte',
                                          definition='De totale hoogte van de sokkel wanneer die rechtop staat.')

    @property
    def afmetingGrondvlak(self):
        """De afmeting van het grondvlak van de sokkel volgens zijn vorm."""
        return self._afmetingGrondvlak.waarde

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)

    @property
    def heeftMaaibescherming(self):
        """Geeft aan of de sokkel (en daarmee het object dat er bovenop geplaatst is) beschermd is tegen schade als gevolg van het maaien van omliggende begroeiing."""
        return self._heeftMaaibescherming.waarde

    @heeftMaaibescherming.setter
    def heeftMaaibescherming(self, value):
        self._heeftMaaibescherming.set_waarde(value, owner=self)

    @property
    def hoogteBovenMaaiveld(self):
        """Hoogte in centimeters van het hoogste punt van de sokkel gemeten vanaf het maaiveld."""
        return self._hoogteBovenMaaiveld.waarde

    @hoogteBovenMaaiveld.setter
    def hoogteBovenMaaiveld(self, value):
        self._hoogteBovenMaaiveld.set_waarde(value, owner=self)

    @property
    def hoogteSokkel(self):
        """De totale hoogte van de sokkel wanneer die rechtop staat."""
        return self._hoogteSokkel.waarde

    @hoogteSokkel.setter
    def hoogteSokkel(self, value):
        self._hoogteSokkel.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """De grondstof waaruit de sokkel (voornamelijk) vervaardigd is."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sokkelhoogte(self):
        """De totale hoogte van de sokkel wanneer die rechtop staat."""
        return self._sokkelhoogte.waarde

    @sokkelhoogte.setter
    def sokkelhoogte(self, value):
        self._sokkelhoogte.set_waarde(value, owner=self)
