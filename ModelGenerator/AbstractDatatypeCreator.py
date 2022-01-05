from abc import ABC

from Loggers.AbstractLogger import AbstractLogger
from ModelGenerator.OSLOCollector import OSLOCollector


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
        if fieldType.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#'):
            return fieldType.split('#')[1]
        match fieldType:
            case None:
                return ''
            case 'http://www.w3.org/2001/XMLSchema#decimal':
                return 'DecimalFloatField'
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

        raise NotImplemented(f'not supported fieldType {fieldType} in getNonSingleFieldFromTypeUri()')

    @staticmethod
    def writeToFile(datatype, directory: str, dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/{directory}/{datatype.name}.py"

        file = open(path, "w")
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()

    def getFieldsToImportFromListOfAttributes(self, attributen, listToStartFrom=[]):
        if len(attributen) == 0:
            return listToStartFrom

        collectedList = []
        collectedList.extend(listToStartFrom)

        for attribuut in attributen:
            typeLink = self.getTypeLinkFromAttribuut(attribuut)
            if typeLink == "OSLOEnumeration":
                collectedList.append('KeuzelijstField')
                collectedList.append(self.getTypeNameOfEnumUri(attribuut.type))
            elif typeLink == "OSLODatatypePrimitive":
                collectedList.append(self.getSingleFieldFromTypeUri(attribuut.type))
            elif typeLink == "OSLODatatypeComplex":
                collectedList.append(self.getTypeNameOfComplexAttribuut(attribuut.type))
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

    def addAttributenToDataBlock(self, attributen, datablock, class_uri='', forDatatypeUse=True):
        for attribuut in attributen:
            typeLink = self.getTypeLinkFromAttribuut(attribuut)

            if attribuut.overerving == 1:
                raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.uri}")

            if attribuut.deprecated_version != '':
                continue
                # raise NotImplementedError(f"deprecated attributes is not implemented, found in {attributen.uri}")

            # depending on the use for datatype creation or class creation use 'self.' or 'self.waarde.'
            selfWaarde = 'self.waarde'
            if not forDatatypeUse:
                selfWaarde = 'self'

            if (attribuut.uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI' and class_uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject') or (
                    attribuut.uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.typeURI' and class_uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'):
                datablock.append('        uri = self.typeURI')

            definitie = attribuut.definition_nl.replace('"', r'\"').replace('\n', '')

            if attribuut.kardinaliteit_max == '1':
                if typeLink == "OSLODatatypePrimitive":
                    fieldName = self.getSingleFieldFromTypeUri(attribuut.type)
                    if fieldName.startswith("Dte") or fieldName.startswith('KwantWrd'):
                        datablock.append(f'        {selfWaarde}.{attribuut.name} = {fieldName}()')
                        datablock.append(f'        """{definitie}"""')
                        datablock.append(f'        {selfWaarde}.{attribuut.name}.naam = "{attribuut.name}"')
                        datablock.append(f'        {selfWaarde}.{attribuut.name}.label = "{attribuut.label_nl}"')
                        datablock.append(f'        {selfWaarde}.{attribuut.name}.uri = "{attribuut.uri}"')

                        datablock.append(f'        {selfWaarde}.{attribuut.name}.definition = "{definitie}"')
                        datablock.append(f'        {selfWaarde}.{attribuut.name}.constraints = "{attribuut.constraints}"')
                        datablock.append(f'        {selfWaarde}.{attribuut.name}.usagenote = "{attribuut.usagenote_nl}"')
                        if attribuut.readonly:
                            datablock.append(f'        {selfWaarde}.{attribuut.name}.readonly = {attribuut.readonly}')
                        datablock.append(
                            f'        {selfWaarde}.{attribuut.name}.deprecated_version = "{attribuut.deprecated_version}"')
                        if forDatatypeUse:
                            datablock.append(f'        self.{attribuut.name} = {selfWaarde}.{attribuut.name}')
                        if (attribuut.uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI' and class_uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject') or (
                                attribuut.uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.typeURI' and class_uri == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'):
                            datablock.append('        self.typeURI.waarde = uri')
                    else:
                        whitespace = self.getWhiteSpaceEquivalent(
                            f'        {selfWaarde}.{attribuut.name} = {self.getFieldNameFromTypeUri(attribuut.type)}(')
                        datablock.append(
                            f'        {selfWaarde}.{attribuut.name} = {self.getFieldNameFromTypeUri(attribuut.type)}(naam="{attribuut.name}",')
                        datablock.append(f'{whitespace}label="{attribuut.label_nl}",')
                        datablock.append(f'{whitespace}uri="{attribuut.uri}",')
                        datablock.append(f'{whitespace}definition="{definitie}",')
                        datablock.append(f'{whitespace}constraints="{attribuut.constraints}",')
                        datablock.append(f'{whitespace}usagenote="{attribuut.usagenote_nl}",')
                        if attribuut.readonly:
                            datablock.append(f'{whitespace}readonly="{attribuut.readonly}",')
                        datablock.append(f'{whitespace}deprecated_version="{attribuut.deprecated_version}")')
                        if forDatatypeUse:
                            datablock.append(f'        self.{attribuut.name} = {selfWaarde}.{attribuut.name}')
                        datablock.append(f'        """{definitie}"""')

                    datablock.append('')
                    continue

                if typeLink == "OSLOEnumeration":
                    typeName = self.getTypeNameOfEnumUri(attribuut.type)
                    whitespace = self.getWhiteSpaceEquivalent(
                        f'        {selfWaarde}.{attribuut.name} = KeuzelijstField(')
                    datablock.append(
                        f'        {selfWaarde}.{attribuut.name} = KeuzelijstField(naam="{attribuut.name}",')
                    datablock.append(f'{whitespace}label="{attribuut.label_nl}",')
                    datablock.append(f'{whitespace}lijst={typeName}(),')
                    datablock.append(f'{whitespace}uri="{attribuut.uri}",')
                    datablock.append(f'{whitespace}definition="{definitie}",')
                    datablock.append(f'{whitespace}constraints="{attribuut.constraints}",')
                    datablock.append(f'{whitespace}usagenote="{attribuut.usagenote_nl}",')
                    if attribuut.readonly:
                        datablock.append(f'{whitespace}readonly="{attribuut.readonly}",')
                    datablock.append(f'{whitespace}deprecated_version="{attribuut.deprecated_version}")')
                    if forDatatypeUse:
                        datablock.append(f'        self.{attribuut.name} = {selfWaarde}.{attribuut.name}')
                    datablock.append(f'        """{definitie}"""')
                    datablock.append('')
                    continue

                if typeLink == "OSLODatatypeComplex":
                    fieldName = self.getTypeNameOfComplexAttribuut(attribuut.type)
                    datablock.append(f'        {selfWaarde}.{attribuut.name} = {fieldName}()')
                    datablock.append(f'        """{definitie}"""')
                    datablock.append(f'        {selfWaarde}.{attribuut.name}.naam = "{attribuut.name}"')
                    datablock.append(f'        {selfWaarde}.{attribuut.name}.label = "{attribuut.label_nl}"')
                    datablock.append(f'        {selfWaarde}.{attribuut.name}.uri = "{attribuut.uri}"')
                    datablock.append(f'        {selfWaarde}.{attribuut.name}.definition = "{definitie}"')
                    datablock.append(f'        {selfWaarde}.{attribuut.name}.constraints = "{attribuut.constraints}"')
                    datablock.append(f'        {selfWaarde}.{attribuut.name}.usagenote = "{attribuut.usagenote_nl}"')
                    if attribuut.readonly:
                        datablock.append(f'        {selfWaarde}.{attribuut.name}.readonly = {attribuut.readonly}')
                    datablock.append(
                        f'        {selfWaarde}.{attribuut.name}.deprecated_version = "{attribuut.deprecated_version}"')
                    if forDatatypeUse:
                        datablock.append(f'        self.{attribuut.name} = {selfWaarde}.{attribuut.name}')
                    datablock.append('')
                    continue

            else:  # kardinaliteit_max > 1
                if typeLink == "OSLODatatypeComplex":
                    fieldName = self.getTypeNameOfComplexAttribuut(attribuut.type)
                    datablock.append(f'        {attribuut.name}Field = {fieldName}()')
                    datablock.append(f'        {attribuut.name}Field.naam = "{attribuut.name}"')
                    datablock.append(f'        {attribuut.name}Field.label = "{attribuut.label_nl}"')
                    datablock.append(f'        {attribuut.name}Field.uri = "{attribuut.uri}"')
                    datablock.append(f'        {attribuut.name}Field.definition = "{definitie}"')
                    datablock.append(f'        {attribuut.name}Field.constraints = "{attribuut.constraints}"')
                    datablock.append(f'        {attribuut.name}Field.usagenote = "{attribuut.usagenote_nl}"')
                    if attribuut.readonly:
                        datablock.append(f'        {attribuut.name}Field.readonly = {attribuut.readonly}')
                    datablock.append(
                        f'        {attribuut.name}Field.deprecated_version = "{attribuut.deprecated_version}"')
                    if forDatatypeUse:
                        datablock.append(
                            f'        self.waarde.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                        datablock.append(f'        self.{attribuut.name} = self.waarde.{attribuut.name}')
                    else:
                        datablock.append(
                            f'        self.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                    datablock.append(f'        """{definitie}"""')
                    datablock.append('')
                    continue

                if typeLink == "OSLOEnumeration":
                    typeName = self.getTypeNameOfEnumUri(attribuut.type)
                    whitespace = self.getWhiteSpaceEquivalent(
                        f'        {attribuut.name}Field = KeuzelijstField(')
                    datablock.append(
                        f'        {attribuut.name}Field = KeuzelijstField(naam="{attribuut.name}",')
                    datablock.append(f'{whitespace}label="{attribuut.label_nl}",')
                    datablock.append(f'{whitespace}lijst={typeName}(),')
                    datablock.append(f'{whitespace}uri="{attribuut.uri}",')
                    datablock.append(f'{whitespace}definition="{definitie}",')
                    datablock.append(f'{whitespace}constraints="{attribuut.constraints}",')
                    datablock.append(f'{whitespace}usagenote="{attribuut.usagenote_nl}",')
                    if attribuut.readonly:
                        datablock.append(f'{whitespace}readonly="{attribuut.readonly}",')
                    datablock.append(f'{whitespace}deprecated_version="{attribuut.deprecated_version}")')
                    if forDatatypeUse:
                        datablock.append(
                            f'        self.waarde.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                        datablock.append(f'        self.{attribuut.name} = self.waarde.{attribuut.name}')
                    else:
                        datablock.append(
                            f'        self.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')

                    datablock.append(f'        """{definitie}"""')
                    datablock.append('')
                    continue

                if typeLink == "OSLODatatypePrimitive":
                    fieldName = self.getSingleFieldFromTypeUri(attribuut.type)
                    if fieldName.startswith("Dte") or fieldName.startswith('KwantWrd'):
                        datablock.append(f'        {attribuut.name}Field = {fieldName}()')

                        datablock.append(f'        {attribuut.name}Field.naam = "{attribuut.name}"')
                        datablock.append(f'        {attribuut.name}Field.label = "{attribuut.label_nl}"')
                        datablock.append(f'        {attribuut.name}Field.uri = "{attribuut.uri}"')
                        datablock.append(f'        {attribuut.name}Field.definition = "{definitie}"')
                        datablock.append(f'        {attribuut.name}Field.constraints = "{attribuut.constraints}"')
                        datablock.append(f'        {attribuut.name}Field.usagenote = "{attribuut.usagenote_nl}"')
                        if attribuut.readonly:
                            datablock.append(f'        {attribuut.name}Field.readonly = {attribuut.readonly}')
                        datablock.append(
                            f'        {attribuut.name}Field.deprecated_version = "{attribuut.deprecated_version}"')
                        if forDatatypeUse:
                            datablock.append(
                                f'        self.waarde.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                            datablock.append(f'        self.{attribuut.name} = self.waarde.{attribuut.name}')
                        else:
                            datablock.append(
                                f'        self.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                        datablock.append(f'        """{definitie}"""')
                    else:
                        whitespace = self.getWhiteSpaceEquivalent(
                            f'        {attribuut.name}Field = {self.getFieldNameFromTypeUri(attribuut.type)}(')
                        datablock.append(
                            f'        {attribuut.name}Field = {self.getFieldNameFromTypeUri(attribuut.type)}(naam="{attribuut.name}",')
                        datablock.append(f'{whitespace}label="{attribuut.label_nl}",')
                        datablock.append(f'{whitespace}uri="{attribuut.uri}",')
                        datablock.append(f'{whitespace}definition="{definitie}",')
                        datablock.append(f'{whitespace}constraints="{attribuut.constraints}",')
                        datablock.append(f'{whitespace}usagenote="{attribuut.usagenote_nl}",')
                        if attribuut.readonly:
                            datablock.append(f'{whitespace}readonly="{attribuut.readonly}",')
                        datablock.append(f'{whitespace}deprecated_version="{attribuut.deprecated_version}")')
                        if forDatatypeUse:
                            datablock.append(
                                f'        self.waarde.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                            datablock.append(f'        self.{attribuut.name} = self.waarde.{attribuut.name}')
                        else:
                            datablock.append(
                                f'        self.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')

                        datablock.append(f'        """{definitie}"""')

                    datablock.append('')
                    continue

        return datablock
