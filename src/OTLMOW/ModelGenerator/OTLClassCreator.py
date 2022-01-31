from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie
from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
from OTLMOW.GeometrieArtefact.GeometrieInheritanceProcessor import GeometrieInheritanceProcessor
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie
from OTLMOW.Loggers.AbstractLogger import AbstractLogger
from OTLMOW.Loggers.LogType import LogType
from OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector


class OTLClassCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector, geoACollector: GeometrieArtefactCollector = None):
        super().__init__(logger, osloCollector)
        logger.log("Created an instance of OTLClassCreator", LogType.INFO)
        self.osloCollector = osloCollector
        self.geoACollector = geoACollector
        self.geometry_types = []

        if geoACollector is not None:
            gip = GeometrieInheritanceProcessor(classes=osloCollector.classes,
                                                geometrie_types=self.geoACollector.geometrie_types,
                                                inheritances=self.osloCollector.inheritances)
            self.geometry_types = gip.process_inheritances()

    def CreateBlockToWriteFromClasses(self, osloClass: OSLOClass):
        if not isinstance(osloClass, OSLOClass):
            raise ValueError(f"Input is not a OSLOClass")

        if osloClass.objectUri == '' or not (
                osloClass.objectUri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/') or osloClass.objectUri.startswith(
            'http://purl.org/dc/terms')):
            raise ValueError(f"OSLOClass.objectUri is invalid. Value = '{osloClass.objectUri}'")

        if osloClass.name == '':
            raise ValueError(f"OSLOClass.name is invalid. Value = '{osloClass.name}'")

        return self.CreateBlockToWriteFromClass(osloClass)

    def CreateBlockToWriteFromClass(self, osloClass: OSLOClass):
        attributen = self.osloCollector.FindAttributesByClass(osloClass)
        inheritances = self.osloCollector.FindInheritancesByClass(osloClass)

        if osloClass.objectUri in ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject',
                                   'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject']:
            inheritances.append(
                Inheritance(base_name='AttributeInfo', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='OTLAsset', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='RelatieInteractor', base_uri='', class_name='', class_uri='', deprecated_version=''))

        elif osloClass.objectUri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject':
            inheritances.append(
                Inheritance(base_name='AttributeInfo', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='OTLObject', base_uri='', class_name='', class_uri='', deprecated_version=''))

        elif osloClass.objectUri == 'http://purl.org/dc/terms/Agent':
            inheritances.append(
                Inheritance(base_name='AttributeInfo', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='OTLObject', base_uri='', class_name='', class_uri='', deprecated_version=''))
            inheritances.append(
                Inheritance(base_name='RelatieInteractor', base_uri='', class_name='', class_uri='', deprecated_version=''))

        datablock = ['# coding=utf-8', 'from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut']

        if osloClass.abstract == 1:
            if len(inheritances) > 0:
                datablock.append('from abc import abstractmethod')
            else:
                datablock.append('from abc import abstractmethod, ABC')

        if len(inheritances) > 0:
            for inheritance in inheritances:
                if inheritance.base_name in ['OTLAsset', 'OTLObject', 'RelatieInteractor', 'AttributeInfo']:
                    datablock.append(f'from OTLMOW.OTLModel.BaseClasses.{inheritance.base_name} import {inheritance.base_name}')
                else:
                    datablock.append(f'from OTLMOW.OTLModel.Classes.{inheritance.base_name} import {inheritance.base_name}')

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getFieldsToImportFromListOfAttributes(attributen)
        for typeField in listOfFields:
            datablock.append(f'from OTLMOW.OTLModel.Datatypes.{typeField} import {typeField}')

        listOfGeometryTypes = self.getGeometryTypesFromUri(osloClass.objectUri)
        for GeometryType in listOfGeometryTypes:
            datablock.append(f'from OTLMOW.GeometryArtefact.{GeometryType.__name__} import {GeometryType.__name__}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(self.getClassLineFromClassAndInheritances(osloClass, inheritances, listOfGeometryTypes))
        datablock.append(f'    """{osloClass.definition}"""')
        datablock.append('')
        datablock.append(f"    typeURI = '{osloClass.objectUri}'")
        datablock.append('    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""')

        if osloClass.deprecated_version != '':
            datablock.append('')
            datablock.append(f"    deprecated_version = '{osloClass.deprecated_version}'")

        datablock.append('')
        if osloClass.abstract == 1:
            datablock.append('    @abstractmethod')
        datablock.append('    def __init__(self):')
        if len(inheritances) + len(listOfGeometryTypes) == 1:
            datablock.append('        super().__init__()')
            datablock.append('')
        elif len(inheritances) + len(listOfGeometryTypes) > 1:
            for inheritance in sorted(inheritances, key=lambda a: a.base_name):
                datablock.append(f'        {inheritance.base_name}.__init__(self)')
            for geo_type in sorted(listOfGeometryTypes, key=lambda a: a.__name__):
                datablock.append(f'        {geo_type.__name__}.__init__(self)')
            datablock.append('')

        self.add_attributen_to_dataBlock(attributen, datablock, forClassUse=True)
        if len(inheritances) == 0 and len(attributen) == 0:
            datablock.append('        pass')

        if datablock[-1] == '':
            datablock.pop()

        return datablock

    def getClassLineFromClassAndInheritances(self, osloClass, inheritances, geometry_types):
        if osloClass.abstract == 0 and len(inheritances) == 0:
            raise NotImplementedError(f"{osloClass.objectUri} class structure not implemented")
        if osloClass.abstract == 1 and len(inheritances) == 0:
            return f'class {osloClass.name}(ABC):'
        if len(inheritances) > 0:
            line = f'class {osloClass.name}('
            for inheritance in inheritances:
                line += inheritance.base_name + ', '
            for geometry_type in geometry_types:
                line += geometry_type.__name__ + ', '
            line = line[:-2]
            line += '):'
            return line

        raise NotImplementedError(f"{osloClass.objectUri} class structure not implemented")

    def getGeometryTypesFromUri(self, objectUri):
        if len(self.geometry_types) == 0:
            return []

        geom_type = next((g for g in self.geometry_types if g.objectUri == objectUri), None)
        if geom_type is None:
            return []

        geom_types = []
        if geom_type.geen_geometrie == 1:
            geom_types.append(GeenGeometrie)
        if geom_type.punt3D == 1:
            geom_types.append(PuntGeometrie)
        if geom_type.lijn3D == 1:
            geom_types.append(LijnGeometrie)
        if geom_type.polygoon3D == 1:
            geom_types.append(VlakGeometrie)

        return geom_types
