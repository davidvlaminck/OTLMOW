# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from UnitTests.TestClasses.OTLModel.Datatypes.KwantWrdTest import KwantWrdTest
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuTestUnionTypeWaarden(AttributeInfo, UnionWaarden):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        UnionWaarden.__init__(self)
        self._unionKwantWrd = OTLAttribuut(field=KwantWrdTest,
                                           naam='unionKwantWrd',
                                           label='Union kwantitatieve waarde',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionKwantWrd',
                                           kardinaliteit_min='0',
                                           definition='Kwantitatieve waarde van het test Union datatype',
                                           owner=self)

        self._unionString = OTLAttribuut(field=StringField,
                                         naam='unionString',
                                         label='Union tekstveld',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString',
                                         kardinaliteit_min='0',
                                         definition='Vrij tekstveld van het test Union datatype',
                                         owner=self)

    @property
    def unionKwantWrd(self):
        """Kwantitatieve waarde van het test Union datatype"""
        return self._unionKwantWrd.get_waarde()

    @unionKwantWrd.setter
    def unionKwantWrd(self, value):
        self._unionKwantWrd.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_unionKwantWrd')

    @property
    def unionString(self):
        """Vrij tekstveld van het test Union datatype"""
        return self._unionString.get_waarde()

    @unionString.setter
    def unionString(self, value):
        self._unionString.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_unionString')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuTestUnionType(UnionTypeField, AttributeInfo):
    """Union datatype voor test doeleinden."""
    naam = 'DtuTestUnionType'
    label = 'Test UnionType'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType'
    definition = 'Union datatype voor test doeleinden.'
    waardeObject = DtuTestUnionTypeWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

