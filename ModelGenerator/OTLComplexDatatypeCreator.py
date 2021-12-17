from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLComplexDatatypeCreator:
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        logger.log("Created an instance of OTLComplexDatatypeCreator", LogType.INFO)
        self.osloCollector = osloCollector

    def CreateBlockToWriteFromPrimitiveTypes(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        if not isinstance(osloDatatypePrimitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")
        if osloDatatypePrimitive.uri == '' or not (osloDatatypePrimitive.uri.startswith('http://www.w3.org/200') or
                                                   osloDatatypePrimitive.uri.startswith(
                                                       'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte')
                                                   or osloDatatypePrimitive.uri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')):
            raise ValueError(f"OSLODatatypePrimitive.uri is invalid. Value = '{osloDatatypePrimitive.uri}'")
        if osloDatatypePrimitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{osloDatatypePrimitive.name}'")

        if osloDatatypePrimitive.uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd'):
            return self.CreateBlockToWriteFromPrimitiveTypesKwantWrd(osloDatatypePrimitive)
        if osloDatatypePrimitive.uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte'):
            return self.CreateBlockToWriteFromPrimitiveTypesDte(osloDatatypePrimitive)

    def CreateBlockToWriteFromPrimitiveTypesDte(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        attributen = self.osloCollector.FindPrimitiveDatatypeAttributenByClassUri(osloDatatypePrimitive.uri)

        if len(attributen) != 1:
            raise NotImplementedError("Assumed exactly 1 PrimitiveDatatypeAttribuut in Dte attributen")

        if int(attributen[0].kardinaliteit_max) > 1:
            raise NotImplementedError("Found PrimitiveDatatypeAttribuut with kardinaliteit_max > 1")

        datablock = ['from OTLModel.Datatypes.KwantWrd import KwantWrd']

        if attributen[0].readonly == 1:
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        typeField = self.getFieldFromTypeUri(attributen[0].type)
        datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')
        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}')
        datablock.append(f'class {osloDatatypePrimitive.name}(KwantWrd):')
        datablock.append(f'    """{osloDatatypePrimitive.definition_nl}"""')
        datablock.append('')
        datablock.append('    def __init__(self, waarde=None):')
        datablock.append(f'        waardeVeld = {typeField}(naam="{attributen[0].name}",')
        datablock.append(f'                                 label="{attributen[0].label_nl}",')
        datablock.append(f'                                 uri="{attributen[0].uri}",')
        datablock.append(f'                                 definition="{attributen[0].definition_nl}",')
        datablock.append(f'                                 constraints=\'{attributen[0].constraints}\',')
        datablock.append(f'                                 usagenote=\'{attributen[0].usagenote_nl}\',')
        datablock.append(f'                                 deprecated_version="{attributen[0].deprecated_version}")')
        datablock.append(f'        """{attributen[0].definition_nl}"""')
        datablock.append('')
        datablock.append(f'        super().__init__(naam="{osloDatatypePrimitive.name}",')
        datablock.append(f'                         label="{osloDatatypePrimitive.label_nl}",')
        datablock.append(f'                         uri="{osloDatatypePrimitive.uri}",')
        datablock.append(f'                         definition="{osloDatatypePrimitive.definition_nl}",')
        datablock.append(f'                         usagenote="{osloDatatypePrimitive.usagenote_nl}",')
        datablock.append(f'                         deprecated_version="{osloDatatypePrimitive.deprecated_version}",')
        datablock.append(f'                         waardeVeld=waardeVeld,')
        datablock.append(f'                         eenheidVeld=None,')
        datablock.append(f'                         waarde=waarde)')

        return datablock

    def CreateBlockToWriteFromPrimitiveTypesKwantWrd(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        attributen = self.osloCollector.FindPrimitiveDatatypeAttributenByClassUri(osloDatatypePrimitive.uri)

        if any(int(a.kardinaliteit_max) > 1 for a in attributen):
            raise NotImplementedError("Found PrimitiveDatatypeAttribuut with kardinaliteit_max > 1")

        datablock = ['from OTLModel.Datatypes.KwantWrd import KwantWrd']
        if 'Literal' not in attributen[0].type:
            raise NotImplementedError(
                f'{osloDatatypePrimitive.uri}: the first attribute is not the Literal for this DatatypePrimitive')
        if attributen[0].readonly == 0 or attributen[1].readonly == 1:
            raise NotImplementedError("readonly property is assumed to be 1 on Literal and 0 on value fields")

        datablock.append('from OTLModel.Datatypes.LiteralField import LiteralField')
        typeField = self.getFieldFromTypeUri(attributen[1].type)
        datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')
        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}')
        datablock.append(f'class {osloDatatypePrimitive.name}(KwantWrd):')
        datablock.append(f'    """{osloDatatypePrimitive.definition_nl}"""')
        datablock.append('')
        datablock.append('    def __init__(self, waarde=None):')
        datablock.append(f'        eenheid = LiteralField(naam="{attributen[0].name}",')
        datablock.append(f'                               label="{attributen[0].label_nl}",')
        datablock.append(f'                               uri="{attributen[0].uri}",')
        datablock.append(f'                               definition="{attributen[0].definition_nl}",')
        datablock.append(f'                               constraints=\'{attributen[0].constraints}\',')
        datablock.append(f'                               usagenote=\'{attributen[0].usagenote_nl}\',')
        datablock.append(f'                               deprecated_version="{attributen[0].deprecated_version}",')
        datablock.append(
            f'                               readonlyValue="{self.getEenheidFromConstraints(attributen[0].constraints)}")')
        datablock.append(f'        """{attributen[0].definition_nl}"""')
        datablock.append('')
        datablock.append(f'        waardeVeld = {typeField}(naam="{attributen[1].name}",')
        datablock.append(f'                                       label="{attributen[1].label_nl}",')
        datablock.append(f'                                       uri="{attributen[1].uri}",')
        datablock.append(f'                                       definition="{attributen[1].definition_nl}",')
        datablock.append(f'                                       constraints=\'{attributen[1].constraints}\',')
        datablock.append(f'                                       usagenote=\'{attributen[1].usagenote_nl}\',')
        datablock.append(f'                                       deprecated_version="{attributen[1].deprecated_version}")')
        datablock.append(f'        """{attributen[1].definition_nl}"""')
        datablock.append('')
        datablock.append(f'        super().__init__(naam="{osloDatatypePrimitive.name}",')
        datablock.append(f'                         label="{osloDatatypePrimitive.label_nl}",')
        datablock.append(f'                         uri="{osloDatatypePrimitive.uri}",')
        datablock.append(f'                         definition="{osloDatatypePrimitive.definition_nl}",')
        datablock.append(f'                         usagenote="{osloDatatypePrimitive.usagenote_nl}",')
        datablock.append(f'                         deprecated_version="{osloDatatypePrimitive.deprecated_version}",')
        datablock.append(f'                         waardeVeld=waardeVeld,')
        datablock.append(f'                         eenheidVeld=eenheid,')
        datablock.append(f'                         waarde=waarde)')

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
            case 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger':
                return 'NonNegIntField'
        raise NotImplemented('not supported type in OTLPrimitiveDatatypeCreator.getFieldFromTypeUri()')

    def writeToFile(self, KwantWrd: OSLODatatypePrimitive, dataToWrite: list[str], relativePath=''):
        path = f"{relativePath}OTLModel/Datatypes/{KwantWrd.name}.py"

        file = open(path, "w")
        for line in dataToWrite:
            file.write(line + "\n")
        file.close()
