from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlGeotextielType import KlGeotextielType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geotextiel(AndereLaag):
    """Geotextiel om grondoppervlakken, taluds en/of bodems te beschermen tegen
 erosie door wind, golfslag en/of stroming van water, afkomstig hetzij van afstromende neerslag, hetzij
 van afvloeiend oppervlaktewater."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftVulling = BooleanField(naam="heeftVulling",
                                         label="heeft vulling",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.heeftVulling",
                                         definition="Aanduiding of er vulling zoals bv. houtsnippers, grind,... in een omhulsel van geotextiel aanwezig is.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Aanduiding of er vulling zoals bv. houtsnippers, grind,... in een omhulsel van geotextiel aanwezig is."""

        self.isBiodegradeerbaar = BooleanField(naam="isBiodegradeerbaar",
                                               label="is biodegradeerbaar",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.isBiodegradeerbaar",
                                               definition="Aanduiding of het geotextiel al dan niet biologisch degradeerbaar is.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Aanduiding of het geotextiel al dan niet biologisch degradeerbaar is."""

        self.isIngezaaid = BooleanField(naam="isIngezaaid",
                                        label="is ingezaaid",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.isIngezaaid",
                                        definition="Aanduiding of er in het geotextiel zaden aanwezig zijn.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Aanduiding of er in het geotextiel zaden aanwezig zijn."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.technischeFiche"
        technischeFicheField.definition = "De technische fiche van het geotextiel."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = ""
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van het geotextiel."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlGeotextielType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.type",
                                    definition="Het type geotextiel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type geotextiel."""
