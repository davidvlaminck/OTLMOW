# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlVoorzetconstructieMateriaal import KlVoorzetconstructieMateriaal
from OTLMOW.OTLModel.Datatypes.KlVoorzetconstructieProfielpositie import KlVoorzetconstructieProfielpositie
from OTLMOW.OTLModel.Datatypes.KlVoorzetconstructieProfielvorm import KlVoorzetconstructieProfielvorm


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVoorzetconstructieProfielWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._materiaal = OTLAttribuut(field=KlVoorzetconstructieMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieProfiel.materiaal',
                                       definition='Het materiaal van de voorzetconstructie.',
                                       owner=self)

        self._positie = OTLAttribuut(field=KlVoorzetconstructieProfielpositie,
                                     naam='positie',
                                     label='positie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieProfiel.positie',
                                     definition='De positie van de voorzetconstructie.',
                                     owner=self)

        self._vorm = OTLAttribuut(field=KlVoorzetconstructieProfielvorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieProfiel.vorm',
                                  definition='De vorm van de voorzetconstructie.',
                                  owner=self)

    @property
    def materiaal(self):
        """Het materiaal van de voorzetconstructie."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self._parent)

    @property
    def positie(self):
        """De positie van de voorzetconstructie."""
        return self._positie.waarde

    @positie.setter
    def positie(self, value):
        self._positie.set_waarde(value, owner=self._parent)

    @property
    def vorm(self):
        """De vorm van de voorzetconstructie."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcVoorzetconstructieProfiel(ComplexField, AttributeInfo):
    """Complex datatype voor de eigenschappen van een profiel gebruikt bij een voorzetconstructie."""
    naam = 'DtcVoorzetconstructieProfiel'
    label = 'Voorzetconstructie profiel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcVoorzetconstructieProfiel'
    definition = 'Complex datatype voor de eigenschappen van een profiel gebruikt bij een voorzetconstructie.'
    waardeObject = DtcVoorzetconstructieProfielWaarden

    def __str__(self):
        return ComplexField.__str__(self)

