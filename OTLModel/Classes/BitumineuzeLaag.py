# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.LaagBouwklasse import LaagBouwklasse
from OTLModel.Datatypes.DtuBVLaagtypes import DtuBVLaagtypes
from OTLModel.Datatypes.KlBVBindmiddel import KlBVBindmiddel
from OTLModel.Datatypes.KlBVMengseltype import KlBVMengseltype
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class BitumineuzeLaag(LaagBouwklasse, AttributeInfo):
    """Flexibele verharding die meestal uit bitumineus gebonden materialen (asfalt of gietasfalt) bestaat en laagsgewijs wordt aangelegd. ."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        LaagBouwklasse.__init__(self)

        self._bindmiddelType = OTLAttribuut(field=KlBVBindmiddel,
                                            naam='bindmiddelType',
                                            label='bindmiddel type',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.bindmiddelType',
                                            definition='Het bindmiddeltype van de bitumineuze laag.')

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.kleur',
                                   definition='De kleur van de bitumineuze laag.')

        self._laagtype = OTLAttribuut(field=DtuBVLaagtypes,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.laagtype',
                                      definition='Het type van bitumineuze laag.')

        self._mengseltype = OTLAttribuut(field=KlBVMengseltype,
                                         naam='mengseltype',
                                         label='mengseltype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.mengseltype',
                                         definition='Het type van het (giet)asfaltmengsel.')

    @property
    def bindmiddelType(self):
        """Het bindmiddeltype van de bitumineuze laag."""
        return self._bindmiddelType.waarde

    @bindmiddelType.setter
    def bindmiddelType(self, value):
        self._bindmiddelType.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De kleur van de bitumineuze laag."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def laagtype(self):
        """Het type van bitumineuze laag."""
        return self._laagtype.waarde

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self)

    @property
    def mengseltype(self):
        """Het type van het (giet)asfaltmengsel."""
        return self._mengseltype.waarde

    @mengseltype.setter
    def mengseltype(self, value):
        self._mengseltype.set_waarde(value, owner=self)
