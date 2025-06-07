from nomad.datamodel.metainfo import BaseSection

class HamiltonDispenseProfileReference(BaseSection):
    pass

class DispenseProfile:
    def __init__(self, dispense_height: float, dispense_rate: float, dispense_pattern: str):
        self.dispense_height = dispense_height  # Height above substrate in mm
        self.dispense_rate = dispense_rate        # Dispense rate in uL/s
        self.dispense_pattern = dispense_pattern  # Pattern of dispense (e.g., spiral, linear)

    def to_dict(self):
        return {
            "dispense_height": self.dispense_height,
            "dispense_rate": self.dispense_rate,
            "dispense_pattern": self.dispense_pattern,
        }