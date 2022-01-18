# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm
from OTLModel.Datatypes.DtcAfmetingDiameterInCm import DtcAfmetingDiameterInCm
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlakAttributen(AttributeInfo):
    def __init__(self):
        self._rechthoekig = OTLAttribuut(field=DtcAfmetingBxlInCm,
                                         naam='rechthoekig',
                                         label='rechthoekig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rechthoekig',
                                         definition='Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter.')

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInCm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak.rond',
                                  definition='Afmeting van de diameter in centimeter van een rond (grond)vlak.')

    @property
    def rechthoekig(self):
        """Afmetingen voor breedte en lengte of diepte. De breedte meet van links naar rechts in vooraanzicht, de lengte van voor naar achter."""
        return self._rechthoekig.waarde

    @property
    def rond(self):
        """Afmeting van de diameter in centimeter van een rond (grond)vlak."""
        return self._rond.waarde


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingGrondvlak(UnionTypeField, AttributeInfo):
    """Datatype voor de afmeting van een (grond)vlak volgens zijn vorm."""
    naam = 'DtuAfmetingGrondvlak'
    label = 'afmeting grondvlak'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingGrondvlak'
    definition = 'Datatype voor de afmeting van een (grond)vlak volgens zijn vorm.'
    waardeObject = DtuAfmetingGrondvlakAttributen

    def __str__(self):
        return UnionTypeField.__str__(self)

