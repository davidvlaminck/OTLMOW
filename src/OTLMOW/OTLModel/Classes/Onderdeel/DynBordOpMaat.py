# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.LEDBord import LEDBord
from OTLMOW.OTLModel.Datatypes.KlDynBordOpMaatMerk import KlDynBordOpMaatMerk
from OTLMOW.OTLModel.Datatypes.KlDynBordOpMaatModelnaam import KlDynBordOpMaatModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordOpMaat(LEDBord):
    """Dynamisch verkeersbord dat niet standaard is; en dus niet is gespecifieerd in SB270."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')

        self._merk = OTLAttribuut(field=KlDynBordOpMaatMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat.merk',
                                  usagenote='Uit een keuzelijst.',
                                  definition='Merknaam van het dynamisch bord op maat.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordOpMaatModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat.modelnaam',
                                       usagenote='Uit een keuzelijst',
                                       definition='Modelnaam van het dynamisch bord op maat.',
                                       owner=self)

    @property
    def merk(self):
        """Merknaam van het dynamisch bord op maat."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het dynamisch bord op maat."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
