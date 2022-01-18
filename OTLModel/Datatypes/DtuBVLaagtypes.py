# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcProfileerlaag import DtcProfileerlaag
from OTLModel.Datatypes.KlBVLaagtype import KlBVLaagtype
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuBVLaagtypesAttributen(AttributeInfo):
    def __init__(self):
        self._laagtype = OTLAttribuut(field=KlBVLaagtype,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes.laagtype',
                                      kardinaliteit_min='0',
                                      definition='Het type van de bitumineuze verharding.')

        self._profileerlaag = OTLAttribuut(field=DtcProfileerlaag,
                                           naam='profileerlaag',
                                           label='profileerlaag',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes.profileerlaag',
                                           kardinaliteit_min='0',
                                           definition='De laag die het profiel verbetert van de verharding.')

    @property
    def laagtype(self):
        """Het type van de bitumineuze verharding."""
        return self._laagtype.waarde

    @property
    def profileerlaag(self):
        """De laag die het profiel verbetert van de verharding."""
        return self._profileerlaag.waarde


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuBVLaagtypes(UnionTypeField, AttributeInfo):
    """Union datatype voor een laagtype anders dan de profileerlaag. Bij een profileerlaag kan men het gewicht toelichten."""
    naam = 'DtuBVLaagtypes'
    label = 'Laagtype van de bitumineuze verharding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuBVLaagtypes'
    definition = 'Union datatype voor een laagtype anders dan de profileerlaag. Bij een profileerlaag kan men het gewicht toelichten.'
    waardeObject = DtuBVLaagtypesAttributen

    def __str__(self):
        return UnionTypeField.__str__(self)

