# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingenAttributen(AttributeInfo):
    def __init__(self):
        self._rechthoekig = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                         naam='rechthoekig',
                                         label='rechthoekig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rechthoekig',
                                         definition='Afmetingen voor breedte, lengte en hoogte van een rechthoekig object.')

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInMm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen.rond',
                                  definition='Afmeting van de diameter in milimeter van een rond object.')

    @property
    def rechthoekig(self):
        """Afmetingen voor breedte, lengte en hoogte van een rechthoekig object."""
        return self._rechthoekig.waarde

    @property
    def rond(self):
        """Afmeting van de diameter in milimeter van een rond object."""
        return self._rond.waarde


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuDwarsafmetingen(UnionTypeField, AttributeInfo):
    """Union datatype voor de dwarsafmetingen van een object volgens zijn vorm."""
    naam = 'DtuDwarsafmetingen'
    label = 'Dwarsafmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuDwarsafmetingen'
    definition = 'Union datatype voor de dwarsafmetingen van een object volgens zijn vorm.'
    waardeObject = DtuDwarsafmetingenAttributen

    def __str__(self):
        return UnionTypeField.__str__(self)

