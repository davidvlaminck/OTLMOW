# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.DtcProfileerlaag import DtcProfileerlaag
from OTLMOW.OTLModel.Datatypes.KlBVLaagtype import KlBVLaagtype
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuBVLaagtypesWaarden(AttributeInfo, UnionWaarden):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        UnionWaarden.__init__(self)
        self._laagtype = OTLAttribuut(field=KlBVLaagtype,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes.laagtype',
                                      kardinaliteit_min='0',
                                      definition='Het type van de bitumineuze verharding.',
                                      owner=self)

        self._profileerlaag = OTLAttribuut(field=DtcProfileerlaag,
                                           naam='profileerlaag',
                                           label='profileerlaag',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes.profileerlaag',
                                           kardinaliteit_min='0',
                                           definition='De laag die het profiel verbetert van de verharding.',
                                           owner=self)

    @property
    def laagtype(self):
        """Het type van de bitumineuze verharding."""
        return self._laagtype.get_waarde()

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_laagtype')

    @property
    def profileerlaag(self):
        """De laag die het profiel verbetert van de verharding."""
        return self._profileerlaag.get_waarde()

    @profileerlaag.setter
    def profileerlaag(self, value):
        self._profileerlaag.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_profileerlaag')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuBVLaagtypes(UnionTypeField, AttributeInfo):
    """Union datatype voor een laagtype anders dan de profileerlaag. Bij een profileerlaag kan men het gewicht toelichten."""
    naam = 'DtuBVLaagtypes'
    label = 'Laagtype van de bitumineuze verharding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes'
    definition = 'Union datatype voor een laagtype anders dan de profileerlaag. Bij een profileerlaag kan men het gewicht toelichten.'
    waardeObject = DtuBVLaagtypesWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

