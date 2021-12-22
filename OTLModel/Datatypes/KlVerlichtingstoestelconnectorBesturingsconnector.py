from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVerlichtingstoestelconnectorBesturingsconnector(Keuzelijst):
    """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""

    def __init__(self):
        super().__init__(naam="KlVerlichtingstoestelconnectorBesturingsconnector",
                         label="WV-besturingsconnector",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelconnectorBesturingsconnector",
                         definition="Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelconnectorBesturingsconnector")

        self.add_option("NEMA", "NEMA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/NEMA")
        self.add_option("SR", "SR", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/SR")
