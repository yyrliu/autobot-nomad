from nomad_perovskite_schema.basesections.process_steps import WhirlSpinCoatingStep, AnnealingStep
from nomad_perovskite_schema.basesections.perovskite_synthesis import PerovskiteFilmSynthesis

# Example of using the WhirlSpinCoatingStep class

# Create an instance of the WhirlSpinCoatingStep
whirl_spin_coating = WhirlSpinCoatingStep(
    duration=60.0,  # duration in seconds
    percursor="PerovskiteComposition",  # reference to the percursor
    solvent="SolventReference",  # reference to the solvent
    rpm_steps=[1000, 2000, 3000],  # RPM steps
    step_durations=[10, 20, 30],  # durations for each RPM step
    accelerations=[500, 1000, 1500],  # accelerations for each step
    antisolvent="AntisolventReference",  # reference to the antisolvent
    antisolvent_dispense_delay=5.0,  # delay before dispensing antisolvent
    antisolvent_dispense_profile="DispenseProfileReference"  # reference to dispense profile
)

# Create an instance of the PerovskiteFilmSynthesis
perovskite_synthesis = PerovskiteFilmSynthesis(
    instruments=["Spin Coater", "Hot Plate"],  # list of instruments used
    samples=["Sample1", "Sample2"],  # list of samples
    steps=[whirl_spin_coating]  # list of process steps
)

# Print the details of the synthesis process
print(perovskite_synthesis)