# coding=utf-8
from OTLModel.Classes.VRModuleZFirmware import VRModuleZFirmware
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVRBAZMerk import KlVRBAZMerk
from OTLModel.Datatypes.KlVRBAZModelnaam import KlVRBAZModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRBAZ(VRModuleZFirmware):
    """Het bedien- en aanzichttoestel, ook wel bedienings- en diagnosepaneel, is ingebouwd achter een politiedeur. Het bevat een display en bedieningstoetsen om de verkeersregelaar te bedienen. 
De display van de BAZ geeft de actuele werktoestand aan, inclusief eventuele toestandswisselingen. De actieve defecten zijn onmiddellijk, zonder enige manipulatie, zichtbaar op de display. Met de bedieningsknoppen moet het werkingsregime (online, offline, handbediening, oranjegeel knipperlicht, integraal rood of volledig gedoofd) gekozen kunnen worden. Tevens moet het regime "handbediening" bediend kunnen worden met de bedieningsknoppen. Met een knop wordt er overgeschakeld naar de volgende fase. Een getuigen-LED geeft aan wanneer de overgangsfase is afgerond en er kan overgegaan worden naar de volgende fase"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBAZ"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlVRBAZMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBAZ.merk",
                                    definition="De merknaam van de VR-BAZ.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam van de VR-BAZ."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlVRBAZModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBAZ.modelnaam",
                                         definition="De modelnaam van de VR-BAZ.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de VR-BAZ."""
