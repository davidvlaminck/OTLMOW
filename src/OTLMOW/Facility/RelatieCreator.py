from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.Exceptions.CouldNotCreateRelation import CouldNotCreateRelation
from OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Classes.RelatieObject import RelatieObject


class RelatieCreator:
    def __init__(self, validator: RelatieValidator):
        self.validator = validator

    def create_relation(self, bron: RelatieInteractor, doel: RelatieInteractor, relatie) -> RelatieObject:
        if not self.validator.validateRelatieByURI(bron, doel, relatie):
            raise CouldNotCreateRelation("Can't create an invalid relation, please validate relations first")
        relatie = AssetFactory().dynamic_create_instance_from_uri(class_uri=relatie.typeURI)
        relatie.bronAssetId.identificator = bron.assetId.identificator
        relatie.bronAssetId.toegekendDoor = bron.assetId.toegekendDoor
        relatie.doelAssetId.identificator = doel.assetId.identificator
        relatie.doelAssetId.toegekendDoor = doel.assetId.toegekendDoor
        return relatie