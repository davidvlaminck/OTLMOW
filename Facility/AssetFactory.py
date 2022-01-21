import copy

from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.Classes.AIMObject import AIMObject


class AssetFactory:
    @staticmethod
    def dynamic_create_instance_from_name(class_name):
        try:
            py_mod = __import__(name=f'OTLModel.Classes.{class_name}', fromlist=f'Classes.{class_name}')
        except ModuleNotFoundError:
            return None
        class_ = getattr(py_mod, class_name)
        instance = class_()

        return instance

    def dynamic_create_instance_from_uri(self, class_uri):
        if not class_uri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns'):
            raise ValueError(
                f'{class_uri} is not valid uri, it does not begin with "https://wegenenverkeer.data.vlaanderen.be/ns"')
        class_name = class_uri.split('#')[-1]
        created = self.dynamic_create_instance_from_name(class_name)
        if created is None:
            raise ValueError(f'{class_uri} is likely not valid uri, it does not result in a created instance')
        return created

    def create_aimObject_using_other_aimObject_as_template(self, orig_aimObject, typeURI='', fieldsToCopy=[]):
        """Creates an AIMObject, using another AIMObject as template.
        The parameter typeURI defines the type of the new AIMObject that is created. If omitted, it is assumed the same type as the given aimObject
        The parameter fieldsToCopy dictates what fields are copied from the first object
        When the types do no match, fieldsToCopy can not be empty"""

        if not isinstance(orig_aimObject, AIMObject):
            raise ValueError(f'{orig_aimObject} is not an AIMObject, not supported')

        if typeURI != '':
            if typeURI != orig_aimObject.typeURI and (fieldsToCopy == [] or fieldsToCopy is None):
                raise ValueError("parameter typeURI is different from orig_aimObject. parameter fieldsToCopy cannot be empty")

        if typeURI == '':
            typeURI = orig_aimObject.typeURI
        new_asset = self.dynamic_create_instance_from_uri(typeURI)

        if fieldsToCopy == []:
            fieldsToCopy = self.get_public_fieldlist_from_object(orig_aimObject)

        if 'typeURI' in fieldsToCopy:
            fieldsToCopy.remove('typeURI')
        if 'assetId' in fieldsToCopy:
            fieldsToCopy.remove('assetId')

        self.copy_fields_from_object_to_new_object(orig_aimObject, new_asset, fieldsToCopy)
        return new_asset

    def get_public_fieldlist_from_object(self, orig_asset):
        if orig_asset is None:
            raise ValueError("input can't be None")
        d = dir(orig_asset)
        listFields = []
        for key in d:
            if key[0] == '_' or key in ['attr_info', 'attr_type_info', 'info', 'make_string_version']:
                continue
            else:
                listFields.append(key)

        return listFields

    def copy_fields_from_object_to_new_object(self, orig_object, new_object, fieldList):
        if orig_object is None:
            raise ValueError("parameter orig_object is None")
        if new_object is None:
            raise ValueError("parameter new_object is None")
        if fieldList is None or fieldList == []:
            raise ValueError("parameter fieldList is empty or None")

        distinct_fieldList = list(set(fieldList))

        for fieldName in distinct_fieldList:
            orig_asset_field = getattr(orig_object, fieldName)
            new_object_field_copy = copy.deepcopy(orig_asset_field)
            setattr(new_object, fieldName, new_object_field_copy)
