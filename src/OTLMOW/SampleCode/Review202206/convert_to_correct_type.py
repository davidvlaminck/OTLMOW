from OTLMOW.OTLModel.Classes.Onderdeel.Geleideconstructie import Geleideconstructie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField

if __name__ == '__main__':
    afschermende_constructie = Geleideconstructie()
    print(afschermende_constructie.typeURI)

    # afschermende_constructie.isActief = 'true'

    # converted_boolean = BooleanField.convert_to_correct_type('false', log_warnings=False)
    # afschermende_constructie.isActief = converted_boolean

    #afschermende_constructie.theoretischeLevensduur.waarde = 2.1

