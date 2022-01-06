# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.Software import Software
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlIVRIBaseline import KlIVRIBaseline


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVRIComponent(Software):
    """Abstracte die eigenschappen van de iVRI (intelligente verkeersregelaar) component bundelt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.baseline = KeuzelijstField(naam="baseline",
                                        label="baseline",
                                        lijst=KlIVRIBaseline(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.baseline",
                                        definition="Specificatieversie van het protocol waarop de iVRI component werkt.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Specificatieversie van het protocol waarop de iVRI component werkt."""

        self.certificaat = DtcDocument()
        """Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. """
        self.certificaat.naam = "certificaat"
        self.certificaat.label = "certificaat"
        self.certificaat.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent.certificaat"
        self.certificaat.definition = "Certificaat van de keuringsinstantie dat wordt uitgereikt aan een iVRI (intelligente verkeersregelaar) component. "
        self.certificaat.constraints = ""
        self.certificaat.usagenote = ""
        self.certificaat.deprecated_version = ""
