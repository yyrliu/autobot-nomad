from nomad.datamodel.metainfo import SynthesisMethod, ProcessStep
from nomad.datamodel import InstrumentReference, CompositeSystemReference

class PerovskiteFilmSynthesis(SynthesisMethod):
    instruments: InstrumentReference
    samples: CompositeSystemReference
    steps: list[ProcessStep]

class AnnealingStep(ProcessStep):
    duration: float  # in seconds
    temperature_steps: list[float]  # in degrees Celsius
    step_durations: list[float]  # in seconds
    slops: list[float]  # in degrees Celsius per second

class SpinCoatingStep(ProcessStep):
    duration: float  # in seconds
    precursor: CompositeSystemReference  # reference to the precursor composition
    solvent: CompositeSystemReference  # reference to the solvent
    rpm_steps: list[float]  # in revolutions per minute
    step_durations: list[float]  # in seconds
    accelerations: list[float]  # in revolutions per minute per second
    dispense_profile: HamiltonDispenseProfileReference  # reference to the dispense profile

class SimpleSpinCoatingStep(SpinCoatingStep):
    pass

class QuechedSpinCoatingStep(SpinCoatingStep):
    antisolvent: CompositeSystemReference  # reference to the antisolvent
    antisolvent_dispense_delay: float  # in seconds
    antisolvent_dispense_profile: HamiltonDispenseProfileReference  # reference to the antisolvent dispense profile