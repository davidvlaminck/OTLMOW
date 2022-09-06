from OTLMOW.Facility.FileFormats.DictDecoder import DictDecoder
from OTLMOW.Facility.GenericHelper import GenericHelper
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject


class AssetFactory:
    @staticmethod
    def dynamic_create_instance_from_ns_and_name(namespace: str, class_name: str, directory: str = 'OTLMOW.OTLModel.Classes'):
        """Loads the OTL class module and attempts to instantiate the class using the name and namespace of the class

        :param namespace: namespace of the class
        :type: str
        :param class_name: class name to instantiate
        :type: str
        :param directory: directory where the class modules are located, defaults to OTLMOW.OTLModel.Classes
        :type: str
        :return: returns an instance of class_name in the given namespace, located from directory, that inherits from OTLObject
        :rtype: OTLObject or None
        """

        if directory is None:
            directory = 'OTLMOW.OTLModel.Classes'

        if namespace is None:
            namespace = ''
        else:
            namespace = GenericHelper.get_titlecase_ns(namespace) + '.'

        try:
            py_mod = __import__(name=f'{directory}.{namespace}{class_name}', fromlist=f'{directory.split(".")[-1]}.{class_name}')
        except ModuleNotFoundError:
            return None
        class_ = getattr(py_mod, class_name)
        instance = class_()

        return instance

    @staticmethod
    def dynamic_create_instance_from_uri(class_uri: str, directory: str = 'OTLMOW.OTLModel.Classes'):
        if directory is None:
            directory = 'OTLMOW.OTLModel.Classes'

        if not class_uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns'):
            raise ValueError(
                f'{class_uri} is not valid uri, it does not begin with "https://wegenenverkeer.data.vlaanderen.be/ns"')
        ns, name = GenericHelper.get_ns_and_name_from_uri(class_uri)
        created = AssetFactory.dynamic_create_instance_from_ns_and_name(ns, name, directory=directory)
        if created is None:
            raise ValueError(f'{class_uri} is likely not valid uri, it does not result in a created instance')
        return created

    @staticmethod
    def create_aimObject_using_other_aimObject_as_template(orig_aimObject: AIMObject, typeURI: str = '',
                                                           fields_to_copy: [str] = None,
                                                           directory: str = 'OTLMOW.OTLModel.Classes'):
        """Creates an AIMObject, using another AIMObject as template.
        The parameter typeURI defines the type of the new AIMObject that is created.
        If omitted, it is assumed the same type as the given aimObject
        The parameter fields_to_copy dictates what fields are copied from the first object
        When the types do not match, fields_to_copy can not be empty"""

        if directory is None:
            directory = 'OTLMOW.OTLModel.Classes'
        if fields_to_copy is None:
            fields_to_copy = []

        if not isinstance(orig_aimObject, AIMObject):
            raise ValueError(f'{orig_aimObject} is not an AIMObject, not supported')

        if typeURI != '':
            if typeURI != orig_aimObject.typeURI and (fields_to_copy == [] or fields_to_copy is None):
                raise ValueError("parameter typeURI is different from orig_aimObject. parameter fields_to_copy cannot be empty")

        if typeURI == '':
            typeURI = orig_aimObject.typeURI
        new_asset = AssetFactory.dynamic_create_instance_from_uri(typeURI, directory=directory)

        if len(fields_to_copy) == 0:
            fields_to_copy = AssetFactory.get_public_field_list_from_object(orig_aimObject)

        if 'typeURI' in fields_to_copy:
            fields_to_copy.remove('typeURI')
        if 'assetId' in fields_to_copy:
            fields_to_copy.remove('assetId')

        AssetFactory.copy_fields_from_object_to_new_object(orig_aimObject, new_asset, fields_to_copy)
        return new_asset

    @staticmethod
    def get_public_field_list_from_object(orig_asset: AIMObject):
        if orig_asset is None:
            raise ValueError("input can't be None")
        d = dir(orig_asset)

        reserved = ['info_attr', 'info_attr_type', 'info', 'make_string_version', 'create_dict_from_asset',
                    'list_attributes_and_values_by_dotnotation', 'add_valid_relation']
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
        instance_dict = orig_object.create_dict_from_asset(waarde_shortcut=False)
        new_instance_dict = {}

        if instance_dict is None:
            instance_dict = {}

        for fieldName in distinct_fieldList:
            if fieldName not in instance_dict:
                continue
            dictitem = instance_dict[fieldName]
            new_instance_dict[fieldName] = dictitem

        for k, v in new_instance_dict.items():
            DictDecoder.set_value_by_dictitem(new_object, k, v, waarde_shortcut=False)
