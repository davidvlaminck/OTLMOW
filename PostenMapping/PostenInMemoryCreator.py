from ModelGenerator.SQLDbReader import SQLDbReader
from PostenMapping.StandaardPost import StandaardPost
from PostenMapping.StandaardPostMapping import StandaardPostMapping


class PostenInMemoryCreator:
    def __init__(self, sQLDbReader: SQLDbReader):
        self.sqlDbReader = sQLDbReader

    def getAllStandaardposten(self):
        data = self.sqlDbReader.performReadQuery(
            'SELECT DISTINCT Standaardpostnummer, Standaardpostbeschrijving, StandaardpostMeetstaateenheid FROM "Mapping SB250"',
            {})

        lijst = []
        for row in data:
            c = StandaardPost(row[0], row[1], row[2])
            lijst.append(c)

        return lijst

    def getAllStandaardPostMappings(self):
        data = self.sqlDbReader.performReadQuery(
            'SELECT TypeURI, AttribuutURI, Dotnotatie, DefaultWaarde, "Range", UsageNote, IsMeetstaatAttr, IsAltijdInTeVullen, IsBasisMapping, MappingStatus, MappingOpmerking, Standaardpostnummer FROM "Mapping SB250"',
            {})

        lijst = []
        for row in data:
            c = StandaardPostMapping(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
            lijst.append(c)

        return lijst


