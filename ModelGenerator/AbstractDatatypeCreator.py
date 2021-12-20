from abc import ABC


class AbstractDatatypeCreator(ABC):
    @staticmethod
    def getFieldFromTypeUri(fieldType: str):
        match fieldType:
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
        raise NotImplemented('not supported fieldType in OTLPrimitiveDatatypeCreator.getFieldFromTypeUri()')

    @staticmethod
    def writeToFile(datatype, dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/Datatypes/{datatype.name}.py"

        file = open(path, "w")
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()

    def getTypeFieldsFromListOfAttributes(self, attributen):
        if len(attributen) == 0:
            return []
        select_types_list = list(map(lambda a: self.getFieldFromTypeUri(a.type), attributen))
        distinct_types_list = list(set(select_types_list))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list