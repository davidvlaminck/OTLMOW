# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm
from OTLMOW.OTLModel.Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlakWaarden(AttributeInfo, UnionWaarden):
    def __init__(self):
        super().__init__()
        self._rechthoekig = OTLAttribuut(field=DtcAfmetingBxlInCm,
                                         naam='rechthoekig',
                                         label='rechthoekig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rechthoekig',
                                         kardinaliteit_min='0',
                                         definition='Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter.',
                                         owner=self)

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInCm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rond',
                                  kardinaliteit_min='0',
                                  definition='Afmeting van de diameter in centimeter van een rond (grond)vlak.',
                                  owner=self)

    @property
    def rechthoekig(self):
        """Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter."""
        return self._rechthoekig.waarde

    @rechthoekig.setter
    def rechthoekig(self, value):
        self._rechthoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rechthoekig')

    @property
    def rond(self):
        """Afmeting van de diameter in centimeter van een rond (grond)vlak."""
        return self._rond.waarde

    @rond.setter
    def rond(self, value):
        self._rond.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rond')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlak(UnionTypeField, AttributeInfo):
    """Datatype voor de afmeting van een (grond)vlak volgens zijn vorm."""
    naam = 'DtuAfmetingGrondvlak'
    label = 'afmeting grondvlak'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak'
    definition = 'Datatype voor de afmeting van een (grond)vlak volgens zijn vorm.'
    waardeObject = DtuAfmetingGrondvlakWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

