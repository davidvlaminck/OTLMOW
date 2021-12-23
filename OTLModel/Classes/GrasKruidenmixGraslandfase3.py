from OTLModel.Classes.Grasland import Grasland
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNSB import KlNSB


# Generated with OTLClassCreator
class GrasKruidenmixGraslandfase3(Grasland):
    """G3 - Fijn mozaïek van grassen en kruiden zoals:
beemdlangbloem, gewone berenklauw,
gewoon duizendblad, gewoon reukgras,
glanshaver, grasmuur, grote vossenstaart,
hopklaver, kleine klaver, pastinaak, peen,
rietzwenkgras, rode klaver, rood zwenkgras,
scherpe boterbloem, sint-Janskruid, smalle
weegbree, timotee, veldbeemdgras,
veldzuring, gewoon biggenkruid, kamgras,
veldgerst, vijfvingerkruid."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrasKruidenmixGraslandfase3"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.huidigNatuurbeeld = KeuzelijstField(naam="huidigNatuurbeeld",
                                                 label="huidig natuurbeeld",
                                                 lijst=KlNSB(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrasKruidenmixGraslandfase3.huidigNatuurbeeld",
                                                 definition="Bepaling van het vegetatietype op basis van terreininventarisatie.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """Bepaling van het vegetatietype op basis van terreininventarisatie."""
