from collections import defaultdict

from src.OTLMOW.Facility.AssetFactory import AssetFactory
from src.OTLMOW.Facility.DavieDecoder import DavieDecoder
from src.OTLMOW.Facility.DavieExporter import DavieExporter
from src.OTLMOW.Facility.Visualiser import Visualiser
from src.OTLMOW.Facility.DavieImporter import DavieImporter
from src.OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from src.OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from src.OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader
from src.OTLMOW.Loggers.AbstractLogger import AbstractLogger
from src.OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from src.OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from src.OTLMOW.ModelGenerator.OTLModelCreator import OTLModelCreator
from src.OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from src.OTLMOW.PostenMapping.PostenCollector import PostenCollector
from src.OTLMOW.PostenMapping.PostenCreator import PostenCreator
from src.OTLMOW.PostenMapping.PostenInMemoryCreator import PostenInMemoryCreator


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
        # self.relatieValidator = RelatieValidator(GeldigeRelatieLijst()) TODO not working
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

    @staticmethod
    def make_overview_of_assets(objects: [OTLObject]) -> defaultdict:
        d = defaultdict(int)
        for i in objects:
            d[i.typeURI] += 1
        return d








