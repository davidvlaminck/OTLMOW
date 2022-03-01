# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcExterneReferentieWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._externReferentienummer = OTLAttribuut(field=StringField,
                                                    naam='externReferentienummer',
                                                    label='extern referentienummer',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie.externReferentienummer',
                                                    definition='Referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ...',
                                                    owner=self)

        self._externePartij = OTLAttribuut(field=StringField,
                                           naam='externePartij',
                                           label='externe partij',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie.externePartij',
                                           definition='De naam van de externe partij waarvoor de referentie geldt. Dit kan een organisatie zijn maar ook een softwaretoepassing zoals bv. ABBA of VLCC.',
                                           owner=self)

    @property
    def externReferentienummer(self):
        """Referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ..."""
        return self._externReferentienummer.waarde

    @externReferentienummer.setter
    def externReferentienummer(self, value):
        self._externReferentienummer.set_waarde(value, owner=self._parent)

    @property
    def externePartij(self):
        """De naam van de externe partij waarvoor de referentie geldt. Dit kan een organisatie zijn maar ook een softwaretoepassing zoals bv. ABBA of VLCC."""
        return self._externePartij.waarde

    @externePartij.setter
    def externePartij(self, value):
        self._externePartij.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcExterneReferentie(ComplexField, AttributeInfo):
    """Complex datatype waarmee een referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ... kan toegevoegd worden aan object."""
    naam = 'DtcExterneReferentie'
    label = 'Externe referentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie'
    definition = 'Complex datatype waarmee een referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ... kan toegevoegd worden aan object.'
    waardeObject = DtcExterneReferentieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

