from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.Exceptions.CouldNotCreateRelation import CouldNotCreateRelation
from OTLMOW.ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Classes.Agent import Agent
from OTLMOW.OTLModel.Classes.ImplementatieElement.RelatieObject import RelatieObject
from OTLMOW.OTLModel.Classes.Onderdeel.HeeftBetrokkene import HeeftBetrokkene


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

        relatie.assetId.identificator = bron.assetId.identificator + '_-_' + doel.assetId.identificator
        relatie.assetId.toegekendDoor = 'OTLMOW'

        if relatie.bronAssetId.toegekendDoor != 'AWV':
            relatie.bron.typeURI = bron.typeURI
        if relatie.doelAssetId.toegekendDoor != 'AWV':
            relatie.doel.typeURI = doel.typeURI
        return relatie

    def create_betrokkenerelation(self, bron: RelatieInteractor, doel: RelatieInteractor, relatie=HeeftBetrokkene) -> RelatieObject:
        if not self.validator.validateRelatieByURI(bron, doel, relatie):
            raise CouldNotCreateRelation("Can't create an invalid relation, please validate relations first")

        relatie = AssetFactory().dynamic_create_instance_from_uri(class_uri=relatie.typeURI)

        if isinstance(bron, Agent):
            relatie.bronAssetId.identificator = bron.agentId.identificator
            relatie.bronAssetId.toegekendDoor = bron.agentId.toegekendDoor
        else:
            relatie.bronAssetId.identificator = bron.assetId.identificator
            relatie.bronAssetId.toegekendDoor = bron.assetId.toegekendDoor

        relatie.doelAssetId.identificator = doel.agentId.identificator
        relatie.doelAssetId.toegekendDoor = doel.agentId.toegekendDoor

        relatie.assetId.identificator = relatie.bronAssetId.identificator + '_-_' + relatie.doelAssetId.identificator
        relatie.assetId.toegekendDoor = 'OTLMOW'

        #if relatie.bronAssetId.toegekendDoor != 'AWV':
        relatie.bron.typeURI = bron.typeURI
        #if relatie.doelAssetId.toegekendDoor != 'AWV':
        relatie.doel.typeURI = doel.typeURI
        return relatie
