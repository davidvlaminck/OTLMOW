# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm
from OTLMOW.OTLModel.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sokkel(AIMNaamObject, VlakGeometrie):
    """Onderdeel dat zich voornamelijk voornamelijk boven het maaiveld bevindt en als doel heeft het object dat er op rust te verhogen, het object te omhullen ter bescherming of de ondergrond te nivelleren. Afhankelijk van de grootte van dat object en van de omvang van de sokkel, kan die ook zorgen voor nodige stabiliteit zoals een fundering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verankering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom')

        self._afmetingGrondvlak = OTLAttribuut(field=DtuAfmetingGrondvlak,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.afmetingGrondvlak',
                                               definition='De afmeting van het grondvlak van de sokkel volgens zijn vorm.',
                                               owner=self)

        self._heeftMaaibescherming = OTLAttribuut(field=BooleanField,
                                                  naam='heeftMaaibescherming',
                                                  label='heeft maaibescherming',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.heeftMaaibescherming',
                                                  definition='Geeft aan of de sokkel (en daarmee het object dat er bovenop geplaatst is) beschermd is tegen schade als gevolg van het maaien van omliggende begroeiing.',
                                                  owner=self)

        self._hoogteBovenMaaiveld = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='hoogteBovenMaaiveld',
                                                 label='hoogte boven het maaiveld',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.hoogteBovenMaaiveld',
                                                 definition='Hoogte in centimeters van het hoogste punt van de sokkel gemeten vanaf het maaiveld.',
                                                 owner=self)

        self._hoogteSokkel = OTLAttribuut(field=DtcAfmetingDiameterInCm,
                                          naam='hoogteSokkel',
                                          label='hoogte van de sokkel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.hoogteSokkel',
                                          usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                          deprecated_version='2.0.0',
                                          definition='De totale hoogte van de sokkel wanneer die rechtop staat.',
                                          owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.materiaal',
                                       definition='De grondstof waaruit de sokkel (voornamelijk) vervaardigd is.',
                                       owner=self)

        self._sokkelhoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='sokkelhoogte',
                                          label='hoogte van de sokkel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel.sokkelhoogte',
                                          definition='De totale hoogte van de sokkel wanneer die rechtop staat.',
                                          owner=self)

    @property
    def afmetingGrondvlak(self):
        """De afmeting van het grondvlak van de sokkel volgens zijn vorm."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)

    @property
    def heeftMaaibescherming(self):
        """Geeft aan of de sokkel (en daarmee het object dat er bovenop geplaatst is) beschermd is tegen schade als gevolg van het maaien van omliggende begroeiing."""
        return self._heeftMaaibescherming.get_waarde()

    @heeftMaaibescherming.setter
    def heeftMaaibescherming(self, value):
        self._heeftMaaibescherming.set_waarde(value, owner=self)

    @property
    def hoogteBovenMaaiveld(self):
        """Hoogte in centimeters van het hoogste punt van de sokkel gemeten vanaf het maaiveld."""
        return self._hoogteBovenMaaiveld.get_waarde()

    @hoogteBovenMaaiveld.setter
    def hoogteBovenMaaiveld(self, value):
        self._hoogteBovenMaaiveld.set_waarde(value, owner=self)

    @property
    def hoogteSokkel(self):
        """De totale hoogte van de sokkel wanneer die rechtop staat."""
        return self._hoogteSokkel.get_waarde()

    @hoogteSokkel.setter
    def hoogteSokkel(self, value):
        self._hoogteSokkel.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """De grondstof waaruit de sokkel (voornamelijk) vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sokkelhoogte(self):
        """De totale hoogte van de sokkel wanneer die rechtop staat."""
        return self._sokkelhoogte.get_waarde()

    @sokkelhoogte.setter
    def sokkelhoogte(self, value):
        self._sokkelhoogte.set_waarde(value, owner=self)
