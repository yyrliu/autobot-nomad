# README for Nomad Perovskite Schema

## Overview

The **Nomad Perovskite Schema** project provides a structured framework for modeling the synthesis of perovskite films, including various process steps such as spin coating, whirl spin coating, and pipette quenching. This project is designed to facilitate the documentation and execution of perovskite synthesis protocols, ensuring reproducibility and clarity in experimental procedures.

## Project Structure

The project is organized into several key directories and files:

- **src/nomad_perovskite_schema/**: The main package containing the core functionality.
  - **basesections/**: Contains definitions for the main classes related to perovskite synthesis and process steps.
    - `perovskite_synthesis.py`: Defines the `PerovskiteFilmSynthesis` class.
    - `process_steps.py`: Defines various process step classes such as `SpinCoatingStep` and `AnnealingStep`.
    - `dispense_profile.py`: Contains classes related to dispensing profiles.
  - **metainfo/**: Contains metadata related to the synthesis and process steps.
  - **utils/**: Contains utility functions, including those for unit conversions.

- **src/tests/**: Contains unit tests for the package to ensure functionality and reliability.
- **examples/**: Provides example scripts demonstrating how to use the classes defined in the package.

## Installation

To install the project, clone the repository and run:

```bash
pip install .
```

## Usage

### Example of Spin Coating

To use the `SpinCoatingStep` class, you can refer to the example provided in `examples/spin_coating_example.py`.

### Running Tests

To run the tests, navigate to the `src` directory and execute:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.