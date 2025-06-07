from nomad.datamodel import metainfo

class SpinCoatingStep(metainfo.ProcessStep):
    def __init__(self, duration: float, percursor: str, solvent: str, 
                 rpm_steps: list, step_durations: list, 
                 accelerations: list, dispense_profile: str):
        self.duration = duration  # in seconds
        self.percursor = percursor  # CompositeSystemReference or PerovskiteCompositionSectionReference
        self.solvent = solvent  # CompositeSystemReference
        self.rpm_steps = rpm_steps  # list of rpm values
        self.step_durations = step_durations  # list of durations for each step in seconds
        self.accelerations = accelerations  # list of accelerations in rpm/sec
        self.dispense_profile = dispense_profile  # HamiltonDispenseProfileReference

class AnnealingStep(metainfo.ProcessStep):
    def __init__(self, duration: float, temperature_steps: list, 
                 step_durations: list, slopes: list):
        self.duration = duration  # in seconds
        self.temperature_steps = temperature_steps  # list of temperature values in °C
        self.step_durations = step_durations  # list of durations for each temperature step in seconds
        self.slopes = slopes  # list of slopes in °C/sec

class QuechedSpinCoatingStep(SpinCoatingStep):
    def __init__(self, duration: float, percursor: str, solvent: str, 
                 rpm_steps: list, step_durations: list, 
                 accelerations: list, dispense_profile: str, 
                 antisolvent: str, antisolvent_dispense_delay: float, 
                 antisolvent_dispense_profile: str):
        super().__init__(duration, percursor, solvent, rpm_steps, 
                         step_durations, accelerations, dispense_profile)
        self.antisolvent = antisolvent  # CompositeSystemReference
        self.antisolvent_dispense_delay = antisolvent_dispense_delay  # in seconds
        self.antisolvent_dispense_profile = antisolvent_dispense_profile  # HamiltonDispenseProfileReference

class SimpleSpinCoatingStep(SpinCoatingStep):
    pass  # Inherits all attributes and methods from SpinCoatingStep without additional modifications.