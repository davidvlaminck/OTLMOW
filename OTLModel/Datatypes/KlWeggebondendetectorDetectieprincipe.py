# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorDetectieprincipe(Keuzelijst):
    """Keuzelijst met de verschillende gangbare manieren waarop een weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler."""

    def __init__(self):
        super().__init__(naam="KlWeggebondendetectorDetectieprincipe",
                         label="Weggebondendetector detectieprincipe",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorDetectieprincipe",
                         definition="Keuzelijst met de verschillende gangbare manieren waarop een weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorDetectieprincipe")

        self.add_option("inductief", "inductief", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/inductief")
        self.add_option("doppler", "doppler", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/doppler")
        self.add_option("infrarood", "infrarood", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/infrarood")
        self.add_option("infrarood+inductief", "infrarood+inductief", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/infrarood+inductief")
