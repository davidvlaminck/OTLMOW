from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBVBindmiddel(Keuzelijst):
    """De mogelijke bindmiddelen bij de bitumineuze verharding."""

    def __init__(self):
        super().__init__(naam="KlBVBindmiddel",
                         label="BV bindmiddel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBVBindmiddel",
                         definition="De mogelijke bindmiddelen bij de bitumineuze verharding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVBindmiddel")

        self.add_option("niet-gespecifieerd-(keuze-van-de-aannemer)", "niet gespecifieerd (keuze van de aannemer)", "niet gespecifieerd (keuze van de aannemer)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/niet-gespecifieerd-(keuze-van-de-aannemer)")
        self.add_option("gewoon-wegenbitumen", "gewoon wegenbitumen", "gewoon wegenbitumen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/gewoon-wegenbitumen")
        self.add_option("polymeerbitumen", "polymeerbitumen", "polymeerbitumen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/polymeerbitumen")
        self.add_option("hard-bitumen-B-10-20-of-B15-25", "hard bitumen B 10-20 of B15-25", "hard bitumen B 10/20 of B15/25", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/hard-bitumen-B-10-20-of-B15-25")
        self.add_option("gewoon-wegenbitumen-met-natuurbitumen", "gewoon wegenbitumen met natuurbitumen", "gewoon wegenbitumen met natuurbitumen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/gewoon-wegenbitumen-met-natuurbitumen")
        self.add_option("bindmiddel-met-positief-indringingsgetal", "bindmiddel met positief indringingsgetal", "bindmiddel met positief indringingsgetal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/bindmiddel-met-positief-indringingsgetal")
        self.add_option("pigmenteerbaar-bitumen", "pigmenteerbaar bitumen", "pigmenteerbaar bitumen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/pigmenteerbaar-bitumen")
        self.add_option("kleurloos-synthetisch-bindmiddel", "kleurloos synthetisch bindmiddel", "kleurloos synthetisch bindmiddel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/kleurloos-synthetisch-bindmiddel")
        self.add_option("met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel", "met polymeren gemodificeerd kleurloos synthetisch bindmiddel", "met polymeren gemodificeerd kleurloos synthetisch bindmiddel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel")
        self.add_option("bindmiddel-met-additieven", "bindmiddel met additieven", "bindmiddel met additieven", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/bindmiddel-met-additieven")
