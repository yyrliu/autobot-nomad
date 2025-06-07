from nomad.datamodel.metainfo import BaseSection, ProcessStep
from nomad.datamodel import fields

class PerovskiteFilmSynthesis(BaseSection):
    instruments = fields.InstrumentReference()
    samples = fields.CompositeSystemReference()
    steps = fields.List(fields.ProcessStep())

class AnnealingStep(ProcessStep):
    duration = fields.Float(unit='sec')
    temperature_steps = fields.List(fields.Float(unit='°C'))
    step_durations = fields.List(fields.Float(unit='sec'))
    slops = fields.List(fields.Float(unit='°C/sec'))

class SpinCoatingStep(ProcessStep):
    duration = fields.Float(unit='sec')
    precursor = fields.CompositeSystemReference()
    solvent = fields.CompositeSystemReference()
    rpm_steps = fields.List(fields.Float(unit='rpm'))
    step_durations = fields.List(fields.Float(unit='sec'))
    accelerations = fields.List(fields.Float(unit='rpm/sec'))
    dispense_profile = fields.HamiltonDispenseProfileReference()

class SimpleSpinCoatingStep(SpinCoatingStep):
    pass

class QuechedSpinCoatingStep(SpinCoatingStep):
    antisolvent = fields.CompositeSystemReference()
    antisolvent_dispense_delay = fields.Float(unit='sec')
    antisolvent_dispense_profile = fields.HamiltonDispenseProfileReference()