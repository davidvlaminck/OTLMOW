from Loggers.AbstractLogger import AbstractLogger
from ModelGenerator.FileExistChecker import FileExistChecker
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OTLModelCreator import OTLModelCreator
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from ModelGenerator.SQLDbReader import SQLDbReader


class OTLFacility:
    def __init__(self, instanceLogger: AbstractLogger):
        self.logger = instanceLogger
        self.collector = None
        self.modelCreator = None
        self.encoder = OtlAssetJSONEncoder(indent=4)

    def init_otl_model_creator(self, otl_file_location):
        file_exist_checker = FileExistChecker(otl_file_location)
        if not (file_exist_checker.fileFound()):
            raise FileNotFoundError(file_exist_checker.path + " is not a valid path. File does not exist.")
        sql_reader = SQLDbReader(file_exist_checker)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        self.collector = OSLOCollector(oslo_creator)
        self.modelCreator = OTLModelCreator(self.logger, self.collector)

    def create_otl_datamodel(self):
        self.collector.collect()
        self.modelCreator.create_full_model()

