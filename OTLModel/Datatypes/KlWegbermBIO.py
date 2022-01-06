# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermBIO(Keuzelijst):
    """Bijzonder ingerichte onderdelen van de wegbermen."""

    def __init__(self):
        super().__init__(naam="KlWegbermBIO",
                         label="Wegberm BIO",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermBIO",
                         definition="Bijzonder ingerichte onderdelen van de wegbermen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermBIO")

        self.add_option("bijzondere-bedding", "bijzondere bedding", "Gedeelte van de wegberm, uitsluitend bestemd voor voertuigen van het openbaar vervoer en andere toegelaten voertuigen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/bijzondere-bedding")
        self.add_option("ruiterpad", "ruiterpad", "Gedeelte van de wegberm, bestemd voor ruiters en als zodanig aangeduid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/ruiterpad")
        self.add_option("fietspad", "fietspad", "Gedeelte van het wegplatform, dat bestemd is voor fietsers en bromfietsers en als zodanig aangeduid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/fietspad")
        self.add_option("voetpad", "voetpad", "Gedeelte van de wegberm, bestemd voor voetgangers.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/voetpad")
        self.add_option("verkeerseiland", "verkeerseiland", "Heeft als doel het verkeer te geleiden en kan verhoogd zijn.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/verkeerseiland")
        self.add_option("vluchtheuvel", "vluchtheuvel", "Verkeersheuvel ten behoeve van voetgangers.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/vluchtheuvel")
