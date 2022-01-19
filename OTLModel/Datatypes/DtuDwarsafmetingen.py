# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm
from OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingenWaarden(AttributeInfo, UnionWaarden):
    def __init__(self):
        self._rechthoekig = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                         naam='rechthoekig',
                                         label='rechthoekig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rechthoekig',
                                         kardinaliteit_min='0',
                                         definition='Afmetingen voor breedte, lengte en hoogte van een rechthoekig object.')

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInMm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rond',
                                  kardinaliteit_min='0',
                                  definition='Afmeting van de diameter in milimeter van een rond object.')

    @property
    def rechthoekig(self):
        """Afmetingen voor breedte, lengte en hoogte van een rechthoekig object."""
        return self._rechthoekig.waarde

    @rechthoekig.setter
    def rechthoekig(self, value):
        self._rechthoekig.set_waarde(value)
        if value is not None:
            self.clear_other_props('_rechthoekig')

    @property
    def rond(self):
        """Afmeting van de diameter in milimeter van een rond object."""
        return self._rond.waarde

    @rond.setter
    def rond(self, value):
        self._rond.set_waarde(value)
        if value is not None:
            self.clear_other_props('_rond')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingen(UnionTypeField, AttributeInfo):
    """Union datatype voor de dwarsafmetingen van een object volgens zijn vorm."""
    naam = 'DtuDwarsafmetingen'
    label = 'Dwarsafmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen'
    definition = 'Union datatype voor de dwarsafmetingen van een object volgens zijn vorm.'
    waardeObject = DtuDwarsafmetingenWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

