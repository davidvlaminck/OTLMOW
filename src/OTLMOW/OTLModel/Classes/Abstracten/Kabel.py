# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlKabelFabrikant import KlKabelFabrikant
from OTLMOW.OTLModel.Datatypes.KlKabelmantelKleur import KlKabelmantelKleur
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabel(AIMNaamObject, LijnGeometrie):
    """Abstracte voor attributen en relaties van allerlei types kabels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._buitenmantelDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                  naam='buitenmantelDiameter',
                                                  label='buitenmantel diameter',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.buitenmantelDiameter',
                                                  definition='De buitenste afmeting van de kabel in millimeter.',
                                                  owner=self)

        self._buitenmantelKleur = OTLAttribuut(field=KlKabelmantelKleur,
                                               naam='buitenmantelKleur',
                                               label='buitenmantel kleur',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.buitenmantelKleur',
                                               definition='De hoofdkleur(en) die voor een waarnemer onmiddellijk zichtbaar is (zijn) zonder de kabel te ontmantelen, de kleur van de markeringen op die buitenste mantel buiten beschouwing gelaten.',
                                               owner=self)

        self._fabrikant = OTLAttribuut(field=KlKabelFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.fabrikant',
                                       definition='De naam van de producent van de kabel.',
                                       owner=self)

    @property
    def buitenmantelDiameter(self):
        """De buitenste afmeting van de kabel in millimeter."""
        return self._buitenmantelDiameter.get_waarde()

    @buitenmantelDiameter.setter
    def buitenmantelDiameter(self, value):
        self._buitenmantelDiameter.set_waarde(value, owner=self)

    @property
    def buitenmantelKleur(self):
        """De hoofdkleur(en) die voor een waarnemer onmiddellijk zichtbaar is (zijn) zonder de kabel te ontmantelen, de kleur van de markeringen op die buitenste mantel buiten beschouwing gelaten."""
        return self._buitenmantelKleur.get_waarde()

    @buitenmantelKleur.setter
    def buitenmantelKleur(self, value):
        self._buitenmantelKleur.set_waarde(value, owner=self)

    @property
    def fabrikant(self):
        """De naam van de producent van de kabel."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)
