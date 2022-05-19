import copy

from OTLMOW.OTLModel.Classes.AIMObject import AIMObject


class AssetFactory:
    @staticmethod
    def dynamic_create_instance_from_name(class_name: str, directory:str = 'OTLMOW.OTLModel.Classes'):
        """Loads the OTL class module and attempts to instantiate the class using the name of the class

                :param class_name: class name to instantiate
                :type: str
                :rtype: OTLObject or None
                :return: returns an instance of class_name, that inherits from OTLObject
                """
        try:
            py_mod = __import__(name=f'{directory}.{class_name}', fromlist=f'{directory.split(".")[-1]}.{class_name}')
        except ModuleNotFoundError:
            try:
                py_mod = __import__(name=f'UnitTests.{class_name}', fromlist=f'{class_name}')
            except ModuleNotFoundError:
                return None
        class_ = getattr(py_mod, class_name)
        instance = class_()

        return instance

    def dynamic_create_instance_from_uri(self, class_uri: str, directory:str = 'OTLMOW.OTLModel.Classes'):
        if not class_uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns'):
            raise ValueError(
                f'{class_uri} is not valid uri, it does not begin with "https://wegenenverkeer.data.vlaanderen.be/ns"')
        class_name = class_uri.split('#')[-1]
        created = self.dynamic_create_instance_from_name(class_name, directory=directory)
        if created is None:
            raise ValueError(f'{class_uri} is likely not valid uri, it does not result in a created instance')
        return created

    def create_aimObject_using_other_aimObject_as_template(self, orig_aimObject: AIMObject, typeURI: str = '',
                                                           fields_to_copy: [str] = None, directory: str = 'OTLMOW.OTLModel.Classes'):
        """Creates an AIMObject, using another AIMObject as template.
        The parameter typeURI defines the type of the new AIMObject that is created.
        If omitted, it is assumed the same type as the given aimObject
        The parameter fields_to_copy dictates what fields are copied from the first object
        When the types do no match, fields_to_copy can not be empty"""

        if fields_to_copy is None:
            fields_to_copy = []
        if not isinstance(orig_aimObject, AIMObject):
            raise ValueError(f'{orig_aimObject} is not an AIMObject, not supported')

        if typeURI != '':
            if typeURI != orig_aimObject.typeURI and (fields_to_copy == [] or fields_to_copy is None):
                raise ValueError("parameter typeURI is different from orig_aimObject. parameter fields_to_copy cannot be empty")

        if typeURI == '':
            typeURI = orig_aimObject.typeURI
        new_asset = self.dynamic_create_instance_from_uri(typeURI, directory=directory)

        if len(fields_to_copy) == 0:
            fields_to_copy = self.get_public_field_list_from_object(orig_aimObject)

        if 'typeURI' in fields_to_copy:
            fields_to_copy.remove('typeURI')
        if 'assetId' in fields_to_copy:
            fields_to_copy.remove('assetId')

        self.copy_fields_from_object_to_new_object(orig_aimObject, new_asset, fields_to_copy)
        return new_asset

    @staticmethod
    def get_public_field_list_from_object(orig_asset: AIMObject):
        if orig_asset is None:
            raise ValueError("input can't be None")
        d = dir(orig_asset)

        reserved = ['info_attr', 'info_attr_type', 'info', 'make_string_version', 'create_dict_from_asset', 'list_attributes_and_values_by_dotnotatie']
        listFields = [item for item in d if item[0] != '_' and item not in reserved]

        return listFields

    @staticmethod
    def copy_fields_from_object_to_new_object(orig_object: AIMObject, new_object: AIMObject, field_list: [str]):
        if orig_object is None:
            raise ValueError("parameter orig_object is None")
        if new_object is None:
            raise ValueError("parameter new_object is None")
        if field_list is None or field_list == []:
            raise ValueError("parameter field_list is empty or None")

        distinct_fieldList = list(set(field_list))

        for fieldName in distinct_fieldList:
            orig_asset_attribute_value = getattr(orig_object, fieldName)
            if orig_asset_attribute_value is None:
                continue
            orig_asset_attribute = getattr(orig_object, '_' + fieldName)
            new_object_field_copy = copy.deepcopy(orig_asset_attribute_value)

            new_asset_attribute = getattr(new_object, '_' + fieldName)
            new_asset_attribute.set_waarde(new_object_field_copy)

