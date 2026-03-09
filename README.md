---

# Interactive Python Calculator

## Overview

This project is an **interactive Python calculator** implemented in a modular and extensible way. It demonstrates advanced Python concepts such as the **Factory Pattern**, **Observer Pattern**, **Memento Pattern**, **custom exceptions**, and **history tracking**. The calculator can perform basic arithmetic operations and supports **history logging**, **auto-save**, and **unit testing** for all functionality.

---

## Features

* **Used "coloroama" to display colored output of calculator.**
* **Supported Arithmetic Operations**

  * Supported Commands:
  * add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff – Perform calculations.
  * history – Display calculation history.
  * clear – Clear calculation history.
  * undo – Undo the last calculation.
  * redo – Redo the last undone calculation.
  * save – Manually save calculation history to file using pandas.
  * load – Load calculation history from file using pandas.
  * help – Display available commands.
  * exit – Exit the application gracefully.

* **Interactive REPL**

  * Users can interactively input calculations
  * Supports commands like `help` and `history`

* **Operation Factory**

  * Dynamically creates arithmetic operation objects
  * Encourages clean, extensible design

* **History Tracking**

  * Stores each calculation performed
  * Supports multiple observers:

    * **LoggingObserver** – logs calculations
    * **AutoSaveObserver** – automatically saves history
  * Implements **Observer Pattern** for easy addition of more observers

* **Memento Pattern**

  * Supports saving and restoring calculator state
  * Useful for undo/redo operations

* **Custom Exceptions**

  * Graceful handling of divide-by-zero and invalid inputs
  * Demonstrates Python’s `try-except` and EAFP/LBYL approaches

* **Logging**

  * Calculation events are logged
  * Observers log messages automatically for monitoring

* **Auto-Save**

  * Automatically saves history to a file if enabled
  * Exceptions during auto-save are caught internally

* **.env File Support**

  * Configuration such as `BASE_DIR` for history files can be loaded from a `.env` file
  * Example `.env`:

    ```env
    BASE_DIR=/path/to/calculator/data
    AUTO_SAVE=True
    LOG_LEVEL=INFO
    ```

* **Testing**

  * Comprehensive **pytest** test coverage
  * Includes `pytest-cov` for measuring coverage
  * Includes a test to validate **import integrity**

---

## Project Structure

```text
calculator-project/
│
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   └── operations.py
│
├── tests/
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_imports.py
│   ├── test_input_validator.py
│   └── test_operations.py
├── .env
├── LICENSE
├── .coverage
├── .coveragerc
├── pytest.ini
├── requirements.txt
├── venv/
└── README.md
```

> **Note:** I have reused a few files from previous assignment examples: `LICENSE`, `.coverage`, `.coveragerc`, `pytest.ini`, `requirements.txt`.

---

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup `.env` file**

Create a `.env` file in the project root with configuration:

```env
BASE_DIR=/path/to/calculator/data
AUTO_SAVE=True
LOG_LEVEL=INFO
```

---

## Usage

1. **Run the Calculator interface**

```bash
python3 -m main.py
```

2. **Perform Operations**

* Example commands:

```text
> add          # adds two numbers
> subtract     # subtracts two numbers
> multiply     # multiplies two numbers
> history      # Show previous calculations
> help         # Show help menu and list of all available commands.
> exit         # Exit calculator
```

3. **Environment Configuration**

* `CALCULATOR_LOG_DIR` – Directory for log files.
* `CALCULATOR_HISTORY_DIR` – Directory for history files.
* `CALCULATOR_MAX_HISTORY_SIZE` – Maximum number of history entries.
* `CALCULATOR_PRECISION` - Number of decimal places for calculations.
* `CALCULATOR_MAX_INPUT_VALUE` - Maximum allowed input value.
* `CALCULATOR_DEFAULT_ENCODING` - Default encoding for file operations.

The calculator reads these values from the `.env` file using Python's `os.environ`.

---

## Features in Action

### 1. REPL Interaction

### 2. History Tracking

### 3. Auto-Save Observer

### 4. Logging Observer

---

## Testing

* **Run all tests**

```bash
pytest
```

* **Run tests with coverage**

```bash
pytest --cov=app --cov-report=html
```

* **Notes**

  * All observers, history tracking, and exceptions are fully tested
  * `# pragma: no cover` is used where automated testing is impractical (e.g., interactive REPL input)
  * Used coloroama to add colors to the calculator output.

---

## Design Patterns Used

* **Factory Pattern** – For creating operation objects dynamically
* **Observer Pattern** – For notifying logging and auto-save observers
* **Memento Pattern** – For saving/restoring calculator state (undo/redo)

---

## Contributing

* Clone the repo, create a branch, implement features or fixes
* Run all tests before creating a pull request
* Follow **PEP8** styling and maintain modularity

---

## License

This project is for **educational purposes** and course assignments.
No commercial license granted. For more details, please read LICENSE file.

---