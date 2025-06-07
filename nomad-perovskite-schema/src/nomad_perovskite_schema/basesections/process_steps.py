from nomad.datamodel.metainfo import ProcessStep
from typing import List, Optional

class SpinCoatingStep(ProcessStep):
    def __init__(self, duration: float, 
                 percursor: Optional[str], 
                 solvent: Optional[str], 
                 rpm_steps: List[float], 
                 step_durations: List[float], 
                 accelerations: List[float], 
                 dispense_profile: Optional[str]):
        super().__init__()
        self.duration = duration  # in seconds
        self.percursor = percursor  # reference to the perovskite composition
        self.solvent = solvent  # reference to the solvent
        self.rpm_steps = rpm_steps  # list of RPM steps
        self.step_durations = step_durations  # list of durations for each step
        self.accelerations = accelerations  # list of accelerations for each step
        self.dispense_profile = dispense_profile  # reference to the dispense profile

class AnnealingStep(ProcessStep):
    def __init__(self, duration: float, 
                 temperature_steps: List[float], 
                 step_durations: List[float], 
                 slops: List[float]):
        super().__init__()
        self.duration = duration  # in seconds
        self.temperature_steps = temperature_steps  # list of temperatures in °C
        self.step_durations = step_durations  # list of durations for each temperature step
        self.slops = slops  # list of temperature slopes in °C/sec

class QuechedSpinCoatingStep(SpinCoatingStep):
    def __init__(self, duration: float, 
                 percursor: Optional[str], 
                 solvent: Optional[str], 
                 rpm_steps: List[float], 
                 step_durations: List[float], 
                 accelerations: List[float], 
                 dispense_profile: Optional[str], 
                 antisolvent: Optional[str], 
                 antisolvent_dispense_delay: float, 
                 antisolvent_dispense_profile: Optional[str]):
        super().__init__(duration, percursor, solvent, rpm_steps, step_durations, accelerations, dispense_profile)
        self.antisolvent = antisolvent  # reference to the antisolvent
        self.antisolvent_dispense_delay = antisolvent_dispense_delay  # delay before dispensing antisolvent
        self.antisolvent_dispense_profile = antisolvent_dispense_profile  # reference to the antisolvent dispense profile

class SimpleSpinCoatingStep(SpinCoatingStep):
    pass  # Inherits everything from SpinCoatingStep without additional attributes