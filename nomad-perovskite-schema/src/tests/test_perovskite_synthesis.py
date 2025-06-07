from nomad_perovskite_schema.basesections.perovskite_synthesis import PerovskiteFilmSynthesis
from nomad_perovskite_schema.basesections.process_steps import SpinCoatingStep, AnnealingStep
import unittest

class TestPerovskiteFilmSynthesis(unittest.TestCase):

    def setUp(self):
        self.synthesis = PerovskiteFilmSynthesis(
            instruments=["Spin Coater", "Hotplate"],
            samples=["Sample A", "Sample B"],
            steps=[
                SpinCoatingStep(
                    duration=60.0,
                    percursor="Perovskite Composition A",
                    solvent="Solvent A",
                    rpm_steps=[1000, 2000],
                    step_durations=[30.0, 30.0],
                    accelerations=[500, 1000],
                    dispense_profile="Dispense Profile A"
                ),
                AnnealingStep(
                    duration=120.0,
                    temperature_steps=[100.0, 150.0],
                    step_durations=[60.0, 60.0],
                    slops=[5.0]
                )
            ]
        )

    def test_instruments(self):
        self.assertEqual(len(self.synthesis.instruments), 2)
        self.assertIn("Spin Coater", self.synthesis.instruments)

    def test_samples(self):
        self.assertEqual(len(self.synthesis.samples), 2)
        self.assertIn("Sample A", self.synthesis.samples)

    def test_steps(self):
        self.assertEqual(len(self.synthesis.steps), 2)
        self.assertIsInstance(self.synthesis.steps[0], SpinCoatingStep)
        self.assertIsInstance(self.synthesis.steps[1], AnnealingStep)

    def test_spin_coating_step(self):
        spin_step = self.synthesis.steps[0]
        self.assertEqual(spin_step.duration, 60.0)
        self.assertEqual(spin_step.percursor, "Perovskite Composition A")
        self.assertEqual(spin_step.solvent, "Solvent A")
        self.assertEqual(spin_step.rpm_steps, [1000, 2000])
        self.assertEqual(spin_step.step_durations, [30.0, 30.0])
        self.assertEqual(spin_step.accelerations, [500, 1000])
        self.assertEqual(spin_step.dispense_profile, "Dispense Profile A")

    def test_annealing_step(self):
        annealing_step = self.synthesis.steps[1]
        self.assertEqual(annealing_step.duration, 120.0)
        self.assertEqual(annealing_step.temperature_steps, [100.0, 150.0])
        self.assertEqual(annealing_step.step_durations, [60.0, 60.0])
        self.assertEqual(annealing_step.slops, [5.0])

if __name__ == '__main__':
    unittest.main()