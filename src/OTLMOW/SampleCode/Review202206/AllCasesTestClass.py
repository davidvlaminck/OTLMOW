from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObjectHelper
from TestClasses.OTLModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


if __name__ == '__main__':
    instance = AllCasesTestClass()
    instance.isActief = True
    instance.toestand = 'in-gebruik'

    instance.testKeuzelijstMetKard = ['waarde-1', 'waarde-2']
    instance.testComplexType.testStringField = 'waarde in complex datatype'
    instance.testComplexType.testBooleanField = True

    print(OTLObjectHelper.build_string_version(instance))


