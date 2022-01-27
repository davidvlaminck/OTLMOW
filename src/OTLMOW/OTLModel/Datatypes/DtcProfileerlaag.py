# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.KlBVLaagtype import KlBVLaagtype
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfileerlaagWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.gewicht',
                                     definition='Het gewicht van de profileerlaag in ton.')

        self._laagtype = OTLAttribuut(field=KlBVLaagtype,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag.laagtype',
                                      definition='Het type van de bitumineuze verharding.')

    @property
    def gewicht(self):
        """Het gewicht van de profileerlaag in ton."""
        return self._gewicht.waarde

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self._parent)

    @property
    def laagtype(self):
        """Het type van de bitumineuze verharding."""
        return self._laagtype.waarde

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcProfileerlaag(ComplexField, AttributeInfo):
    """Complex datatype om extra informatie te capteren van de profilerende laag."""
    naam = 'DtcProfileerlaag'
    label = 'Profileerlaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcProfileerlaag'
    definition = 'Complex datatype om extra informatie te capteren van de profilerende laag.'
    waardeObject = DtcProfileerlaagWaarden

    def __str__(self):
        return ComplexField.__str__(self)

