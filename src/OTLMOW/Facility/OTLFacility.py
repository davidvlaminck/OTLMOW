import json
import logging
import os
from os.path import abspath

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.FileFormats.DavieImporter import DavieImporter
from OTLMOW.Facility.FileFormats.JsonDecoder import JsonDecoder
from OTLMOW.Facility.FileFormats.JsonExporter import JsonExporter
from OTLMOW.Facility.RelatieCreator import RelatieCreator
from OTLMOW.Facility.Visualiser import Visualiser
from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
from OTLMOW.GeometrieArtefact.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OTLModelCreator import OTLModelCreator
from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader
from OTLMOW.OEFModel.ModelGrabber import ModelGrabber
from OTLMOW.OEFModel.OEFModelCreator import OEFModelCreator
from OTLMOW.OTLModel.GeldigeRelatieLijst import GeldigeRelatieLijst
from OTLMOW.PostenMapping.PostenCollector import PostenCollector
from OTLMOW.PostenMapping.PostenCreator import PostenCreator
from OTLMOW.PostenMapping.PostenInMemoryCreator import PostenInMemoryCreator


class OTLFacility:
    def __init__(self, loggingLevel: int = logging.WARNING, logfile: str = 'logs.txt',
                 enable_relation_features: bool = False,
                 settings_path: str = ''):
        self.settings: dict = {}
        if settings_path != '':
            self.load_settings(settings_path)

        if loggingLevel != 0 and logfile != '':
            logging.basicConfig(filename=logfile,
                                filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=loggingLevel)

        self.davie_importer = DavieImporter(self.settings)
        self.oef_model_creator: None | OEFModelCreator = None
        self.posten_collector = None
        self.posten_creator = None
        self.jsonExporter = JsonExporter(self.settings)
        self.encoder = OtlAssetJSONEncoder(indent=4, settings=self.settings)
        self.davieDecoder = JsonDecoder(self.settings)
        self.asset_factory = AssetFactory()
        self.relatie_validator: None | RelatieValidator = None
        self.relatie_creator: None | RelatieCreator = None
        self.visualiser = Visualiser()

        if enable_relation_features:
            self._init_relatie_validation()

    def create_datamodel(self, directory: str = '',
                         otl_sqlite_file_location: str = '',
                         geo_artefact_sqlite_file_location: str = '') -> None:
        """Creates a datamodel given an OTL SQLite database in the specified directory. This will also use a Geometry Artefact
        if specified

        :param directory: directory where the model classes will be created. If not specified, this will create a model in a
        directory OTLModel in the same directory as the script that runs this method
        :type: str
        :param otl_sqlite_file_location: path to the OTL SQLite file
        :type: str
        :param geo_artefact_sqlite_file_location: path to the Geometry Artefact SQLite file. Defaults to an empty string as this
        file is not mandatory to create a model
        :type: str

        :return: returns an instance of class_name in the given namespace, located from directory, that inherits from OTLObject
        :rtype: OTLObject or None
        """
        model_creator = self._init_otl_model_creator(otl_sqlite_file_location, geo_artefact_sqlite_file_location)
        self._create_otl_datamodel(model_creator, directory)

    # import

    # export

    # create instance

    def _init_relatie_validation(self, relation_list: [GeldigeRelatieLijst] = None):
        if relation_list is None:
            relation_list = GeldigeRelatieLijst().lijst
        self.relatie_validator = RelatieValidator(relation_list)
        self.relatie_validator.enableValidateRelatieOnRelatieInteractor()
        self.relatie_creator = RelatieCreator(self.relatie_validator)

    @staticmethod
    def _init_otl_model_creator(otl_file_location: str = '', geoA_file_location: str = '') -> OTLModelCreator:
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        geo_artefact_collector = None
        if geoA_file_location != '':
            sql_reader_GA = SQLDbReader(geoA_file_location)
            geo_memory_creator = GeometrieInMemoryCreator(sql_reader_GA)
            geo_artefact_collector = GeometrieArtefactCollector(geo_memory_creator)
        return OTLModelCreator(collector, geo_artefact_collector)

    @staticmethod
    def _create_otl_datamodel(model_creator: OTLModelCreator = None, directory: str = ''):
        model_creator.oslo_collector.collect()
        if model_creator.geo_artefact_collector is not None:
            model_creator.geo_artefact_collector.collect()
        if directory == '':
            base_dir = os.path.dirname(os.path.realpath(__file__))
            directory = abspath(f'{base_dir}/../')
        model_creator.create_full_model(directory=directory)

    def init_postenmapping_creator(self, otl_file_location):
        sql_reader = SQLDbReader(otl_file_location)
        oslo_creator = PostenInMemoryCreator(sql_reader)
        self.posten_collector = PostenCollector(oslo_creator)
        self.posten_creator = PostenCreator(self.posten_collector)

    def create_posten_model(self):
        self.posten_collector.collect()
        self.posten_creator.create_all_mappings()

    def init_oef_model_creator(self, oef_file_location, ins_ond_file_location=''):
        model_grabber = ModelGrabber()
        model_grabber.grab_models_as_json(oef_file_location, ins_ond_file_location)
        classes = model_grabber.decode_json_and_get_classes(oef_file_location)
        attributen = model_grabber.decode_json_and_get_attributen(oef_file_location)
        ins_ond_classes = model_grabber.decode_json_and_get_classes(ins_ond_file_location)
        self.extend_classes_with_ond_ins(classes, ins_ond_classes)
        ins_ond_attributen = model_grabber.decode_json_and_get_attributen(ins_ond_file_location)
        attributen.extend(ins_ond_attributen)

        self.oef_model_creator = OEFModelCreator(classes=classes, attributen=attributen)

    def create_oef_datamodel(self):
        self.oef_model_creator.create_full_model()

    @staticmethod
    def extend_classes_with_ond_ins(classes, ins_ond_classes):
        for cls in classes:
            ins_ond_cls = next((c for c in ins_ond_classes if c["uri"] == cls["uri"]), None)
            if ins_ond_cls is None:
                continue
            cls["attributen"].extend(ins_ond_cls["attributen"])

    def load_settings(self, settings_path):
        with open(settings_path) as settings_file:
            self.settings = json.load(settings_file)
