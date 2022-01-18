from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.StringHelper import wrap_in_quotes


class OTLPrimitiveDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        self.logger.log("Created an instance of OTLPrimitiveDatatypeCreator", LogType.INFO)

    def CreateBlockToWriteFromPrimitiveTypes(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        if not isinstance(osloDatatypePrimitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")
        if osloDatatypePrimitive.objectUri == '' or not (osloDatatypePrimitive.objectUri.startswith('http://www.w3.org/200') or
                                                         osloDatatypePrimitive.objectUri.startswith(
                                                             'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte')
                                                         or osloDatatypePrimitive.objectUri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')):
            raise ValueError(f"OSLODatatypePrimitive.objectUri is invalid. Value = '{osloDatatypePrimitive.objectUri}'")
        if osloDatatypePrimitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{osloDatatypePrimitive.name}'")

        if osloDatatypePrimitive.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd'):
            return self.CreateBlockToWriteFromPrimitiveTypesKwantWrd(osloDatatypePrimitive)
        if osloDatatypePrimitive.objectUri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte'):
            return self.CreateBlockToWriteFromPrimitiveTypesDte(osloDatatypePrimitive)

    def CreateBlockToWriteFromPrimitiveTypesDte(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        attributen = self.osloCollector.FindPrimitiveDatatypeAttributenByClassUri(osloDatatypePrimitive.objectUri)

        if len(attributen) != 1:
            raise NotImplementedError("Assumed exactly 1 PrimitiveDatatypeAttribuut in Dte attributen")

        if int(attributen[0].kardinaliteit_max) > 1:
            raise NotImplementedError("Found PrimitiveDatatypeAttribuut with kardinaliteit_max > 1")

        datablock = ['# coding=utf-8', 'from OTLModel.Datatypes.KwantWrd import KwantWrd']

        if attributen[0].readonly == 1:
            raise NotImplementedError("readonly property is assumed to be 0 on value fields")

        raise NotImplementedError('refactor Dte moet nog gebeuren')

        typeField = self.getSingleFieldFromTypeUri(attributen[0].type)
        datablock.append(f'from OTLModel.Datatypes.{typeField} import {typeField}')
        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(f'class {osloDatatypePrimitive.name}(KwantWrd):')
        datablock.append(f'    """{osloDatatypePrimitive.definition}"""')
        datablock.append('')
        datablock.append('    def __init__(self, waarde=None):')
        datablock.append(f'        self.waardeVeld = {typeField}(naam="{attributen[0].name}",')
        datablock.append(f'                                      label="{attributen[0].label}",')
        datablock.append(f'                                      objectUri="{attributen[0].objectUri}",')
        datablock.append(f'                                      definition="{attributen[0].definition}",')
        datablock.append(f'                                      constraints="{attributen[0].constraints}",')
        datablock.append(f'                                      usagenote="{attributen[0].usagenote}",')
        datablock.append(f'                                      deprecated_version="{attributen[0].deprecated_version}")')
        datablock.append(f'        """{attributen[0].definition}"""')
        datablock.append('')
        datablock.append(f'        super().__init__(naam="{osloDatatypePrimitive.name}",')
        datablock.append(f'                         label="{osloDatatypePrimitive.label}",')
        datablock.append(f'                         objectUri="{osloDatatypePrimitive.objectUri}",')
        datablock.append(f'                         definition="{osloDatatypePrimitive.definition}",')
        datablock.append(f'                         usagenote="{osloDatatypePrimitive.usagenote}",')
        datablock.append(f'                         deprecated_version="{osloDatatypePrimitive.deprecated_version}",')
        datablock.append(f'                         waardeVeld=self.waardeVeld,')
        datablock.append(f'                         eenheidVeld=None,')
        datablock.append(f'                         waarde=waarde)')

        return datablock

    def CreateBlockToWriteFromPrimitiveTypesKwantWrd(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        attributen = self.osloCollector.FindPrimitiveDatatypeAttributenByClassUri(osloDatatypePrimitive.objectUri)

        if int(attributen[0].kardinaliteit_max) > 1 or int(attributen[0].kardinaliteit_max) > 1:
            raise NotImplementedError("Found PrimitiveDatatypeAttribuut with kardinaliteit_max > 1")

        if len(attributen) != 2:
            raise NotImplementedError('it is assumed PrimitiveDatatype of type KwantWrd to have exactly 2 attributes')

        datablock = ['# coding=utf-8']
        if 'Literal' not in attributen[0].type:
            raise NotImplementedError(
                f'{osloDatatypePrimitive.objectUri}: the first attribute is not the Literal for this DatatypePrimitive')
        if attributen[0].readonly == 0 or attributen[1].readonly == 1:
            raise NotImplementedError("readonly property is assumed to be 1 on Literal and 0 on value fields")

        eenheidType = attributen[0]
        waardeType = attributen[1]

        waardeTypeField = self.getSingleFieldFromTypeUri(waardeType.type)
        datablock.append(f'from OTLModel.Datatypes.{waardeTypeField} import {waardeTypeField}')

        datablock.append('from OTLModel.Datatypes.LiteralField import LiteralField')
        datablock.append('from OTLModel.BaseClasses.KwantWrd import KwantWrd')
        datablock.append('from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid')
        datablock.append('from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')

        datablock.append(f'class {osloDatatypePrimitive.name}Eenheid(KwantWrdEenheid):')

        datablock.append(f'    def __init__(self):')
        datablock.append(f'        super().__init__()')
        datablock.append(f'        self._standaardEenheid = OTLAttribuut(field=LiteralField,')
        datablock.append(f'                                              naam={wrap_in_quotes(eenheidType.name)},')
        datablock.append(f'                                              label={wrap_in_quotes(eenheidType.label)},')
        datablock.append(f'                                              objectUri={wrap_in_quotes(eenheidType.objectUri)},')
        datablock.append(f'                                              definition={wrap_in_quotes(eenheidType.definition)},')
        datablock.append(f'                                              constraints={wrap_in_quotes(eenheidType.constraints)},')
        if eenheidType.deprecated_version != '':
            datablock.append(f'                                              constraints={wrap_in_quotes(eenheidType.deprecated_version)},')
        datablock.append(f'                                              usagenote={wrap_in_quotes(eenheidType.usagenote)})')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')

        datablock.append(f'class {osloDatatypePrimitive.name}({waardeTypeField}, KwantWrd):')
        datablock.append(f'    naam = {wrap_in_quotes(osloDatatypePrimitive.name)}')
        datablock.append(f'    label = {wrap_in_quotes(osloDatatypePrimitive.label)}')
        datablock.append(f'    objectUri = {wrap_in_quotes(osloDatatypePrimitive.objectUri)}')
        datablock.append(f'    definition = {wrap_in_quotes(osloDatatypePrimitive.definition)}')
        if waardeType.deprecated_version != '':
            datablock.append(f'    constraints={wrap_in_quotes(osloDatatypePrimitive.deprecated_version)}')
        datablock.append(f'    eenheid = {osloDatatypePrimitive.name}Eenheid()')

        datablock.append('')

        return datablock

    @staticmethod
    def getEenheidFromConstraints(constraints: str):
        if constraints == '':
            raise ValueError
        split_text = constraints.split('"')
        return split_text[1]
