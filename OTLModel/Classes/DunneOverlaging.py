# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KlDunneOverlagingType import KlDunneOverlagingType
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon


# Generated with OTLClassCreator. To modify: extend, do not edit
class DunneOverlaging(AndereLaag, AttributeInfo):
    """Een dunne overlaging kan bestaan uit een SME overlaging of een antisliplaag."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        AttributeInfo.__init__(self)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.gewicht',
                                     definition='Het gewicht van de dunne overlaging in ton.')

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.kleur',
                                   definition='De kleur van de dunne overlaging.')

        self._type = OTLAttribuut(field=KlDunneOverlagingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.type',
                                  definition='Het type SME overlaging of antisliplaag.')

    @property
    def gewicht(self):
        """Het gewicht van de dunne overlaging in ton."""
        return self._gewicht.waarde

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De kleur van de dunne overlaging."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type SME overlaging of antisliplaag."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
