# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.DtcGrondAfgravinguitgraving import DtcGrondAfgravinguitgraving
from OTLMOW.OTLModel.Datatypes.DtcGrondafdekking import DtcGrondafdekking
from OTLMOW.OTLModel.Datatypes.DtcGrondophoging import DtcGrondophoging
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuSoortGrondwerkWaarden(AttributeInfo, UnionWaarden):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        UnionWaarden.__init__(self)
        self._afdekking = OTLAttribuut(field=DtcGrondafdekking,
                                       naam='afdekking',
                                       label='afdekking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuSoortGrondwerk.afdekking',
                                       kardinaliteit_min='0',
                                       definition='Afdekking van grond.',
                                       owner=self)

        self._afgraving = OTLAttribuut(field=DtcGrondAfgravinguitgraving,
                                       naam='afgraving',
                                       label='afgraving',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuSoortGrondwerk.afgraving',
                                       kardinaliteit_min='0',
                                       definition='Afgraving van grond.',
                                       owner=self)

        self._ophoging = OTLAttribuut(field=DtcGrondophoging,
                                      naam='ophoging',
                                      label='ophoging',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuSoortGrondwerk.ophoging',
                                      kardinaliteit_min='0',
                                      definition='Ophoging van grond.',
                                      owner=self)

        self._uitgraving = OTLAttribuut(field=DtcGrondAfgravinguitgraving,
                                        naam='uitgraving',
                                        label='uitgraving',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuSoortGrondwerk.uitgraving',
                                        kardinaliteit_min='0',
                                        definition='Uitgraving van grond.',
                                        owner=self)

    @property
    def afdekking(self):
        """Afdekking van grond."""
        return self._afdekking.get_waarde()

    @afdekking.setter
    def afdekking(self, value):
        self._afdekking.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_afdekking')

    @property
    def afgraving(self):
        """Afgraving van grond."""
        return self._afgraving.get_waarde()

    @afgraving.setter
    def afgraving(self, value):
        self._afgraving.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_afgraving')

    @property
    def ophoging(self):
        """Ophoging van grond."""
        return self._ophoging.get_waarde()

    @ophoging.setter
    def ophoging(self, value):
        self._ophoging.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_ophoging')

    @property
    def uitgraving(self):
        """Uitgraving van grond."""
        return self._uitgraving.get_waarde()

    @uitgraving.setter
    def uitgraving(self, value):
        self._uitgraving.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_uitgraving')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuSoortGrondwerk(UnionTypeField, AttributeInfo):
    """Union datatype voor het soort werk waar de grond van afkomstig is of voor dient."""
    naam = 'DtuSoortGrondwerk'
    label = 'Soort grondwerk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuSoortGrondwerk'
    definition = 'Union datatype voor het soort werk waar de grond van afkomstig is of voor dient.'
    usagenote = 'Gebruik enkel 1 attribuut van dit Union datatype.'
    waardeObject = DtuSoortGrondwerkWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

