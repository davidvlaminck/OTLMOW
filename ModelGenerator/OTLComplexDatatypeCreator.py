from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut


class OTLComplexDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        self.logger.log("Created an instance of OTLComplexDatatypeCreator", LogType.INFO)

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
        elif osloDatatypeComplex.uri.startswith('https://schema.org/'):
            return self.CreateBlockToWriteFromComplexTypesDtc(osloDatatypeComplex)
        else:
            raise NotImplementedError

    def CreateBlockToWriteFromComplexTypesDtc(self, osloDatatypeComplex: OSLODatatypeComplex):
        attributen = self.osloCollector.FindComplexDatatypeAttributenByClassUri(osloDatatypeComplex.uri)

        datablock = ['from OTLModel.Datatypes.ComplexField import ComplexField']

        if any(atr.kardinaliteit_max != "1" for atr in attributen):
            datablock.append('from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField')

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getFieldsToImportFromListOfAttributes(attributen, ['ComplexField'])
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
        datablock.append('')

        self.addAttributenToDataBlock(attributen, datablock)

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