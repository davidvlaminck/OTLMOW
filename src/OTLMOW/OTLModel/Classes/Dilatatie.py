# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlLEACUitzettingswaardeDilatatie import KlLEACUitzettingswaardeDilatatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dilatatie(AIMObject):
    """Dilataties zijn bedoeld om ervoor te zorgen dat bouwconstructies vrij kunnen krimpen en uitzetten bij onder andere temperatuurwisselingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._uitzettingswaarde = OTLAttribuut(field=KlLEACUitzettingswaardeDilatatie,
                                               naam='uitzettingswaarde',
                                               label='Uitzettingswaarde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie.uitzettingswaarde',
                                               definition='De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing.')

    @property
    def uitzettingswaarde(self):
        """De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing."""
        return self._uitzettingswaarde.waarde

    @uitzettingswaarde.setter
    def uitzettingswaarde(self, value):
        self._uitzettingswaarde.set_waarde(value, owner=self)
