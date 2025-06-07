from nomad_perovskite_schema.basesections.process_steps import SpinCoatingStep, AnnealingStep
from nomad_perovskite_schema.basesections.perovskite_synthesis import PerovskiteFilmSynthesis

# Example of using SpinCoatingStep in a PerovskiteFilmSynthesis workflow

# Create a SpinCoatingStep instance
spin_coating = SpinCoatingStep(
    duration=60.0,  # duration in seconds
    percursor="PerovskiteComposition",  # reference to the percursor
    solvent="SolventReference",  # reference to the solvent
    rpm_steps=[1000, 2000, 3000],  # RPM steps
    step_durations=[10, 20, 30],  # durations for each RPM step
    accelerations=[500, 1000, 1500],  # accelerations in rpm/sec
    dispense_profile="HamiltonDispenseProfile"  # reference to the dispense profile
)

# Create an AnnealingStep instance
annealing = AnnealingStep(
    duration=120.0,  # duration in seconds
    temperature_steps=[100, 150, 200],  # temperature steps in °C
    step_durations=[30, 30, 60],  # durations for each temperature step
    slops=[5, 10, 15]  # temperature slopes in °C/sec
)

# Create a PerovskiteFilmSynthesis instance
perovskite_synthesis = PerovskiteFilmSynthesis(
    instruments=["SpinCoater", "Hotplate"],  # list of instruments used
    samples=["Sample1", "Sample2"],  # list of samples
    steps=[spin_coating, annealing]  # list of process steps
)

# Print the synthesis details
print(perovskite_synthesis)