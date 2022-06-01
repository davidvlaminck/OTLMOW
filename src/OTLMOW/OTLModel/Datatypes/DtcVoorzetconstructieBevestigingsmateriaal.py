# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlVoorzetconstructieBevestigingsmateriaal import KlVoorzetconstructieBevestigingsmateriaal
from OTLMOW.OTLModel.Datatypes.KlVoorzetconstructieBevestigingsmateriaalDiameter import KlVoorzetconstructieBevestigingsmateriaalDiameter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVoorzetconstructieBevestigingsmateriaalWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._diameter = OTLAttribuut(field=KlVoorzetconstructieBevestigingsmateriaalDiameter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieBevestigingsmateriaal.diameter',
                                      definition='De diameter van de voorzetconstructie.',
                                      owner=self)

        self._materiaal = OTLAttribuut(field=KlVoorzetconstructieBevestigingsmateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieBevestigingsmateriaal.materiaal',
                                       definition='Het materiaal gebruikt bij de bevestiging van de voorzetconstructie.',
                                       owner=self)

    @property
    def diameter(self):
        """De diameter van de voorzetconstructie."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self._parent)

    @property
    def materiaal(self):
        """Het materiaal gebruikt bij de bevestiging van de voorzetconstructie."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVoorzetconstructieBevestigingsmateriaal(ComplexField, AttributeInfo):
    """Complex datatype voor de bevestigingsmaterialen van een voorzetconstructie."""
    naam = 'DtcVoorzetconstructieBevestigingsmateriaal'
    label = 'Voorzetconstructie bevestigingsmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieBevestigingsmateriaal'
    definition = 'Complex datatype voor de bevestigingsmaterialen van een voorzetconstructie.'
    waardeObject = DtcVoorzetconstructieBevestigingsmateriaalWaarden

    def __str__(self):
        return ComplexField.__str__(self)

