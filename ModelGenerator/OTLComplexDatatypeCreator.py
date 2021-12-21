from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLComplexDatatypeCreator(AbstractDatatypeCreator):
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

        if osloDatatypeComplex.uri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in osloDatatypeComplex.uri:
            return self.CreateBlockToWriteFromComplexTypesDtc(osloDatatypeComplex)
        else:
            raise NotImplementedError

    def CreateBlockToWriteFromComplexTypesDtc(self, osloDatatypeComplex: OSLODatatypeComplex):
        attributen = self.osloCollector.FindComplexDatatypeAttributenByClassUri(osloDatatypeComplex.uri)

        if len(attributen) == 1:
            raise NotImplementedError("Assumed more than 1 ComplexDatatypeAttribuut in Dtc attributen")

        datablock = ['from OTLModel.Datatypes.ComplexField import ComplexField']

        if any(atr.kardinaliteit_max != "1" for atr in attributen):
            datablock.append('from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField')

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getFieldsToImportFromListOfAttributes(attributen)
        for typeField in listOfFields:
            if typeField != 'ComplexField':
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
        datablock.append('')

        for attribuut in attributen:
            if attribuut.kardinaliteit_max == '1':

                if self.getFieldNameFromTypeUri(attribuut.type) != "ComplexField":
                    whitespace = self.getWhiteSpaceEquivalent(
                        f'        self.waarde.{attribuut.name} = {self.getFieldNameFromTypeUri(attribuut.type)}(')
                    datablock.append(
                        f'        self.waarde.{attribuut.name} = {self.getFieldNameFromTypeUri(attribuut.type)}(naam="{attribuut.name}",')
                    if self.getFieldNameFromTypeUri(attribuut.type) == "KeuzelijstField":
                        typeName = attribuut.type[attribuut.type.find("#") + 1::]
                        datablock.append(f'{whitespace}lijst={typeName}(),')
                        datablock.append(f'{whitespace}overerving={attribuut.overerving},')
                    datablock.append(f'{whitespace}label="{attribuut.label_nl}",')
                    datablock.append(f'{whitespace}uri="{attribuut.uri}",')
                    datablock.append(f'{whitespace}definition="{attribuut.definition_nl}",')
                    datablock.append(f'{whitespace}constraints="{attribuut.constraints}",')
                    datablock.append(f'{whitespace}usagenote="{attribuut.usagenote_nl}",')
                    datablock.append(f'{whitespace}deprecated_version="{attribuut.deprecated_version}")')
                    datablock.append(f'        self.{attribuut.name} = self.waarde.{attribuut.name}')
                    datablock.append(f'        """{attribuut.definition_nl}"""')
                else:
                    typeName = attribuut.type[attribuut.type.find("#") + 1::]
                    datablock.append(f'        self.waarde.adres = {typeName}()')
                    datablock.append(f'        self.waarde.adres.naam = "{attribuut.name}"')
                    datablock.append(f'        self.waarde.adres.label = "{attribuut.label_nl}"')
                    datablock.append(f'        self.waarde.adres.definition = "{attribuut.definition_nl}"')
                    datablock.append(f'        self.waarde.adres.uri = "{attribuut.uri}"')
                    datablock.append(f'        self.waarde.adres.overerving = {attribuut.overerving}')
                    datablock.append(f'        self.waarde.adres.constraints = "{attribuut.constraints}"')
                    datablock.append(f'        self.waarde.adres.readonly = {attribuut.readonly}')
                    datablock.append(f'        self.waarde.adres.usagenote = "{attribuut.usagenote_nl}"')
                    datablock.append(f'        self.waarde.adres.deprecated_version = "{attribuut.deprecated_version}"')
                    datablock.append(f'        """{attribuut.definition_nl}"""')

                datablock.append('')

            else:
                whitespace = self.getWhiteSpaceEquivalent(
                    f'        {attribuut.name}Field = {self.getFieldNameFromTypeUri(attribuut.type)}(')
                datablock.append(
                    f'        {attribuut.name}Field = {self.getFieldNameFromTypeUri(attribuut.type)}(naam="{attribuut.name}",')
                if self.getFieldNameFromTypeUri(attribuut.type) == "KeuzelijstField":
                    typeName = attribuut.type[attribuut.type.find("#") + 1::]
                    datablock.append(f'{whitespace}lijst={typeName}(),')
                    datablock.append(f'{whitespace}overerving={attribuut.overerving},')
                datablock.append(f'{whitespace}label="{attribuut.label_nl}",')
                datablock.append(f'{whitespace}uri="{attribuut.uri}",')
                datablock.append(f'{whitespace}definition="{attribuut.definition_nl}",')
                datablock.append(f'{whitespace}constraints="{attribuut.constraints}",')
                datablock.append(f'{whitespace}usagenote="{attribuut.usagenote_nl}",')
                datablock.append(f'{whitespace}deprecated_version="{attribuut.deprecated_version}")')
                datablock.append(f'        self.{attribuut.name} = KardinaliteitField(minKardinaliteit="{attribuut.kardinaliteit_min}", maxKardinaliteit="{attribuut.kardinaliteit_max}", fieldToMultiply={attribuut.name}Field)')
                datablock.append(f'        """{attribuut.definition_nl}"""')
                datablock.append('')

        if datablock[-1] == '':
            datablock.pop()

        return datablock

    @staticmethod
    def getEenheidFromConstraints(constraints: str):
        if constraints == '':
            raise ValueError
        split_text = constraints.split('"')
        return split_text[1]

    @staticmethod
    def getWhiteSpaceEquivalent(string):
        return ''.join(' ' * len(string))

    def getFieldNameFromTypeUri(self, attribuutType):
        if attribuutType.startswith('http://www.w3.org/2001/XMLSchema#'):
            return self.getSingleFieldFromTypeUri(attribuutType)
        return self.getNonSingleFieldFromTypeUri(attribuutType)[0]
