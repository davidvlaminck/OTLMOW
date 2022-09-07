# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereLaag import AndereLaag
from OTLMOW.OTLModel.Datatypes.KlDunneOverlagingType import KlDunneOverlagingType
from OTLMOW.OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLMOW.OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DunneOverlaging(AndereLaag, VlakGeometrie):
    """Een dunne overlaging kan bestaan uit een SME overlaging of een antisliplaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.gewicht',
                                     definition='Het gewicht van de dunne overlaging in ton.',
                                     owner=self)

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.kleur',
                                   definition='De kleur van de dunne overlaging.',
                                   owner=self)

        self._type = OTLAttribuut(field=KlDunneOverlagingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.type',
                                  definition='Het type SME overlaging of antisliplaag.',
                                  owner=self)

    @property
    def gewicht(self):
        """Het gewicht van de dunne overlaging in ton."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De kleur van de dunne overlaging."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type SME overlaging of antisliplaag."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
