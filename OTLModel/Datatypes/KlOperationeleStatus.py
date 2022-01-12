# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOperationeleStatus(Keuzelijst):
    """Operationele status codes."""

    def __init__(self):
        super().__init__(naam="KlOperationeleStatus",
                         label="Keuzelijst operationele status",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOperationeleStatus",
                         definition="Operationele status codes.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOperationeleStatus")

        self.add_option("actief", "actief", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief")
        self.add_option("actief-met-geplande-verwijdering", "actief met geplande verwijdering", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-geplande-verwijdering")
        self.add_option("actief-met-geplande-wijziging", "actief met geplande wijziging", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-geplande-wijziging")
        self.add_option("actief-met-tijdelijke-wijziging", "actief met tijdelijke wijziging", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-tijdelijke-wijziging")
        self.add_option("tijdelijk-actief", "tijdelijk actief", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/tijdelijk-actief")
        self.add_option("tijdelijk-inactief", "tijdelijk inactief", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/tijdelijk-inactief")
