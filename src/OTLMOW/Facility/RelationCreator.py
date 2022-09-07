from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.Exceptions.CouldNotCreateRelationError import CouldNotCreateRelationError
from OTLMOW.ModelGenerator.BaseClasses.RelationValidator import RelationValidator
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Classes.Agent import Agent
from OTLMOW.OTLModel.Classes.ImplementatieElement.RelatieObject import RelatieObject
from OTLMOW.OTLModel.Classes.Onderdeel.HeeftBetrokkene import HeeftBetrokkene


class RelationCreator:
    @staticmethod
    def create_relation(bron: RelatieInteractor, doel: RelatieInteractor, relatie) -> RelatieObject:
        valid = RelationValidator.is_valid_relation(source=bron, target=doel, relation=relatie)
        if not valid:
            raise CouldNotCreateRelationError("Can't create an invalid relation, please validate relations first")
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

    @staticmethod
    def create_betrokkenerelation(bron: RelatieInteractor, doel: RelatieInteractor, relation=HeeftBetrokkene) -> RelatieObject:
        valid = RelationValidator.is_valid_relation(source=bron, target=doel, relation=relation)
        if not valid:
            raise CouldNotCreateRelationError("Can't create an invalid relation, please validate relations first")

        relatie = AssetFactory().dynamic_create_instance_from_uri(class_uri=relation.typeURI)

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
