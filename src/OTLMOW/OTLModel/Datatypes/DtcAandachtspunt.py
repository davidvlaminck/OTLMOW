# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlAandachtspunttype import KlAandachtspunttype
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAandachtspuntWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAandachtspunt.omschrijving',
                                          definition='Een toelichting die beschrijft waar precies op gelet moet worden.',
                                          owner=self)

        self._type = OTLAttribuut(field=KlAandachtspunttype,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAandachtspunt.type',
                                  definition='Mogelijke types van het aandachtspunt.',
                                  owner=self)

    @property
    def omschrijving(self):
        """Een toelichting die beschrijft waar precies op gelet moet worden."""
        return self._omschrijving.get_waarde()

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self._parent)

    @property
    def type(self):
        """Mogelijke types van het aandachtspunt."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAandachtspunt(ComplexField, AttributeInfo):
    """Complex datatype voor iets waar speciaal op gelet moet worden, meestal in het kader van de veiligheid."""
    naam = 'DtcAandachtspunt'
    label = 'Aandachtspunt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAandachtspunt'
    definition = 'Complex datatype voor iets waar speciaal op gelet moet worden, meestal in het kader van de veiligheid.'
    waardeObject = DtcAandachtspuntWaarden

    def __str__(self):
        return ComplexField.__str__(self)

