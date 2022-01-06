# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMimeType(Keuzelijst):
    """De mime types van bestanden (AWVDocument) beperkt tot mime types voor toegelaten bestandstypen."""

    def __init__(self):
        super().__init__(naam="KlAlgMimeType",
                         label="Mimetype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgMimeType",
                         definition="De mime types van bestanden (AWVDocument) beperkt tot mime types voor toegelaten bestandstypen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMimeType")

        self.add_option("application-acad", "application-acad", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-acad")
        self.add_option("text-html", "text-html", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-html")
        self.add_option("application-pdf", "application-pdf", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-pdf")
        self.add_option("application-rtf", "application-rtf", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-rtf")
        self.add_option("image-tiff", "image-tiff", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-tiff")
        self.add_option("application-vnd.openxmlformats-officedocument.wordprocessingml.document", "application-vnd.openxmlformats-officedocument.wordprocessingml.document", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-vnd.openxmlformats-officedocument.wordprocessingml.document")
        self.add_option("application-vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application-vnd.openxmlformats-officedocument.spreadsheetml.sheet", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        self.add_option("application-zip", "application-zip", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-zip")
        self.add_option("application-xml", "application-xml", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-xml")
        self.add_option("text-csv", "text-csv", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-csv")
        self.add_option("image-dxf", "image-dxf", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-dxf")
        self.add_option("application-rvt", "application-rvt", "Revit project file.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-rvt")
        self.add_option("image-svg", "image-svg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-svg")
        self.add_option("text-xml", "text-xml", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-xml")
        self.add_option("text-rtf", "text-rtf", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-rtf")
        self.add_option("image-jpeg", "image-jpeg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-jpeg")
        self.add_option("video-avi", "video-avi", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/video-avi")
        self.add_option("application-acadmap", "application-acadmap", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-acadmap")
