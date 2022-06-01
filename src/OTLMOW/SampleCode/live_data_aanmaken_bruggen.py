from datetime import datetime

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OEFModel.Classes.Brug import Brug
from OTLMOW.OTLModel.Classes.Brugdeel import Brugdeel
from OTLMOW.OTLModel.Classes.Brugdek import Brugdek
from OTLMOW.OTLModel.Classes.Hoofdligger import Hoofdligger
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Landhoofd import Landhoofd
from OTLMOW.OTLModel.Classes.LigtOp import LigtOp
from OTLMOW.OTLModel.Classes.Oplegging import Oplegging
from OTLMOW.OTLModel.Classes.Oplegrij import Oplegrij
from OTLMOW.OTLModel.Classes.Pijler import Pijler
from OTLMOW.OTLModel.Classes.VakwerkElement import VakwerkElement
from OTLMOW.OTLModel.Classes.Vlotplaat import Vlotplaat

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json",
                               enable_relation_features=True)

    brug = Brug()
    brug.naam = 'Testbrug'
    brug.toestand = 'in-gebruik'
    brug.assetId.identificator = 'Testbrug'

    brugdeel1 = Brugdeel()
    brugdeel1.naam = 'brugdeel1'
    brugdeel1.toestand = 'in-gebruik'
    brugdeel1.assetId.identificator = 'brugdeel1'

    brugdeel1_brug = otl_facility.relatie_creator.create_relation(bron=brugdeel1, doel=brug, relatie=HoortBij)

    brugdeel2 = Brugdeel()
    brugdeel2.naam = 'brugdeel2'
    brugdeel2.toestand = 'in-gebruik'
    brugdeel2.assetId.identificator = 'brugdeel2'

    brugdeel2_brug = otl_facility.relatie_creator.create_relation(bron=brugdeel2, doel=brug, relatie=HoortBij)

    lijst_otl_objecten = [brug, brugdeel1, brugdeel2, brugdeel1_brug, brugdeel2_brug]

    for index, brugdeel in enumerate([brugdeel1, brugdeel2]):
        brugdek = Brugdek()
        brugdek.naam = f'brugdek{index+1}'
        brugdek.toestand = 'in-gebruik'
        brugdek.assetId.identificator = f'brugdek{index+1}'

        lijst_otl_objecten.append(brugdek)

        relatie_brugdek_brugdeel = otl_facility.relatie_creator.create_relation(bron=brugdek, doel=brugdeel, relatie=HoortBij)
        lijst_otl_objecten.append(relatie_brugdek_brugdeel)

    for index in range(1,3):
        landhoofd = Landhoofd()
        landhoofd.toestand = 'in-gebruik'
        landhoofd.assetId.identificator = f'landhoofd{index}'

        lijst_otl_objecten.append(landhoofd)

        relatie_landhoofd_brug = otl_facility.relatie_creator.create_relation(bron=landhoofd, doel=brug, relatie=HoortBij)
        lijst_otl_objecten.append(relatie_landhoofd_brug)

    landhoofden = list(filter(lambda x: isinstance(x, Landhoofd), lijst_otl_objecten))
    for index, landhoofd in enumerate(landhoofden):
        oplegrij = Oplegrij()
        oplegrij.naam = f'oplegrij{index+1}'
        oplegrij.toestand = 'in-gebruik'
        oplegrij.assetId.identificator = f'oplegrij{index+1}'

        lijst_otl_objecten.append(oplegrij)

        relatie_oplegrij_landhoofd = otl_facility.relatie_creator.create_relation(bron=oplegrij, doel=landhoofd, relatie=LigtOp)
        lijst_otl_objecten.append(relatie_oplegrij_landhoofd)
        relatie_oplegrij_brug = otl_facility.relatie_creator.create_relation(bron=oplegrij, doel=brug, relatie=HoortBij)
        lijst_otl_objecten.append(relatie_oplegrij_brug)
        brugdeel = next(x for x in lijst_otl_objecten if isinstance(x, Brugdeel) and str(index+1) in x.naam)
        relatie_oplegrij_brugdeel = otl_facility.relatie_creator.create_relation(bron=brugdeel, doel=oplegrij, relatie=LigtOp)
        lijst_otl_objecten.append(relatie_oplegrij_brugdeel)

    pijler = Pijler()
    pijler.toestand = 'in-gebruik'
    pijler.assetId.identificator = 'pijler_midden'
    lijst_otl_objecten.append(pijler)

    relatie_pijler_brug = otl_facility.relatie_creator.create_relation(bron=pijler, doel=brug, relatie=HoortBij)
    lijst_otl_objecten.append(relatie_pijler_brug)

    for index, brugdeel in enumerate([brugdeel1, brugdeel2]):
        oplegrij = Oplegrij()
        oplegrij.naam = f'oplegrij{index+3}'
        oplegrij.toestand = 'in-gebruik'
        oplegrij.assetId.identificator = f'oplegrij{index+3}'

        lijst_otl_objecten.append(oplegrij)

        relatie_oplegrij_brugdeel = otl_facility.relatie_creator.create_relation(bron=brugdeel, doel=oplegrij, relatie=LigtOp)
        lijst_otl_objecten.append(relatie_oplegrij_brugdeel)

        relatie_oplegrij_pijler = otl_facility.relatie_creator.create_relation(bron=oplegrij, doel=pijler, relatie=LigtOp)
        lijst_otl_objecten.append(relatie_oplegrij_pijler)

    for index, oplegrij in enumerate(list(filter(lambda x: isinstance(x, Oplegrij), lijst_otl_objecten))):
        oplegging = Oplegging()
        oplegging.toestand = 'in-gebruik'
        oplegging.assetId.identificator = f'oplegging{index+1}'

        lijst_otl_objecten.append(oplegging)

        relatie_oplegrij_oplegging = otl_facility.relatie_creator.create_relation(bron=oplegging, doel=oplegrij, relatie=HoortBij)
        lijst_otl_objecten.append(relatie_oplegrij_oplegging)

    for index, brugdek in enumerate(list(filter(lambda x: isinstance(x, Brugdek), lijst_otl_objecten))):
        hoofdligger = Hoofdligger()
        hoofdligger.toestand = 'in-gebruik'
        hoofdligger.assetId.identificator = f'hoofdligger{index+1}'

        lijst_otl_objecten.append(hoofdligger)

        relatie_hoofdligger_brugdek = otl_facility.relatie_creator.create_relation(bron=hoofdligger, doel=brugdek, relatie=HoortBij)
        lijst_otl_objecten.append(relatie_hoofdligger_brugdek)

    vakwerkElement = VakwerkElement()
    vakwerkElement.toestand = 'in-gebruik'
    vakwerkElement.assetId.identificator = f'vakwerkElement'

    lijst_otl_objecten.append(vakwerkElement)

    relatie_hoofdligger_brugdek = otl_facility.relatie_creator.create_relation(bron=vakwerkElement, doel=list(filter(lambda x: isinstance(x, Hoofdligger), lijst_otl_objecten))[0], relatie=HoortBij)
    lijst_otl_objecten.append(relatie_hoofdligger_brugdek)

    # for index, landhoofd in enumerate(list(filter(lambda x: isinstance(x, Landhoofd), lijst_otl_objecten))):
    #     damwand = Damwand()
    #     damwand.toestand = 'in-gebruik'
    #     damwand.assetId.identificator = f'damwand{index + 1}'
    #
    #     lijst_otl_objecten.append(damwand)
    #
    #     relatie_damwand_landhoofd = otl_facility.relatie_creator.create_relation(bron=damwand, doel=landhoofd,
    #                                                                                relatie=HoortBij)
    #     lijst_otl_objecten.append(relatie_damwand_landhoofd)

    for index, landhoofd in enumerate(list(filter(lambda x: isinstance(x, Landhoofd), lijst_otl_objecten))):
        vlotplaat = Vlotplaat()
        vlotplaat.toestand = 'in-gebruik'
        vlotplaat.assetId.identificator = f'vlotplaat{index + 1}'

        lijst_otl_objecten.append(vlotplaat)

        relatie_vlotplaat_landhoofd = otl_facility.relatie_creator.create_relation(bron=vlotplaat, doel=landhoofd,
                                                                                   relatie=HoortBij)
        lijst_otl_objecten.append(relatie_vlotplaat_landhoofd)



    # encode to a json representation
    encoded_json = otl_facility.encoder.encode(lijst_otl_objecten)
    print(encoded_json)

    # write the json file
    filepath = f'Output/{datetime.now().strftime("%Y%m%d%H%M%S")}_export_RLC_SNC.json'
    otl_facility.encoder.write_json_to_file(encoded_json, filepath)

    otl_facility.visualiser.show(lijst_otl_objecten)
