# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarCoordinatiewijze(Keuzelijst):
    """Keuzelijst met de voorkomende manieren van coordinate voor verkeersregelaars."""

    def __init__(self):
        super().__init__(naam="KlVerkeersregelaarCoordinatiewijze",
                         label="Verkeersregelaar coordinatiewijze",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarCoordinatiewijze",
                         definition="Keuzelijst met de voorkomende manieren van coordinate voor verkeersregelaars.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarCoordinatiewijze")

        self.add_option("centraal", "centraal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/centraal")
        self.add_option("geen", "geen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/geen")
        self.add_option("its-app", "ITS-app", "Coordinatie door ITS-app.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/its-app")
        self.add_option("klok", "klok", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/klok")
        self.add_option("master", "master", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/master")
        self.add_option("pulsen", "pulsen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/pulsen")
        self.add_option("slave", "slave", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/slave")
