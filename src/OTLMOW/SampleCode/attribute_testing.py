from OTLMOW.Facility.DotnotationHelper import DotnotationHelper
from OTLMOW.OTLModel.Classes.Geleideconstructie import Geleideconstructie

if __name__ == '__main__':
    gc = Geleideconstructie()
    gc.totaleLengte.waarde = 50
    print(gc.create_dict_from_asset(waarde_shortcut=True))
