# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.LEDBord import LEDBord
from OTLMOW.OTLModel.Datatypes.KlDynBordPKMerk import KlDynBordPKMerk
from OTLMOW.OTLModel.Datatypes.KlDynBordPKModelnaam import KlDynBordPKModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordPK(LEDBord):
    """Dynamisch verkeersbord dat een Pijl of Kruis verkeersteken kan afbeelden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')

        self._merk = OTLAttribuut(field=KlDynBordPKMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK.merk',
                                  definition='Merk van het dynamische bord.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordPKModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK.modelnaam',
                                       definition='Modelnaam van het PK-bord.',
                                       owner=self)

    @property
    def merk(self):
        """Merk van het dynamische bord."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het PK-bord."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
