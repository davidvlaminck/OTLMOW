from Facility.AssetFactory import AssetFactory
from Facility.DavieDecoder import DavieDecoder
from Facility.DavieExporter import DavieExporter
from Facility.Visualiser import Visualiser
from Loggers.AbstractLogger import AbstractLogger
from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLModel.GeldigeRelatieLijst import GeldigeRelatieLijst
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from ModelGenerator.OTLModelCreator import OTLModelCreator
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from ModelGenerator.SQLDbReader import SQLDbReader
from Facility.DavieImporter import DavieImporter
from PostenMapping.PostenCollector import PostenCollector
from PostenMapping.PostenCreator import PostenCreator
from PostenMapping.PostenInMemoryCreator import PostenInMemoryCreator


class OTLFacility:
    def __init__(self, instanceLogger: AbstractLogger):
        self.davieImporter = DavieImporter()
        self.logger = instanceLogger
        self.collector = None
        self.modelCreator = None
        self.posten_collector = None
        self.posten_creator = None
        self.davieExporter = DavieExporter()
        self.encoder = OtlAssetJSONEncoder(indent=4)
        self.davieDecoder = DavieDecoder()
        self.asset_factory = AssetFactory()
        self.relatieValidator = RelatieValidator(GeldigeRelatieLijst())
        self.visualiser = Visualiser()

    def init_otl_model_creator(self, otl_file_location):
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        self.collector = OSLOCollector(oslo_creator)
        self.modelCreator = OTLModelCreator(self.logger, self.collector)

    def create_otl_datamodel(self):
        self.collector.collect()
        self.modelCreator.create_full_model()

    def init_postenmapping_creator(self, otl_file_location):
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = PostenInMemoryCreator(sql_reader)
        self.posten_collector = PostenCollector(oslo_creator)
        self.posten_creator = PostenCreator(self.logger, self.posten_collector)

    def create_posten_model(self):
        self.posten_collector.collect()
        self.posten_creator.create_all_mappings()








