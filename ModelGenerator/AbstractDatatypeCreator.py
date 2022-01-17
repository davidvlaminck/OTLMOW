import os
from abc import ABC

from Loggers.AbstractLogger import AbstractLogger
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.StringHelper import wrap_in_quotes


class AbstractDatatypeCreator(ABC):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        self.logger = logger
        self.osloCollector = osloCollector

    def getTypeLinkFromAttribuut(self, attribuut):
        typeLink = self.osloCollector.FindTypeLinkByUri(attribuut.type)
        if typeLink is not None:
            return typeLink.item_tabel

    @staticmethod
    def getSingleFieldFromTypeUri(fieldType: str):
        if fieldType.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/') and '#' in fieldType:
            return fieldType.split('#')[1]
        match fieldType:
            case None:
                return ''
            case 'http://www.w3.org/2001/XMLSchema#decimal':
                return 'FloatOrDecimalField'
            case 'http://www.w3.org/2001/XMLSchema#string':
                return 'StringField'
            case 'http://www.w3.org/2001/XMLSchema#boolean':
                return 'BooleanField'
            case 'http://www.w3.org/2001/XMLSchema#integer':
                return 'IntegerField'
            case 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger':
                return 'NonNegIntegerField'
            case 'http://www.w3.org/2001/XMLSchema#date':
                return 'DateField'
            case 'http://www.w3.org/2001/XMLSchema#dateTime':
                return 'DateTimeField'
            case 'http://www.w3.org/2001/XMLSchema#time':
                return 'TimeField'
            case 'http://www.w3.org/2001/XMLSchema#anyURI':
                return 'URIField'
            case 'https://schema.org/OpeningHoursSpecification':
                return 'DtcOpeningsurenSpecificatie'
            case                'https://schema.org/ContactPoint':
                return 'DtcContactinfo'

        raise NotImplemented('not supported fieldType in getSingleFieldFromTypeUri()')

    @staticmethod
    def getNonSingleFieldFromTypeUri(fieldType: str):
        if '#Dtc' in fieldType:
            typeName = fieldType[fieldType.find("#") + 1::]
            return ['ComplexField', typeName]
        if fieldType.startswith("https://schema.org/"):
            if fieldType == "https://schema.org/ContactPoint":
                return ['ComplexField', "DtcContactinfo"]
            if fieldType == "https://schema.org/OpeningHoursSpecification":
                return ['ComplexField', "DtcOpeningsurenSpecificatie"]
            raise NotImplementedError(f"Field of type {fieldType} is not implemented in DatatypeCreator")
        if '#Dte' in fieldType or '#KwantWrd' in fieldType:
            typeName = fieldType[fieldType.find("#") + 1::]
            return ['ComplexField', typeName]
        if '#Kl' in fieldType:
            typeName = fieldType[fieldType.find("#") + 1::]
            return ['KeuzelijstField', typeName]
        if '#Dtu' in fieldType:
            typeName = fieldType[fieldType.find("#") + 1::]
            return ['UnionTypeField', typeName]

        raise NotImplemented(f'not supported fieldType {fieldType} in getNonSingleFieldFromTypeUri()')

    @staticmethod
    def writeToFile(datatype, directory: str, dataToWrite: list[str], relativePath=''):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        path = f"{base_dir}/../OTLModel/{directory}/{datatype.name}.py"

        file = open(path, "w", encoding='utf-8')
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()

    def getFieldsToImportFromListOfAttributes(self, attributen, listToStartFrom=None):
        if listToStartFrom is None:
            listToStartFrom = []
        if len(attributen) == 0:
            return listToStartFrom

        collectedList = []
        collectedList.extend(listToStartFrom)

        for attribuut in attributen:
            typeLink = self.getTypeLinkFromAttribuut(attribuut)
            if typeLink == "OSLOEnumeration":
                collectedList.append(self.getTypeNameOfEnumUri(attribuut.type))
            elif typeLink == "OSLODatatypePrimitive":
                collectedList.append(self.getSingleFieldFromTypeUri(attribuut.type))
            elif typeLink == "OSLODatatypeComplex":
                collectedList.append(self.getTypeNameOfComplexAttribuut(attribuut.type))
            elif typeLink == "OSLODatatypeUnion":
                collectedList.append(self.getTypeNameOfUnionAttribuut(attribuut.type))
            else:
                raise not NotImplementedError(f"{typeLink.item_tabel} not implemented")

        distinct_types_list = list(set(collectedList))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list

    def getFieldsAndNamesFromListOfAttributes(self, attributen):
        if len(attributen) == 0:
            return []

        primitiveTypesList = list(filter(lambda t: t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))
        otherTypesList = list(filter(lambda t: not t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))

        select_types_list = list(map(lambda a: (self.getSingleFieldFromTypeUri(a.type), a.name), primitiveTypesList))

        for nonPrimitiveType in otherTypesList:
            select_types_list.append((self.getFieldNameFromTypeUri(nonPrimitiveType.type), nonPrimitiveType.name))

        distinct_types_list = list(set(select_types_list))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list

    @staticmethod
    def getWhiteSpaceEquivalent(string):
        return ''.join(' ' * len(string))

    def getFieldNameFromTypeUri(self, attribuutType):
        if attribuutType.startswith('http://www.w3.org/2001/XMLSchema#'):
            return self.getSingleFieldFromTypeUri(attribuutType)
        if attribuutType.startswith("https://schema.org/"):
            return self.getNonSingleFieldFromTypeUri(attribuutType)[1]
        return self.getNonSingleFieldFromTypeUri(attribuutType)[1]

    @staticmethod
    def getTypeNameOfEnumUri(type_uri: str):
        return type_uri.split('#')[1]

    def getTypeNameOfUnionAttribuut(self, type_uri: str):
        if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/"):
            return type_uri[type_uri.find("#") + 1::]

        raise NotImplementedError(f"getTypeNameOfComplexAttribuut fails to get typename from {type_uri}")

    def getTypeNameOfComplexAttribuut(self, type_uri: str):
        if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/") or type_uri.startswith(
                "http://www.w3.org/2001/XMLSchema#"):
            return type_uri[type_uri.find("#") + 1::]
        elif type_uri.startswith("https://schema.org/"):
            if type_uri == "https://schema.org/ContactPoint":
                return "DtcContactinfo"
            if type_uri == "https://schema.org/OpeningHoursSpecification":
                return "DtcOpeningsurenSpecificatie"
            raise NotImplementedError(
                f"Field of type {type_uri} is not implemented in DatatypeCreator.getTypeNameOfComplexAttribuut")

        raise NotImplementedError(f"getTypeNameOfComplexAttribuut fails to get typename from {type_uri}")

    def CreateBlockToWriteFromComplexOrUnionTypes(self, osloDatatypeComplex, ComplexOrUnionTypeField='ComplexField'):
        if ComplexOrUnionTypeField == 'ComplexField':
            attributen = self.osloCollector.FindComplexDatatypeAttributenByClassUri(osloDatatypeComplex.objectUri)
        else:
            attributen = self.osloCollector.FindUnionDatatypeAttributenByClassUri(osloDatatypeComplex.objectUri)

        datablock = ['# coding=utf-8',
                     'from OTLModel.BaseClasses.AttributeInfo import AttributeInfo',
                     'from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut']

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getFieldsToImportFromListOfAttributes(attributen, [f'{ComplexOrUnionTypeField}'])
        for typeField in listOfFields:
            datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        WaardenString = 'Waarden'
        if ComplexOrUnionTypeField!='ComplexField':
            WaardenString = 'Attributen'
        datablock.append(f'class {osloDatatypeComplex.name}{WaardenString}(AttributeInfo):')
        datablock.append('    def __init__(self):')

        self.addAttributenToDataBlock(attributen, datablock, forUnionTypeUse=not(ComplexOrUnionTypeField=='ComplexField'))

        datablock.append(''),
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(f'class {osloDatatypeComplex.name}({ComplexOrUnionTypeField}, AttributeInfo):'),
        datablock.append(f'    """{osloDatatypeComplex.definition_nl}"""'),
        datablock.append(f'    naam = {wrap_in_quotes(osloDatatypeComplex.name)}'),
        datablock.append(f'    label = {wrap_in_quotes(osloDatatypeComplex.label_nl)}'),
        datablock.append(f'    objectUri = {wrap_in_quotes(osloDatatypeComplex.objectUri)}'),
        datablock.append(f'    definition = {wrap_in_quotes(osloDatatypeComplex.definition_nl)}'),
        if osloDatatypeComplex.usagenote_nl != '':
            datablock.append(f'    usagenote_nl = {wrap_in_quotes(osloDatatypeComplex.usagenote_nl)}'),
        if osloDatatypeComplex.deprecated_version != '':
            datablock.append(f'    deprecated_version = {wrap_in_quotes(osloDatatypeComplex.deprecated_version)}'),
        datablock.append(f'    waardeObject = {osloDatatypeComplex.name}{WaardenString}'),
        datablock.append(f''),
        datablock.append(f'    def __str__(self):'),
        datablock.append(f'        return {ComplexOrUnionTypeField}.__str__(self)')
        datablock.append('')

        return datablock

    def addAttributenToDataBlock(self, attributen, datablock, class_uri='', forClassUse=False, forUnionTypeUse=False):
        prop_datablock = []
        for attribuut in sorted(attributen, key=lambda a: a.name):
            if attribuut.overerving == 1:
                raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.objectUri}")

            whitepace = self.getWhiteSpaceEquivalent(f'        self._{attribuut.name} = OTLAttribuut(')
            fieldName = self.getSingleFieldFromTypeUri(attribuut.type)

            datablock.append(f'        self._{attribuut.name} = OTLAttribuut(field={fieldName},')
            datablock.append(f'{whitepace}naam={wrap_in_quotes(attribuut.name)},')
            datablock.append(f'{whitepace}label={wrap_in_quotes(attribuut.label_nl)},')
            datablock.append(f'{whitepace}objectUri={wrap_in_quotes(attribuut.objectUri)},')
            if attribuut.usagenote_nl != '':
                datablock.append(f'{whitepace}usagenote_nl={wrap_in_quotes(attribuut.usagenote_nl)},')
            if attribuut.deprecated_version != '':
                datablock.append(f'{whitepace}deprecated_version={wrap_in_quotes(attribuut.deprecated_version)},')
            if attribuut.constraints != '':
                datablock.append(f'{whitepace}constraints={wrap_in_quotes(attribuut.constraints)},')
            if attribuut.kardinaliteit_min != '1':
                datablock.append(f'{whitepace}kardinaliteit_min={wrap_in_quotes(attribuut.kardinaliteit_min)},')
            if attribuut.kardinaliteit_max != '1':
                datablock.append(f'{whitepace}kardinaliteit_max={wrap_in_quotes(attribuut.kardinaliteit_max)},')
            datablock.append(f'{whitepace}definition={wrap_in_quotes(attribuut.definition_nl)})')
            datablock.append('')

            prop_datablock.append(f'    @property'),
            prop_datablock.append(f'    def {attribuut.name}(self):'),
            prop_datablock.append(f'        """{attribuut.definition_nl}"""'),
            prop_datablock.append(f'        return self._{attribuut.name}.waarde'),
            prop_datablock.append(f''),
            if not forUnionTypeUse:
                prop_datablock.append(f'    @{attribuut.name}.setter'),
                prop_datablock.append(f'    def {attribuut.name}(self, value):'),
                prop_datablock.append(f'        self._{attribuut.name}.set_waarde(value)'),
                prop_datablock.append(f'')

        for propline in prop_datablock:
            datablock.append(propline)

        return datablock
