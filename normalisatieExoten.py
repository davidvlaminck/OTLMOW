from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger
from OTLModel.Classes.InvasieveExoten import InvasieveExoten


def normaliseer_exoten():
    # create the main facade class: OTLFacility
    logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
    otl_facility = OTLFacility(logger)

    # import from a Davie json file
    jsonPath = "C:\\resources\\DAVIE_export_exoten.json"
    lijst_exoten = otl_facility.davieImporter.import_file(jsonPath)

    # loop through all objects and create an instance of InvasieveExoten
    lijst_objecten = []
    for exoten in lijst_exoten:
        i = InvasieveExoten()
        i.assetId.identificator.waarde = f'nieuwe_versie_van_{exoten.assetId.identificator.waarde}'
        i.lengte.waarde = exoten.lengte.waarde
        i.breedte.waarde = exoten.breedte.waarde
        i.isActief.waarde = exoten.isActief.waarde
        i.geometry.waarde = exoten.geometry.waarde
        i.toestand.set_value_by_invulwaarde(exoten.toestand.waarde.invulwaarde)
        i.notitie.waarde = exoten.notitie.waarde
        i.bestekPostNummer.waarde = exoten.bestekPostNummer.waarde
        i.datumOprichtingObject.waarde = exoten.datumOprichtingObject.waarde
        i.drassigheid.set_value_by_invulwaarde(exoten.drassigheid.waarde.invulwaarde)
        i.heeftObstakels.waarde = exoten.heeftObstakels.waarde
        i.oppervlakte.waarde = exoten.oppervlakte.waarde
        i.soort.waarde = exoten.soort.waarde
        i.standaardBestekPostNummer.waarde = exoten.standaardBestekPostNummer.waarde
        i.taludwaarde.set_value_by_invulwaarde(exoten.taludwaarde.waarde.invulwaarde)
        i.theoretischeLevensduur.waarde = exoten.theoretischeLevensduur.waarde
        lijst_objecten.append(i)

        # also set isActief to False to soft-delete Exoten
        exoten.isActief.waarde = False
        lijst_objecten.append(exoten)

    # write to a json file that can be uploaded in Davie
    otl_facility.davieExporter.export_objects_to_json_file(lijst_objecten, 'C:\\resources\\DAVIE_exoten_normalisatie.json')

