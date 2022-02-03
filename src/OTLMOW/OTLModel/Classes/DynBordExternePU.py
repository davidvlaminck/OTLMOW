# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.PU import PU
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlDynBordExternePUMerk import KlDynBordExternePUMerk
from OTLMOW.OTLModel.Datatypes.KlDynBordExternePUModelnaam import KlDynBordExternePUModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordExternePU(PU):
    """Externe stuureenheid die buiten het dynamisch bord bevestigd is, in de buurt van de openbare weg. Het betreft dus geen stuureenheid in een serverroom, noch een stuureenheid op het bord zelf."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftGeintegreerdeModem = OTLAttribuut(field=BooleanField,
                                                     naam='heeftGeintegreerdeModem',
                                                     label='heeft geintegreerde modem',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.heeftGeintegreerdeModem',
                                                     definition='De PU heeft een geïntegreerde modem.',
                                                     owner=self)

        self._merk = OTLAttribuut(field=KlDynBordExternePUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.merk',
                                  definition='Het merk van de externe PU volgens een keuzelijst.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordExternePUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.modelnaam',
                                       definition='De modelnaam van de externe PU volgens een keuzelijst.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.technischeFiche',
                                             definition='Document met technische informatie over de PU.',
                                             owner=self)

    @property
    def heeftGeintegreerdeModem(self):
        """De PU heeft een geïntegreerde modem."""
        return self._heeftGeintegreerdeModem.waarde

    @heeftGeintegreerdeModem.setter
    def heeftGeintegreerdeModem(self, value):
        self._heeftGeintegreerdeModem.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de externe PU volgens een keuzelijst."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de externe PU volgens een keuzelijst."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Document met technische informatie over de PU."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
