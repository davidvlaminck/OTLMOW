from OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACObstakelbeveiligerType import KlLEACObstakelbeveiligerType
from OTLModel.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau


# Generated with OTLClassCreator. To modify: extend, do not edit
class Obstakelbeveiliger(SchokindexVoertuigkering, AfschermendeConstructie):
    """Een energie-absorberende constructie voor voertuigen,geïnstalleerd vóór één of meerdere obstakels,met als doel de ernst van een botsing te reduceren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        SchokindexVoertuigkering.__init__(self)
        AfschermendeConstructie.__init__(self)

        self.performantieniveau = KeuzelijstField(naam="performantieniveau",
                                                  label="performantieniveau",
                                                  lijst=KlLEACPerformantieniveau(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.performantieniveau",
                                                  definition="Het niveau waarop de obstakelbeveiliger is getest.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Het niveau waarop de obstakelbeveiliger is getest."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLEACObstakelbeveiligerType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.type",
                                    definition="De functie die de obstakelbeveiliger vervult.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De functie die de obstakelbeveiliger vervult."""
