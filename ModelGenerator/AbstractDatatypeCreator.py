from abc import ABC


class AbstractDatatypeCreator(ABC):
    @staticmethod
    def getSingleFieldFromTypeUri(fieldType: str):
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
            case 'http://www.w3.org/2001/XMLSchema#time':
                return 'TimeField'
            case 'http://www.w3.org/2001/XMLSchema#anyURI':
                return 'URIField'

        raise NotImplemented('not supported fieldType in getSingleFieldFromTypeUri()')

    @staticmethod
    def getNonSingleFieldFromTypeUri(fieldType: str):
        if '#Dtc' in fieldType:
            typeName = fieldType[fieldType.find("#")+1::]
            return ['ComplexField', typeName]
        if '#Dte' in fieldType or '#KwantWrd' in fieldType:
            typeName = fieldType[fieldType.find("#")+1::]
            return [typeName]
        if '#Kl' in fieldType:
            typeName = fieldType[fieldType.find("#")+1::]
            return ['KeuzelijstField', typeName]

        raise NotImplemented('not supported fieldType in getNonSingleFieldFromTypeUri()')

    @staticmethod
    def writeToFile(datatype, dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/Datatypes/{datatype.name}.py"

        file = open(path, "w")
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()

    def getFieldsToImportFromListOfAttributes(self, attributen):
        if len(attributen) == 0:
            return []

        primitiveTypesList = list(filter(lambda t: t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))
        otherTypesList = list(filter(lambda t: not t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))

        select_types_list = list(map(lambda a: self.getSingleFieldFromTypeUri(a.type), primitiveTypesList))

        for nonPrimitiveType in otherTypesList:
            select_types_list.extend(self.getNonSingleFieldFromTypeUri(nonPrimitiveType.type))

        distinct_types_list = list(set(select_types_list))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list