from OTLMOW.Facility.DotnotationHelper import DotnotationHelper
from OTLMOW.OTLModel.Classes.Geleideconstructie import Geleideconstructie

if __name__ == '__main__':
    gc = Geleideconstructie()
    attribute = DotnotationHelper.get_attributes_by_dotnotation(gc, 'productidentificatiecode.producent')
    attribute.set_waarde('demo producent')
    print(attribute.objectUri)
    print(attribute.get_waarde())
    print(gc.create_dict_from_asset())


