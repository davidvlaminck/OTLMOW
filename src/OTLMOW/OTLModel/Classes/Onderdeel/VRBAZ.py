# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.VRModuleZFirmware import VRModuleZFirmware
from OTLMOW.OTLModel.Datatypes.KlVRBAZMerk import KlVRBAZMerk
from OTLMOW.OTLModel.Datatypes.KlVRBAZModelnaam import KlVRBAZModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRBAZ(VRModuleZFirmware):
    """Het bedien- en aanzichttoestel, ook wel bedienings- en diagnosepaneel, is ingebouwd achter een politiedeur. Het bevat een display en bedieningstoetsen om de verkeersregelaar te bedienen. 
De display van de BAZ geeft de actuele werktoestand aan, inclusief eventuele toestandswisselingen. De actieve defecten zijn onmiddellijk, zonder enige manipulatie, zichtbaar op de display. Met de bedieningsknoppen moet het werkingsregime (online, offline, handbediening, oranjegeel knipperlicht, integraal rood of volledig gedoofd) gekozen kunnen worden. Tevens moet het regime "handbediening" bediend kunnen worden met de bedieningsknoppen. Met een knop wordt er overgeschakeld naar de volgende fase. Een getuigen-LED geeft aan wanneer de overgangsfase is afgerond en er kan overgegaan worden naar de volgende fase"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBAZ'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVRBAZMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBAZ.merk',
                                  definition='De merknaam van de VR-BAZ.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVRBAZModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBAZ.modelnaam',
                                       definition='De modelnaam van de VR-BAZ.',
                                       owner=self)

    @property
    def merk(self):
        """De merknaam van de VR-BAZ."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de VR-BAZ."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
