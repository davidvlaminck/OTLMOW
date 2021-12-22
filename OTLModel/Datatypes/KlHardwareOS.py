from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHardwareOS(Keuzelijst):
    """vb : Windows 10 SP1, Windows 10 SP2, unix."""

    def __init__(self):
        super().__init__(naam="KlHardwareOS",
                         label="Hardware OS",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareOS",
                         definition="vb : Windows 10 SP1, Windows 10 SP2, unix.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareOS")

        self.add_option("cent-os-linux-7-core", "CentOS Linux 7 (Core)", "CentOS Linux 7 (Core)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/cent-os-linux-7-core")
        self.add_option("unix", "unix", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/unix")
        self.add_option("windows-10-SP2", "windows 10 SP2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/windows-10-SP2")
        self.add_option("windows-10-SP1", "windows 10 SP1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/windows-10-SP1")
