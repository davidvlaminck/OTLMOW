import copy
from datetime import datetime

from OTLModel.ClassLoader import ClassLoader
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


class EMInfraDecoder:
    def decode(self, responseString):
        dict_obj = json.loads(responseString)
        lijst = []
        for obj in dict_obj["@graph"]:
            typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

            if 'https://wegenenverkeer.data.vlaanderen.be/ns' not in typeURI:
                continue

            instance = ClassLoader().dynamic_create_instance_from_uri(typeURI)
            lijst.append(instance)

            for key, value in obj.items():
                if key.startswith('@') or 'typeURI' in key or value == '' or 'toezichter' in key or 'puntlocatie' in key:
                    continue
                if 'geometrie' in key:
                    key = 'loc:Locatie.geometry'

                self.set_attribute(instance, key, value)

        return lijst

    def set_attribute(self, instance, attr_key, value):
        attrnaam = attr_key.split('.')[-1]
        attribute = getattr(instance, attrnaam)
        if isinstance(attribute, KeuzelijstField):
            attribute.set_value_by_invulwaarde(value.split('/')[-1])
        elif isinstance(attribute, ComplexField):
            for k, v in value.items():
                self.set_attribute(attribute, k, v)
        elif isinstance(attribute, DateField):
            attribute.waarde = datetime.strptime(value, '%Y-%m-%d')
        elif isinstance(attribute, KardinaliteitField):
            lijstValues = []
            for valueDict in value:
                attributeInstance = copy.deepcopy(attribute.fieldToMultiply)
                for k, v in valueDict.items():
                    self.set_attribute(attributeInstance, k, v)
                lijstValues.append(attributeInstance)
            attribute.waarde = lijstValues
        else:
            attribute.waarde = value