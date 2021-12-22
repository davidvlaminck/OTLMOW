from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDwarseMarkeringSoort(Keuzelijst):
    """Soorten van dwarse markering."""

    def __init__(self):
        super().__init__(naam="KlDwarseMarkeringSoort",
                         label="Dwarse markering soort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringSoort",
                         definition="Soorten van dwarse markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringSoort")

        self.add_option("stopstreep-(Alg)", "stopstreep (Alg)", "Een stopstreep is een witte streep die dwars op de rijbaan is aangebracht. Het geeft aan waar de bestuurders moeten stoppen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/stopstreep-(Alg)")
        self.add_option("stopstreep-(OFOS)", "stopstreep (OFOS)", "Een stopstreep bij de opgeblazen fietsopstelstrook (OFOS).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/stopstreep-(OFOS)")
        self.add_option("voetgangers-oversteekplaats-(VOP)", "voetgangers-oversteekplaats (VOP)", "Een locatie op de rijbaan die bestemd is voor voetgangers om over te steken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/voetgangers-oversteekplaats-(VOP)")
        self.add_option("verdrijvingsvlak-(Arcering)", "verdrijvingsvlak (Arcering)", "Keuzelijst voor het bepalen van het type van dwarse markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/verdrijvingsvlak-(Arcering)")
        self.add_option("driehoek-(Haaientand)", "driehoek (Haaientand)", "Haaietanden is een markering die de bestuurders aangeeft om voorrang te verlenen aan bestuurders op de kruisende weg.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/driehoek-(Haaientand)")
        self.add_option("parkeerstrook", "parkeerstrook", "Een gemarkeerde parkeergelegenheid langs een rijweg.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/parkeerstrook")
        self.add_option("afremmingsstreep", "afremmingsstreep", "Ribbelvlak bestaande uit een aantal permanente dwarse lijnen, ook afremmingsstrepen genoemd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/afremmingsstreep")
        self.add_option("dambord", "dambord", "Een dambord bakent de plaats af voorbehouden aan voertuigen van geregelde diensten voor gemeenschappelijk vervoer op een bijzondere overrijdbare bedding of de plaats die eigen beddingen en bijzondere overrijdbare beddingen met elkaar verbinden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/dambord")
        self.add_option("fietsoversteekplaats-met-blokken-(FOP)", "fietsoversteekplaats met blokken (FOP)", "Een oversteekplaats voor fietsers gemarkeerd door witte blokken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/fietsoversteekplaats-met-blokken-(FOP)")
        self.add_option("fietsoversteekplaats-met-lijnen-(FOPL)", "fietsoversteekplaats met lijnen (FOPL)", "Een oversteekplaats voor fietsers gemarkeerd door witte evenwijdige lijnen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/fietsoversteekplaats-met-lijnen-(FOPL)")
        self.add_option("verkeersdrempel-markering", "verkeersdrempel markering", "?", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/verkeersdrempel-markering")
        self.add_option("onderbroken-verbindingsmarkering", "onderbroken verbindingsmarkering", "Markering om de geleiding voor de fietsers te verbeteren en het attentieniveau van een afdraaiend voertuig ten opzichte van de fietsers te verhogen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/onderbroken-verbindingsmarkering")
