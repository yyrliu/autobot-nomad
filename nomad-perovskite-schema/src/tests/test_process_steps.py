import unittest
from nomad_perovskite_schema.basesections.process_steps import SpinCoatingStep, AnnealingStep, QuechedSpinCoatingStep

class TestProcessSteps(unittest.TestCase):

    def test_spin_coating_step(self):
        step = SpinCoatingStep(
            duration=60.0,
            percursor="PerovskiteComposition",
            solvent="SolventA",
            rpm_steps=[1000, 2000],
            step_durations=[10, 50],
            accelerations=[500],
            dispense_profile="HamiltonDispenseProfile"
        )
        self.assertEqual(step.duration, 60.0)
        self.assertEqual(step.percursor, "PerovskiteComposition")
        self.assertEqual(step.solvent, "SolventA")
        self.assertEqual(step.rpm_steps, [1000, 2000])
        self.assertEqual(step.step_durations, [10, 50])
        self.assertEqual(step.accelerations, [500])
        self.assertEqual(step.dispense_profile, "HamiltonDispenseProfile")

    def test_annealing_step(self):
        step = AnnealingStep(
            duration=120.0,
            temperature_steps=[100, 150],
            step_durations=[30, 90],
            slops=[5, 10]
        )
        self.assertEqual(step.duration, 120.0)
        self.assertEqual(step.temperature_steps, [100, 150])
        self.assertEqual(step.step_durations, [30, 90])
        self.assertEqual(step.slops, [5, 10])

    def test_quenched_spin_coating_step(self):
        step = QuechedSpinCoatingStep(
            duration=75.0,
            percursor="PerovskiteComposition",
            solvent="SolventB",
            rpm_steps=[1500, 2500],
            step_durations=[15, 60],
            accelerations=[600],
            dispense_profile="HamiltonDispenseProfile",
            antisolvent="AntisolventA",
            antisolvent_dispense_delay=5.0,
            antisolvent_dispense_profile="HamiltonDispenseProfile"
        )
        self.assertEqual(step.duration, 75.0)
        self.assertEqual(step.percursor, "PerovskiteComposition")
        self.assertEqual(step.solvent, "SolventB")
        self.assertEqual(step.rpm_steps, [1500, 2500])
        self.assertEqual(step.step_durations, [15, 60])
        self.assertEqual(step.accelerations, [600])
        self.assertEqual(step.dispense_profile, "HamiltonDispenseProfile")
        self.assertEqual(step.antisolvent, "AntisolventA")
        self.assertEqual(step.antisolvent_dispense_delay, 5.0)
        self.assertEqual(step.antisolvent_dispense_profile, "HamiltonDispenseProfile")

if __name__ == '__main__':
    unittest.main()