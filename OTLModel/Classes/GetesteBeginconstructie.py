from OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLModel.Classes.Beginstuk import Beginstuk
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACPerformantieklasse import KlLEACPerformantieklasse


# Generated with OTLClassCreator
class GetesteBeginconstructie(SchokindexVoertuigkering, Beginstuk):
    """Een gecertificeerd begin aan een geleideconstructie,met als doel de ernst van een frontale botsing te reduceren aan de stroomopwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        SchokindexVoertuigkering.__init__(self)
        Beginstuk.__init__(self)
        self.performantieklasse = KeuzelijstField(naam="performantieklasse",
                                                  label="performantieklasse",
                                                  lijst=KlLEACPerformantieklasse(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie.performantieklasse",
                                                  definition="De aanduiding hoe (performantie) de beginconstructie is getest.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """De aanduiding hoe (performantie) de beginconstructie is getest."""
