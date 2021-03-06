# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Straatmeubilair import Straatmeubilair
from OTLMOW.OTLModel.Datatypes.KlKleurPlooibaken import KlKleurPlooibaken
from OTLMOW.OTLModel.Datatypes.KlPlooibakenType import KlPlooibakenType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Plooibaken(Straatmeubilair, PuntGeometrie):
    """Een zacht kunststoffen paal met verschillende diameter en reflecterende banden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plooibaken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Straatmeubilair.__init__(self)
        PuntGeometrie.__init__(self)

        self._kleur = OTLAttribuut(field=KlKleurPlooibaken,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plooibaken.kleur',
                                   definition='Bepaling van de kleur van het plooibaken.',
                                   owner=self)

        self._type = OTLAttribuut(field=KlPlooibakenType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plooibaken.type',
                                  definition='De diameter en vorm van het plooibaken.',
                                  owner=self)

    @property
    def kleur(self):
        """Bepaling van de kleur van het plooibaken."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def type(self):
        """De diameter en vorm van het plooibaken."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
