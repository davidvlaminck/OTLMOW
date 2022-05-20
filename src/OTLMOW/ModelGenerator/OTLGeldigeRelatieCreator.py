import logging

from OTLMOW.ModelGenerator import OSLOCollector


class OTLGeldigeRelatieCreator:
    def __init__(self, osloCollector: OSLOCollector):
        logging.info("Created an instance of OTLGeldigeRelatieCreator")
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromRelations(self):
        datablock = ['# coding=utf-8', 'from OTLMOW.ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie']

        datablock.extend(['',
                          '',
                          'class GeldigeRelatieLijst:',
                          '    def __init__(self):',
                          '        self.lijst = ['])

        for relatie in self.osloCollector.relations:
            bron = next(c.objectUri for c in self.osloCollector.classes if c.objectUri == relatie.bron_uri)
            doel = next(c.objectUri for c in self.osloCollector.classes if c.objectUri == relatie.doel_uri)
            uri = next(c.objectUri for c in self.osloCollector.classes if c.objectUri == relatie.objectUri)
            datablock.append(f'            GeldigeRelatie("{bron}", "{doel}", "{uri}", "{relatie.deprecated_version}"),')

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







