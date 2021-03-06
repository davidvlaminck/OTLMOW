# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLMOW.OTLModel.Datatypes.KlTypeSuppCBV import KlTypeSuppCBV


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSupplementenCBVWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.kleur',
                                   definition='De kleur van de supplementen toegevoegd aan de verharding.',
                                   owner=self)

        self._type = OTLAttribuut(field=KlTypeSuppCBV,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.type',
                                  definition='Het type van de supplementen toegevoegd aan de verharding.',
                                  owner=self)

    @property
    def kleur(self):
        """De kleur van de supplementen toegevoegd aan de verharding."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self._parent)

    @property
    def type(self):
        """Het type van de supplementen toegevoegd aan de verharding."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSupplementenCBV(ComplexField, AttributeInfo):
    """Complex datatype voor de supplementen van de CBV."""
    naam = 'DtcSupplementenCBV'
    label = 'Supplementen CBV'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV'
    definition = 'Complex datatype voor de supplementen van de CBV.'
    waardeObject = DtcSupplementenCBVWaarden

    def __str__(self):
        return ComplexField.__str__(self)

