class DispenseProfile:
    def __init__(self, profile_type, parameters):
        self.profile_type = profile_type
        self.parameters = parameters

class HamiltonDispenseProfile(DispenseProfile):
    def __init__(self, dispense_height, dispense_speed, dispense_pattern):
        super().__init__("Hamilton", {"dispense_height": dispense_height, "dispense_speed": dispense_speed, "dispense_pattern": dispense_pattern})
        self.dispense_height = dispense_height
        self.dispense_speed = dispense_speed
        self.dispense_pattern = dispense_pattern

class CustomDispenseProfile(DispenseProfile):
    def __init__(self, custom_parameters):
        super().__init__("Custom", custom_parameters)
        self.custom_parameters = custom_parameters