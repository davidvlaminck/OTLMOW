# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.KlCompacteBatterijMerk import KlCompacteBatterijMerk
from OTLMOW.OTLModel.Datatypes.KlCompacteBatterijModelnaam import KlCompacteBatterijModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLMOW.OTLModel.Datatypes.KwantWrdInmAh import KwantWrdInmAh


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCompacteBatterijWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._capaciteit = OTLAttribuut(field=KwantWrdInmAh,
                                        naam='capaciteit',
                                        label='capaciteit',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcCompacteBatterij.capaciteit',
                                        definition='De hoeveelheid stroom die een batterij over een bepaalde tijd kan leveren in mAh.',
                                        owner=self)

        self._ingebruikname = OTLAttribuut(field=DateField,
                                           naam='ingebruikname',
                                           label='ingebruikname',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcCompacteBatterij.ingebruikname',
                                           definition='De dag dat de batterij in bruik werd genomen.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlCompacteBatterijMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcCompacteBatterij.merk',
                                  definition='Het merk van de compacte batterij.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCompacteBatterijModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcCompacteBatterij.modelnaam',
                                       definition='De modelnaam van de compacte batterij.',
                                       owner=self)

        self._spanning = OTLAttribuut(field=KwantWrdInVolt,
                                      naam='spanning',
                                      label='spanning',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcCompacteBatterij.spanning',
                                      definition='De elektrische spanning van de batterij in Volt.',
                                      owner=self)

    @property
    def capaciteit(self):
        """De hoeveelheid stroom die een batterij over een bepaalde tijd kan leveren in mAh."""
        return self._capaciteit.get_waarde()

    @capaciteit.setter
    def capaciteit(self, value):
        self._capaciteit.set_waarde(value, owner=self._parent)

    @property
    def ingebruikname(self):
        """De dag dat de batterij in bruik werd genomen."""
        return self._ingebruikname.get_waarde()

    @ingebruikname.setter
    def ingebruikname(self, value):
        self._ingebruikname.set_waarde(value, owner=self._parent)

    @property
    def merk(self):
        """Het merk van de compacte batterij."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self._parent)

    @property
    def modelnaam(self):
        """De modelnaam van de compacte batterij."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self._parent)

    @property
    def spanning(self):
        """De elektrische spanning van de batterij in Volt."""
        return self._spanning.get_waarde()

    @spanning.setter
    def spanning(self, value):
        self._spanning.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCompacteBatterij(ComplexField, AttributeInfo):
    """Complex datatype waarmee de informatie, zoals merk, modelnaam, spanning, enz..., van de compacte batterij wordt verzameld."""
    naam = 'DtcCompacteBatterij'
    label = 'Compacte batterij'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcCompacteBatterij'
    definition = 'Complex datatype waarmee de informatie, zoals merk, modelnaam, spanning, enz..., van de compacte batterij wordt verzameld.'
    waardeObject = DtcCompacteBatterijWaarden

    def __str__(self):
        return ComplexField.__str__(self)

