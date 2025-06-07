from nomad_perovskite_schema.basesections.process_steps import PipetteQuenchingStep

def create_pipette_quenching_example():
    # Create an instance of PipetteQuenchingStep
    pipette_quenching = PipetteQuenchingStep(
        duration=60.0,  # Duration in seconds
        pipette_rack_number="Rack 1",
        tip_type="Tip A",
        solution_number="Solution 1",
        solution_volume=100.0,  # Volume in uL
        solvent_station_number="Solvent Station 1",
        dispense_height=5.0,  # Height in mm
        quench_solution_number="Quench Solution 1",
        quench_volume=50.0,  # Volume in uL
        quench_height=3.0,  # Height in mm
        quench_dispense_delay=10.0,  # Delay in seconds
        second_spin_acceleration=3000.0,  # Acceleration in rpm/s
        second_spin_time=30.0,  # Time in seconds
        second_spin_velocity=2000.0,  # Velocity in rpm
        annealing_station_number="Annealing Station 1",
        annealing_temperature=100.0,  # Temperature in °C
        annealing_time=120.0  # Time in seconds
    )

    # Print the details of the pipette quenching step
    print("Pipette Quenching Step Details:")
    print(f"Duration: {pipette_quenching.duration} seconds")
    print(f"Pipette Rack Number: {pipette_quenching.pipette_rack_number}")
    print(f"Tip Type: {pipette_quenching.tip_type}")
    print(f"Solution Number: {pipette_quenching.solution_number}")
    print(f"Solution Volume: {pipette_quenching.solution_volume} uL")
    print(f"Solvent Station Number: {pipette_quenching.solvent_station_number}")
    print(f"Dispense Height: {pipette_quenching.dispense_height} mm")
    print(f"Quench Solution Number: {pipette_quenching.quench_solution_number}")
    print(f"Quench Volume: {pipette_quenching.quench_volume} uL")
    print(f"Quench Height: {pipette_quenching.quench_height} mm")
    print(f"Quench Dispense Delay: {pipette_quenching.quench_dispense_delay} seconds")
    print(f"Second Spin Acceleration: {pipette_quenching.second_spin_acceleration} rpm/s")
    print(f"Second Spin Time: {pipette_quenching.second_spin_time} seconds")
    print(f"Second Spin Velocity: {pipette_quenching.second_spin_velocity} rpm")
    print(f"Annealing Station Number: {pipette_quenching.annealing_station_number}")
    print(f"Annealing Temperature: {pipette_quenching.annealing_temperature} °C")
    print(f"Annealing Time: {pipette_quenching.annealing_time} seconds")

if __name__ == "__main__":
    create_pipette_quenching_example()