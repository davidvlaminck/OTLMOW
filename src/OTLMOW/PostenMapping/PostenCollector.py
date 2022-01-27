from src.OTLMOW.PostenMapping.StandaardPost import StandaardPost
from src.OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping


class PostenCollector:
    def __init__(self, postenInMemoryCreator):
        self.postenInMemoryCreator = postenInMemoryCreator
        self.standaardposten = [StandaardPost]
        self.standaardpostmappings = [StandaardPostMapping]

    def collect(self):
        self.standaardposten = self.postenInMemoryCreator.getAllStandaardposten()
        self.standaardpostmappings = self.postenInMemoryCreator.getAllStandaardPostMappings()

    def find_mappings_by_postnummer(self, nummer: str) -> [StandaardPostMapping]:
        return list(filter(lambda m: m.standaardpostnummer == nummer, self.standaardpostmappings))
