from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlSignalisatieMarkeringOpvatting(Keuzelijst):
    """De markeringsopvattingen van de markering."""

    def __init__(self):
        super().__init__(naam="KlSignalisatieMarkeringOpvatting",
                         label="Signalisatie markering opvatting",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignalisatieMarkeringOpvatting",
                         definition="De markeringsopvattingen van de markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignalisatieMarkeringOpvatting")

        self.add_option("middelenverbintenis", "middelenverbintenis", "Legt de nadruk op de wijze van aanbrengen en doseringen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieMarkeringOpvatting/middelenverbintenis")
        self.add_option("resultaatsverbintenis", "resultaatsverbintenis", "Houdt in dat de doseringen niet worden vastgelegd in het bijzonder bestek maar dat de markeringen, in nieuwe toestand en gedurende de waarborgperiode voor de markering, moeten voldoen aan resultaatseisen. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieMarkeringOpvatting/resultaatsverbintenis")
