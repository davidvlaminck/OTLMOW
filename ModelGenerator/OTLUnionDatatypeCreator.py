from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut


class OTLUnionDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        self.logger.log("Created an instance of OTLUnionDatatypeCreator", LogType.INFO)

    def CreateBlockToWriteFromUnionTypes(self, oSLODatatypeUnion: OSLODatatypeUnion):
        if not isinstance(oSLODatatypeUnion, OSLODatatypeUnion):
            raise ValueError(f"Input is not a OSLODatatypeUnion")

        if oSLODatatypeUnion.objectUri == '' or not (oSLODatatypeUnion.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtu' in oSLODatatypeUnion.objectUri):
            raise ValueError(f"OSLODatatypeUnion.objectUri is invalid. Value = '{oSLODatatypeUnion.objectUri}'")

        if oSLODatatypeUnion.name == '':
            raise ValueError(f"OSLODatatypeUnion.name is invalid. Value = '{oSLODatatypeUnion.name}'")

        return self.CreateBlockToWriteFromUnionTypesDtu(oSLODatatypeUnion)

    def CreateBlockToWriteFromUnionTypesDtu(self, oSLODatatypeUnion: OSLODatatypeUnion):
        attributen = self.osloCollector.FindUnionDatatypeAttributenByClassUri(oSLODatatypeUnion.objectUri)

        datablock = ['# coding=utf-8', 'from OTLModel.Datatypes.UnionTypeField import UnionTypeField']

        if any(atr.kardinaliteit_max != "1" for atr in attributen):
            raise NotImplementedError(" no support for UnionTypes with > 1 kardinaliteit")

        if any(atr.readonly == 1 for atr in attributen):
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        listOfFields = self.getFieldsToImportFromListOfAttributes(attributen)
        for typeField in listOfFields:
            datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(f'class {oSLODatatypeUnion.name}(UnionTypeField):')
        datablock.append(f'    """{oSLODatatypeUnion.definition_nl}"""')
        datablock.append('')
        datablock.append('    def __init__(self):')
        datablock.append(f'        super().__init__(naam="{oSLODatatypeUnion.name}",')
        datablock.append(f'                         label="{oSLODatatypeUnion.label_nl}",')
        datablock.append(f'                         objectUri="{oSLODatatypeUnion.objectUri}",')
        datablock.append(f'                         definition="{oSLODatatypeUnion.definition_nl}",')
        datablock.append(f'                         usagenote="{oSLODatatypeUnion.usagenote_nl}",')
        datablock.append(f'                         deprecated_version="{oSLODatatypeUnion.deprecated_version}")')
        datablock.append('')

        self.addAttributenToDataBlock(attributen, datablock, forUnionTypeUse=True)

        fieldsTupleLine = '        self.fieldsTuple = ('
        for attribuut in attributen:
            fieldsTupleLine += 'field_' + attribuut.name + ', '
        fieldsTupleLine = fieldsTupleLine[:-2] + ')'
        datablock.append(fieldsTupleLine)

        return datablock
