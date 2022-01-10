from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLORelatie import OSLORelatie


class OTLGeldigeRelatieCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        logger.log("Created an instance of OTLClassCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromRelations(self):
        datablock = ['# coding=utf-8', 'from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie']

        datablock.extend(['',
                          '',
                          'class GeldigeRelatieLijst:',
                          '    def __init__(self):',
                          '        self.lijst = ['])

        for relatie in self.osloCollector.relations:
            bron = next(c.uri for c in self.osloCollector.classes if c.uri == relatie.bron_uri)
            doel = next(c.uri for c in self.osloCollector.classes if c.uri == relatie.doel_uri)
            uri = next(c.uri for c in self.osloCollector.classes if c.uri == relatie.uri)
            datablock.append(f'            GeldigeRelatie("{bron}", "{doel}", "{uri}"),')

        datablock[-1] = datablock[-1][:-1]  # remove last character of the last item in datablock

        datablock.append('        ]')
        return datablock

    @staticmethod
    def writeToFile(dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/GeldigeRelatieLijst.py"

        file = open(path, "w")
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()







