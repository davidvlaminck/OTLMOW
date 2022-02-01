from collections import defaultdict

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.DavieDecoder import DavieDecoder
from OTLMOW.Facility.DavieExporter import DavieExporter
from OTLMOW.Facility.Visualiser import Visualiser
from OTLMOW.Facility.DavieImporter import DavieImporter
from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
from OTLMOW.GeometrieArtefact.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader
from OTLMOW.Loggers.AbstractLogger import AbstractLogger
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLModelCreator import OTLModelCreator
from OTLMOW.OEFModel.ModelGrabber import ModelGrabber
from OTLMOW.OEFModel.OEFModelCreator import OEFModelCreator
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from OTLMOW.PostenMapping.PostenCollector import PostenCollector
from OTLMOW.PostenMapping.PostenCreator import PostenCreator
from OTLMOW.PostenMapping.PostenInMemoryCreator import PostenInMemoryCreator


class OTLFacility:
    def __init__(self, instanceLogger: AbstractLogger):
        self.davieImporter = DavieImporter()
        self.logger = instanceLogger
        self.collector = None
        self.geoAcollector = None
        self.modelCreator = None
        self.oef_model_creator = None
        self.posten_collector = None
        self.posten_creator = None
        self.davieExporter = DavieExporter()
        self.encoder = OtlAssetJSONEncoder(indent=4)
        self.davieDecoder = DavieDecoder()
        self.asset_factory = AssetFactory()
        # self.relatieValidator = RelatieValidator(GeldigeRelatieLijst()) TODO not working
        self.visualiser = Visualiser()

    def init_otl_model_creator(self, otl_file_location, geoA_file_location=''):
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        self.collector = OSLOCollector(oslo_creator)
        if geoA_file_location != '':
            sql_reader_GA = SQLDbReader(geoA_file_location)
            geo_memory_creator = GeometrieInMemoryCreator(sql_reader_GA)
            self.geoAcollector = GeometrieArtefactCollector(geo_memory_creator)
        self.modelCreator = OTLModelCreator(self.logger, self.collector, self.geoAcollector)

    def create_otl_datamodel(self):
        self.collector.collect()
        if self.geoAcollector is not None:
            self.geoAcollector.collect()
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

    def init_oef_model_creator(self, oef_file_location, ins_ond_file_location=''):
        model_grabber = ModelGrabber()
        model_grabber.grab_models_as_json(oef_file_location, ins_ond_file_location)
        classes = model_grabber.decode_json_and_get_classes(oef_file_location)
        attributen = model_grabber.decode_json_and_get_attributen(oef_file_location)
        ins_ond_classes = model_grabber.decode_json_and_get_classes(ins_ond_file_location)
        self.extend_classes_with_ond_ins(classes, ins_ond_classes)
        ins_ond_attributen = model_grabber.decode_json_and_get_attributen(ins_ond_file_location)
        attributen.extend(ins_ond_attributen)

        self.oef_model_creator = OEFModelCreator(self.logger, classes=classes, attributen=attributen)

    def create_oef_datamodel(self):
        self.oef_model_creator.create_full_model()

    def extend_classes_with_ond_ins(self, classes, ins_ond_classes):
        for cls in classes:
            ins_ond_cls = next((c for c in ins_ond_classes if c["uri"] == cls["uri"]), None)
            if ins_ond_cls is None:
                continue
            cls["attributen"].extend(ins_ond_cls["attributen"])









