from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLComplexDatatypeCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        logger.log("Created an instance of OTLComplexDatatypeCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromComplexTypes(self, osloDatatypeComplex: OSLODatatypeComplex):
        if not isinstance(osloDatatypeComplex, OSLODatatypeComplex):
            raise ValueError(f"Input is not a OSLODatatypeComplex")

        if osloDatatypeComplex.uri == '' or not (osloDatatypeComplex.uri == 'https://schema.org/ContactPoint' or
                                                 osloDatatypeComplex.uri == 'https://schema.org/OpeningHoursSpecification' or
                                                 (osloDatatypeComplex.uri.startswith(
                                                     'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in osloDatatypeComplex.uri)):
            raise ValueError(f"OSLODatatypeComplex.uri is invalid. Value = '{osloDatatypeComplex.uri}'")

        if osloDatatypeComplex.name == '':
            raise ValueError(f"OSLODatatypeComplex.name is invalid. Value = '{osloDatatypeComplex.name}'")

        if osloDatatypeComplex.uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in osloDatatypeComplex.uri:
            return self.CreateBlockToWriteFromComplexTypesDtc(osloDatatypeComplex)
        else:
            raise NotImplementedError

    def CreateBlockToWriteFromComplexTypesDtc(self, osloDatatypeComplex: OSLODatatypeComplex):
        attributen = self.osloCollector.FindComplexDatatypeAttributenByClassUri(osloDatatypeComplex.uri)

        if len(attributen) == 1:
            raise NotImplementedError("Assumed more than 1 ComplexDatatypeAttribuut in Dtc attributen")

        if any(atr.kardinaliteit_max != "1" for atr in attributen):
            raise NotImplementedError("Found ComplexDatatypeAttribuut with kardinaliteit_max != 1")

        datablock = ['from OTLModel.Datatypes.ComplexField import ComplexField, ComplexAttributen']

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getTypeFieldsFromListOfAttributes(attributen)
        for typeField in listOfFields:
            datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}')
        datablock.append(f'class {osloDatatypeComplex.name}(ComplexField):')
        datablock.append(f'    """{osloDatatypeComplex.definition_nl}"""')
        datablock.append('')
        datablock.append('    def __init__(self):')
        datablock.append(f'        super().__init__(naam="{osloDatatypeComplex.name}",')
        datablock.append(f'                         label="{osloDatatypeComplex.label_nl}",')
        datablock.append(f'                         uri="{osloDatatypeComplex.uri}",')
        datablock.append(f'                         definition="{osloDatatypeComplex.definition_nl}",')
        datablock.append(f'                         usagenote="{osloDatatypeComplex.usagenote_nl}",')
        datablock.append(f'                         deprecated_version="{osloDatatypeComplex.deprecated_version}")')
        datablock.append('        self.waarde = ComplexAttributen()')
        datablock.append('')

        # TODO for each attribute...

        datablock.append(f'        waardeVeld = {typeField}(naam="{attributen[0].name}",')
        datablock.append(f'                                 label="{attributen[0].label_nl}",')
        datablock.append(f'                                 uri="{attributen[0].uri}",')
        datablock.append(f'                                 definition="{attributen[0].definition_nl}",')
        datablock.append(f'                                 constraints=\'{attributen[0].constraints}\',')
        datablock.append(f'                                 usagenote=\'{attributen[0].usagenote_nl}\',')
        datablock.append(f'                                 deprecated_version="{attributen[0].deprecated_version}")')
        datablock.append(f'        """{attributen[0].definition_nl}"""')
        datablock.append('')

        return datablock

    @staticmethod
    def getEenheidFromConstraints(constraints: str):
        if constraints == '':
            raise ValueError
        split_text = constraints.split('"')
        return split_text[1]

    @staticmethod
    def getFieldFromTypeUri(type: str):
        match type:
            case 'http://www.w3.org/2001/XMLSchema#decimal':
                return 'DecimalFloatField'
            case 'http://www.w3.org/2001/XMLSchema#string':
                return 'StringField'
            case 'http://www.w3.org/2001/XMLSchema#boolean':
                return 'BooleanField'
            case 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger':
                return 'NonNegIntField'
        raise NotImplemented('not supported type in OTLPrimitiveDatatypeCreator.getFieldFromTypeUri()')

    def writeToFile(self, KwantWrd: OSLODatatypePrimitive, dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/Datatypes/{KwantWrd.name}.py"

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
