# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACObstakelbeveiligerType(Keuzelijst):
    """De verschillende types van obstakelbeveiliger."""

    def __init__(self):
        super().__init__(naam="KlLEACObstakelbeveiligerType",
                         label="Obstakelbeveiliger type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACObstakelbeveiligerType",
                         definition="De verschillende types van obstakelbeveiliger.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACObstakelbeveiligerType")

        self.add_option("geleidend-(R)", "geleidend (R)", "Obstakelbeveiliger brengt het voertuig niet tot stilstand maar terug in de juiste richting", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACObstakelbeveiligerType/geleidend-(R)")
        self.add_option("afstoppend-(NR)", "afstoppend (NR)", "Obstakelbeveiliger brengt het voertuig tot stilstand maar zijn niet getest op zijdelingse aanrijdingen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACObstakelbeveiligerType/afstoppend-(NR)")
