from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLORelatie import OSLORelatie


class OTLGeldigeRelatieCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        logger.log("Created an instance of OTLClassCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromRelations(self):
        list_classes_to_import = []
        list_of_relaties = []
        datablock = ['# coding=utf-8', 'from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie']

        list_classes_to_import = list(map(lambda r: r.bron_uri, self.osloCollector.relations))
        list_classes_to_import.extend(list(map(lambda r: r.doel_uri, self.osloCollector.relations)))
        list_classes_to_import.extend(list(map(lambda r: r.uri, self.osloCollector.relations)))

        distinct_class_list = list(set(list_classes_to_import))

        classes_to_import_list = []
        for classuri in distinct_class_list:
            cls = next(c.name for c in self.osloCollector.classes if c.uri == classuri)
            classes_to_import_list.append(cls)
        sorted_classes_to_import_list = sorted(classes_to_import_list, key=lambda c: c)

        for class_to_import in sorted_classes_to_import_list:
            datablock.append(f'from OTLModel.Classes.{class_to_import} import {class_to_import}')

        datablock.extend(['',
                          '',
                          'class GeldigeRelatieLijst:',
                          '    def __init__(self):',
                          '        self.lijst = ['])

        for relatie in self.osloCollector.relations:
            bron = next(c.name for c in self.osloCollector.classes if c.uri == relatie.bron_uri)
            doel = next(c.name for c in self.osloCollector.classes if c.uri == relatie.doel_uri)
            uri = next(c.name for c in self.osloCollector.classes if c.uri == relatie.uri)
            datablock.append(f'            GeldigeRelatie({bron}, {doel}, {uri}),')

        datablock[-1] = datablock[-1][:-1] # remove last character of the last item in datablock

        datablock.append('        ]')
        return datablock

    @staticmethod
    def writeToFile(dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/GeldigeRelatieLijst.py"

        file = open(path, "w")
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()







