# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Fundering import Fundering
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtuAfmetingGrondvlak import DtuAfmetingGrondvlak
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Funderingsmassief(Fundering, VlakGeometrie):
    """Een fundering waarop een klein(er) object geplaatst wordt of er (in principe) onlosmakelijk in vastgezet wordt (vb.: een paal/een steun, een kleine sokkel,...) Als het grotere constructie-elementen betreft (vb.: een pijler, een gebouw,...), moeten andere onderdelen van fundering gebruikt worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Fundering.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self._afmetingGrondvlak = OTLAttribuut(field=DtuAfmetingGrondvlak,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.afmetingGrondvlak',
                                               definition='De afmetingen van het grondvlak van de fundering volgens zijn vorm.',
                                               owner=self)

        self._funderingshoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                              naam='funderingshoogte',
                                              label='funderingshoogte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.funderingshoogte',
                                              definition='De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering.',
                                              owner=self)

        self._isPermanent = OTLAttribuut(field=BooleanField,
                                         naam='isPermanent',
                                         label='is permanent',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.isPermanent',
                                         definition='Bepaalt of de fundering (en het gefundeerd object) blijvend is.',
                                         owner=self)

        self._isPrefab = OTLAttribuut(field=BooleanField,
                                      naam='isPrefab',
                                      label='is prefab',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.isPrefab',
                                      definition='Bepaalt of de fundering ter plaatse gestort is of als geprefabriceerd element aangevoerd.',
                                      owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.materiaal',
                                       definition='De grondstof waaruit het funderingsmassief gemaakt is. ',
                                       owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsmassief.volume',
                                    definition='Het volume in kubieke meter van het funderingsmassief.',
                                    owner=self)

    @property
    def afmetingGrondvlak(self):
        """De afmetingen van het grondvlak van de fundering volgens zijn vorm."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)

    @property
    def funderingshoogte(self):
        """De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."""
        return self._funderingshoogte.get_waarde()

    @funderingshoogte.setter
    def funderingshoogte(self, value):
        self._funderingshoogte.set_waarde(value, owner=self)

    @property
    def isPermanent(self):
        """Bepaalt of de fundering (en het gefundeerd object) blijvend is."""
        return self._isPermanent.get_waarde()

    @isPermanent.setter
    def isPermanent(self, value):
        self._isPermanent.set_waarde(value, owner=self)

    @property
    def isPrefab(self):
        """Bepaalt of de fundering ter plaatse gestort is of als geprefabriceerd element aangevoerd."""
        return self._isPrefab.get_waarde()

    @isPrefab.setter
    def isPrefab(self, value):
        self._isPrefab.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """De grondstof waaruit het funderingsmassief gemaakt is. """
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def volume(self):
        """Het volume in kubieke meter van het funderingsmassief."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
