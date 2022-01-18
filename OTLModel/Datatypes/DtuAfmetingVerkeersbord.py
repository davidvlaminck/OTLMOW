# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcAfmetingBxhInMm import DtcAfmetingBxhInMm
from OTLModel.Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm
from OTLModel.Datatypes.DtcAfmetingZijdeInMm import DtcAfmetingZijdeInMm
from OTLModel.Datatypes.UnionTypeField import UnionTypeField


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbordAttributen(AttributeInfo):
    def __init__(self):
        self._achthoekig = OTLAttribuut(field=DtcAfmetingZijdeInMm,
                                        naam='achthoekig',
                                        label='achthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.achthoekig',
                                        kardinaliteit_min='0',
                                        definition='De afmeting voor een achthoekig verkeersbord (zijde in millimeter).')

        self._driehoekig = OTLAttribuut(field=DtcAfmetingZijdeInMm,
                                        naam='driehoekig',
                                        label='driehoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.driehoekig',
                                        kardinaliteit_min='0',
                                        definition='De afmeting van een driehoekig verkeersbord (zijde in millimeter).')

        self._rond = OTLAttribuut(field=DtcAfmetingDiameterInMm,
                                  naam='rond',
                                  label='rond',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.rond',
                                  kardinaliteit_min='0',
                                  definition='De afmeting voor een rond verkeersbord (diameter in millimeter).')

        self._vierhoekig = OTLAttribuut(field=DtcAfmetingBxhInMm,
                                        naam='vierhoekig',
                                        label='vierhoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.vierhoekig',
                                        kardinaliteit_min='0',
                                        definition='De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter).')

        self._zeshoekig = OTLAttribuut(field=DtcAfmetingZijdeInMm,
                                       naam='zeshoekig',
                                       label='zeshoekig',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord.zeshoekig',
                                       kardinaliteit_min='0',
                                       definition='De afmeting voor een zeshoekig verkeersbord (zijde in millimeter).')

    @property
    def achthoekig(self):
        """De afmeting voor een achthoekig verkeersbord (zijde in millimeter)."""
        return self._achthoekig.waarde

    @property
    def driehoekig(self):
        """De afmeting van een driehoekig verkeersbord (zijde in millimeter)."""
        return self._driehoekig.waarde

    @property
    def rond(self):
        """De afmeting voor een rond verkeersbord (diameter in millimeter)."""
        return self._rond.waarde

    @property
    def vierhoekig(self):
        """De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter)."""
        return self._vierhoekig.waarde

    @property
    def zeshoekig(self):
        """De afmeting voor een zeshoekig verkeersbord (zijde in millimeter)."""
        return self._zeshoekig.waarde


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbord(UnionTypeField, AttributeInfo):
    """Union datatype voor de afmeting van het verkeersbord."""
    naam = 'DtuAfmetingVerkeersbord'
    label = 'Afmeting verkeersbord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord'
    definition = 'Union datatype voor de afmeting van het verkeersbord.'
    waardeObject = DtuAfmetingVerkeersbordAttributen

    def __str__(self):
        return UnionTypeField.__str__(self)

