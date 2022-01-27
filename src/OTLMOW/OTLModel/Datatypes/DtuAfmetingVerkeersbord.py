# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxhInMm import DtcAfmetingBxhInMm
from OTLMOW.OTLModel.Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm
from OTLMOW.OTLModel.Datatypes.DtcAfmetingZijdeInMm import DtcAfmetingZijdeInMm
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbordWaarden(AttributeInfo, UnionWaarden):
    def __init__(self):
        super().__init__()
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

    @achthoekig.setter
    def achthoekig(self, value):
        self._achthoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_achthoekig')

    @property
    def driehoekig(self):
        """De afmeting van een driehoekig verkeersbord (zijde in millimeter)."""
        return self._driehoekig.waarde

    @driehoekig.setter
    def driehoekig(self, value):
        self._driehoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_driehoekig')

    @property
    def rond(self):
        """De afmeting voor een rond verkeersbord (diameter in millimeter)."""
        return self._rond.waarde

    @rond.setter
    def rond(self, value):
        self._rond.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_rond')

    @property
    def vierhoekig(self):
        """De afmeting voor een vierhoekig verkeersbord (breedte en hoogte in millimeter)."""
        return self._vierhoekig.waarde

    @vierhoekig.setter
    def vierhoekig(self, value):
        self._vierhoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_vierhoekig')

    @property
    def zeshoekig(self):
        """De afmeting voor een zeshoekig verkeersbord (zijde in millimeter)."""
        return self._zeshoekig.waarde

    @zeshoekig.setter
    def zeshoekig(self, value):
        self._zeshoekig.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_zeshoekig')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuAfmetingVerkeersbord(UnionTypeField, AttributeInfo):
    """Union datatype voor de afmeting van het verkeersbord."""
    naam = 'DtuAfmetingVerkeersbord'
    label = 'Afmeting verkeersbord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuAfmetingVerkeersbord'
    definition = 'Union datatype voor de afmeting van het verkeersbord.'
    waardeObject = DtuAfmetingVerkeersbordWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

