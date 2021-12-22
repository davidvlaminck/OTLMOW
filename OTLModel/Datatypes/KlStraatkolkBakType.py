from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlStraatkolkBakType(Keuzelijst):
    """Het type van bak van de straatkolk."""

    def __init__(self):
        super().__init__(naam="KlStraatkolkBakType",
                         label="Straatkolk bak type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkBakType",
                         definition="Het type van bak van de straatkolk.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkBakType")

        self.add_option("geprefabriceerde-betonnen-bak-type-II", "geprefabriceerde betonnen bak type II", "geprefabriceerde betonnen bak type II", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/geprefabriceerde-betonnen-bak-type-II")
        self.add_option("infiltratiekolk-type-1", "Infiltratiekolk type 1", "Infiltratiekolk type 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/infiltratiekolk-type-1")
        self.add_option("gietijzeren-bak", "gietijzeren bak", "gietijzeren bak", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/gietijzeren-bak")
        self.add_option("infiltratiekolk-type-2", "Infiltratiekolk type 2", "Infiltratiekolk type 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/infiltratiekolk-type-2")
        self.add_option("gemetst", "gemetst", "gemetst", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/gemetst")
        self.add_option("geprefabriceerde-betonnen-bak-type-I", "geprefabriceerde betonnen bak type I", "geprefabriceerde betonnen bak type I", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/geprefabriceerde-betonnen-bak-type-I")
        self.add_option("infiltratiekolk-type-1-2", "Infiltratiekolk type 1+", "Infiltratiekolk type 1+", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/infiltratiekolk-type-1-2")
