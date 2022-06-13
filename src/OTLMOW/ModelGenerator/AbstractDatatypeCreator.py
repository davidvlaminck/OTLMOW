import os
from abc import ABC

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.StringHelper import wrap_in_quotes


class AbstractDatatypeCreator(ABC):
    def __init__(self, oslo_collector: OSLOCollector):
        self.oslo_collector = oslo_collector

    def get_type_link_from_attribuut(self, attribuut):
        typeLink = self.oslo_collector.find_type_link_by_uri(attribuut.type)
        if typeLink is not None:
            return typeLink.item_tabel

    @staticmethod
    def get_single_field_from_type_uri(fieldType: str):
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
            case 'https://schema.org/ContactPoint':
                return 'DtcContactinfo'
            case 'http://www.w3.org/2000/01/rdf-schema#Literal':
                return 'StringField'
            case _:
                raise NotImplemented('not supported fieldType in get_single_field_from_type_uri()')

    @staticmethod
    def get_non_single_field_from_type_uri(fieldType: str):
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

        raise NotImplemented(f'not supported fieldType {fieldType} in get_non_single_field_from_type_uri()')

    @staticmethod
    def write_to_file(datatype, directory: str, data_to_write: list[str], relative_path=''):
        if relative_path == '':
            base_dir = os.path.dirname(os.path.realpath(__file__))
            base_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
        else:
            base_dir = relative_path
        path = f"{base_dir}/OTLModel/{directory}/{datatype.name}.py"

        with open(path, "w", encoding='utf-8') as file:
            for line in data_to_write:
                file.write(line + "\n")

    def get_fields_to_import_from_list_of_attributes(self, attributen, listToStartFrom=None):
        if listToStartFrom is None:
            listToStartFrom = []
        if len(attributen) == 0:
            return listToStartFrom

        collectedList = []
        collectedList.extend(listToStartFrom)

        for attribuut in attributen:
            typeLink = self.get_type_link_from_attribuut(attribuut)
            if typeLink == "OSLOEnumeration":
                collectedList.append(self.get_type_name_of_enum_uri(attribuut.type))
            elif typeLink == "OSLODatatypePrimitive":
                collectedList.append(self.get_single_field_from_type_uri(attribuut.type))
            elif typeLink == "OSLODatatypeComplex":
                collectedList.append(self.get_type_name_of_complex_attribuut(attribuut.type))
            elif typeLink == "OSLODatatypeUnion":
                collectedList.append(self.get_type_name_of_union_attribuut(attribuut.type))
            else:
                raise not NotImplementedError(f"{typeLink.item_tabel} not implemented")

        distinct_types_list = list(set(collectedList))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list

    def get_fields_and_names_from_list_of_attributes(self, attributen):
        if len(attributen) == 0:
            return []

        primitiveTypesList = list(filter(lambda t: t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))
        otherTypesList = list(filter(lambda t: not t.type.startswith('http://www.w3.org/2001/XMLSchema#'), attributen))

        select_types_list = list(map(lambda a: (self.get_single_field_from_type_uri(a.type), a.name), primitiveTypesList))

        for nonPrimitiveType in otherTypesList:
            select_types_list.append((self.get_field_name_from_type_uri(nonPrimitiveType.type), nonPrimitiveType.name))

        distinct_types_list = list(set(select_types_list))
        sorted_list = sorted(distinct_types_list, key=lambda t: t)
        return sorted_list

    @staticmethod
    def get_white_space_equivalent(string):
        return ''.join(' ' * len(string))

    def get_field_name_from_type_uri(self, attribuutType):
        if attribuutType.startswith('http://www.w3.org/2001/XMLSchema#'):
            return self.get_single_field_from_type_uri(attribuutType)
        if attribuutType.startswith("https://schema.org/"):
            return self.get_non_single_field_from_type_uri(attribuutType)[1]
        return self.get_non_single_field_from_type_uri(attribuutType)[1]

    @staticmethod
    def get_type_name_of_enum_uri(type_uri: str):
        return type_uri.split('#')[1]

    def get_type_name_of_union_attribuut(self, type_uri: str):
        if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/"):
            return type_uri[type_uri.find("#") + 1::]

        raise NotImplementedError(f"get_type_name_of_complex_attribuut fails to get typename from {type_uri}")

    def get_type_name_of_complex_attribuut(self, type_uri: str):
        if type_uri.startswith("https://wegenenverkeer.data.vlaanderen.be/ns/") or type_uri.startswith(
                "http://www.w3.org/2001/XMLSchema#"):
            return type_uri[type_uri.find("#") + 1::]
        elif type_uri.startswith("https://schema.org/"):
            if type_uri == "https://schema.org/ContactPoint":
                return "DtcContactinfo"
            if type_uri == "https://schema.org/OpeningHoursSpecification":
                return "DtcOpeningsurenSpecificatie"
            raise NotImplementedError(
                f"Field of type {type_uri} is not implemented in DatatypeCreator.get_type_name_of_complex_attribuut")

        raise NotImplementedError(f"get_type_name_of_complex_attribuut fails to get typename from {type_uri}")

    def create_block_to_write_from_complex_primitive_or_union_types(self, osloDatatype, typeField='', model_location=''):
        attributen = self.get_attributen_by_typeField(typeField, osloDatatype)

        datablock = ['# coding=utf-8',
                     'from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo',
                     'from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut']

        list_fields_to_start_with = [f'{typeField}Field']
        if typeField == 'UnionType':
            list_fields_to_start_with.append('UnionWaarden')
        elif typeField == 'Primitive' or typeField == 'KwantWrd':
            datablock.append('from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField')
            list_fields_to_start_with = []
        listOfFields = self.get_fields_to_import_from_list_of_attributes(attributen, list_fields_to_start_with)
        base_fields = ['BooleanField', 'ComplexField', 'DateField', 'DateTimeField', 'FloatOrDecimalField', 'IntegerField',
                       'KeuzelijstField', 'UnionTypeField', 'URIField', 'LiteralField', 'NonNegIntegerField', 'TimeField',
                       'StringField', 'UnionWaarden']
        for module in listOfFields:
            model_module = 'OTLMOW'
            if model_location != '' and module not in base_fields:
                modules_index = model_location.rfind('\\OTLMOW')
                modules = model_location[modules_index+1:]
                model_module = modules.replace('\\', '.')
            datablock.append(f'from {model_module}.OTLModel.Datatypes.{module} import {module}')

        datablock.append('')
        datablock.append('')
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        if typeField == 'UnionType':
            datablock.append(f'class {osloDatatype.name}Waarden(AttributeInfo, UnionWaarden):')
            datablock.append('    def __init__(self, parent=None):')
            datablock.append('        AttributeInfo.__init__(self, parent)')
            datablock.append('        UnionWaarden.__init__(self)')
        else:
            datablock.append(f'class {osloDatatype.name}Waarden(AttributeInfo):')
            datablock.append('    def __init__(self, parent=None):')
            datablock.append('        AttributeInfo.__init__(self, parent)')

        self.add_attributen_to_dataBlock(attributen, datablock, forClassUse=False, typeField=typeField)

        if typeField == 'Primitive' or typeField == 'KwantWrd':
            typeField = 'OTL'


        datablock.append(''),
        datablock.append(f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit')
        datablock.append(f'class {osloDatatype.name}({typeField}Field, AttributeInfo):')
        datablock.append(f'    """{osloDatatype.definition}"""')
        datablock.append(f'    naam = {wrap_in_quotes(osloDatatype.name)}')
        datablock.append(f'    label = {wrap_in_quotes(osloDatatype.label)}')
        datablock.append(f'    objectUri = {wrap_in_quotes(osloDatatype.objectUri)}')
        datablock.append(f'    definition = {wrap_in_quotes(osloDatatype.definition)}')
        if osloDatatype.usagenote != '':
            datablock.append(f'    usagenote = {wrap_in_quotes(osloDatatype.usagenote)}')
        if osloDatatype.deprecated_version != '':
            datablock.append(f'    deprecated_version = {wrap_in_quotes(osloDatatype.deprecated_version)}'),
        if typeField == 'OTL':
            datablock.append('    waarde_shortcut_applicable = True')
        datablock.append(f'    waardeObject = {osloDatatype.name}Waarden')
        datablock.append(f'')
        datablock.append(f'    def __str__(self):')
        datablock.append(f'        return {typeField}Field.__str__(self)')
        datablock.append('')

        return datablock

    def get_attributen_by_typeField(self, TypeField, osloDatatype):
        if TypeField == 'Complex':
            return self.oslo_collector.find_complex_datatype_attributes_by_class_uri(osloDatatype.objectUri)
        elif TypeField == 'UnionType':
            return self.oslo_collector.find_union_datatype_attributes_by_class_uri(osloDatatype.objectUri)
        else:
            return self.oslo_collector.find_primitive_datatype_attributes_by_class_uri(osloDatatype.objectUri)

    def add_attributen_to_dataBlock(self, attributen, datablock, forClassUse=False, typeField=''):
        prop_datablock = []
        for attribuut in sorted(attributen, key=lambda a: a.name):
            if attribuut.overerving == 1:
                raise NotImplementedError(f"overerving 1 is not implemented, found in {attributen.objectUri}")

            whitespace = self.get_white_space_equivalent(f'        self._{attribuut.name} = OTLAttribuut(')
            fieldName = self.get_single_field_from_type_uri(attribuut.type)

            datablock.append(f'        self._{attribuut.name} = OTLAttribuut(field={fieldName},')
            datablock.append(f'{whitespace}naam={wrap_in_quotes(attribuut.name)},')
            datablock.append(f'{whitespace}label={wrap_in_quotes(attribuut.label)},')
            datablock.append(f'{whitespace}objectUri={wrap_in_quotes(attribuut.objectUri)},')
            if attribuut.usagenote != '':
                datablock.append(f'{whitespace}usagenote={wrap_in_quotes(attribuut.usagenote)},')
            if attribuut.deprecated_version != '':
                datablock.append(f'{whitespace}deprecated_version={wrap_in_quotes(attribuut.deprecated_version)},')
            if attribuut.constraints != '':
                datablock.append(f'{whitespace}constraints={wrap_in_quotes(attribuut.constraints)},')
            if attribuut.kardinaliteit_min != '1':
                datablock.append(f'{whitespace}kardinaliteit_min={wrap_in_quotes(attribuut.kardinaliteit_min)},')
            if attribuut.kardinaliteit_max != '1':
                datablock.append(f'{whitespace}kardinaliteit_max={wrap_in_quotes(attribuut.kardinaliteit_max)},')
            definitie = wrap_in_quotes(attribuut.definition.replace('\n', ''))
            datablock.append(f'{whitespace}definition={definitie},')
            datablock.append(f'{whitespace}owner=self)')
            datablock.append('')

            ownerself = ', owner=self'
            if not forClassUse:
                ownerself += '._parent'

            prop_datablock.append(f'    @property'),
            prop_datablock.append(f'    def {attribuut.name}(self):'),
            prop_datablock.append(f'        """{attribuut.definition}"""'),
            if typeField == 'KwantWrd' and attribuut.name == 'standaardEenheid':
                prop_datablock.append(f'        return self._{attribuut.name}.usagenote.split(\'"\')[1]'),
            else:
                prop_datablock.append(f'        return self._{attribuut.name}.get_waarde()'),
            prop_datablock.append(f''),
            if not attribuut.readonly:
                prop_datablock.append(f'    @{attribuut.name}.setter'),
                prop_datablock.append(f'    def {attribuut.name}(self, value):'),

                prop_datablock.append(f'        self._{attribuut.name}.set_waarde(value{ownerself})'),
                if typeField == 'UnionType':
                    prop_datablock.append(f'        if value is not None:')
                    prop_datablock.append(f"            self.clear_other_props('_{attribuut.name}')")
                prop_datablock.append(f'')

        for prop_line in prop_datablock:
            datablock.append(prop_line)

        return datablock
