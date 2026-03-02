# Assignment 6 Midterm Project – Professional Calculator REPL

This project implements a **Professional Calculator REPL** in Python, demonstrating **object-oriented programming**, **factory design patterns**, **error handling**, and **unit testing**.

It builds upon the basic calculator assignments from previous homework, using the same **requirements.txt** and configuration setup for virtual environments, testing, and linting.

---

## Features

1. **REPL Calculator**

   * Perform basic arithmetic operations: `add`, `subtract`, `multiply`, `divide`.
   * Supports floating-point numbers.
   * Handles invalid inputs gracefully using **EAFP** and **LBYL** programming paradigms.

2. **Calculation Classes**

   * `Calculation` abstract base class defines a consistent interface for all operations.
   * Concrete subclasses: `AddCalculation`, `SubtractCalculation`, `MultiplyCalculation`, `DivideCalculation`.
   * Factory pattern via `CalculationFactory` allows dynamic creation of calculation objects.

3. **Operations Module**

   * `Operation` class implements static methods: `addition`, `subtraction`, `multiplication`, `division`.
   * Division by zero is checked at the **operation level**, preventing runtime errors.

4. **History and Help**

   * `history` command shows a list of all calculations performed in the session.
   * `help` command displays usage instructions and supported operations.

5. **Error Handling**

   * Invalid input, unknown operations, and division by zero are all handled gracefully.
   * Supports **KeyboardInterrupt (Ctrl+C)** and **EOF (Ctrl+D)** for exiting.

6. **Unit Tests**

   * `pytest` tests for all modules:

     * `test_operations.py` – tests the arithmetic operations.
     * `test_calculation.py` – tests the calculation classes and factory.
     * `test_calculator.py` – tests the REPL flow, including history, help, and error handling.

---

## Project Structure

```
assignment6-midterm/
│
├── app/
│   ├── operations.py
│   ├── calculation.py
│   └── calculator.py
│
├── tests/
│   ├── test_operations.py
│   ├── test_calculation.py
│   └── test_calculator.py
│
├── requirements.txt   # Reused from previous assignments
├── pytest.ini         # Reused basic configuration
└── README.md
```

---

## Getting Started

1. **Create virtual environment** (if not already done in previous homework):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Calculator REPL**:

   ```bash
   python3 main.py
   ```

4. **Run Tests**:

   ```bash
   pytest
   ```

---

## Example REPL Session

```
Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.

>> add 2 3
Result: AddCalculation: 2.0 Add 3.0 = 5.0

>> divide 10 0
Error: division by zero is not allowed.

>> history
1. AddCalculation: 2.0 Add 3.0 = 5.0

>> help
Calculator Help
---------------
Format:
    <operation> <number1> <number2>
Supported operations:
    add
    subtract
    multiply
    divide
Special commands:
    history
    help
    exit
Example:
    add 5 10

>> exit
Goodbye!
```

---

## Development Notes

### LBYL vs EAFP

* **LBYL (Look Before You Leap)** – Check inputs or conditions before performing an operation (e.g., verifying operands before creating a calculation).
* **EAFP (Easier to Ask Forgiveness than Permission)** – Attempt an operation and handle exceptions if they occur (e.g., catching `ValueError` from unsupported operations).
* This project uses **both paradigms** for robust and Pythonic error handling.

### Factory Pattern

* `CalculationFactory` dynamically creates calculation objects based on a string identifier (`add`, `subtract`, etc.).
* Adding new operations (like `power`) requires **minimal code changes**: register a new subclass with the factory.

### Class Hierarchy

```
Calculation (ABC)
│
├── AddCalculation
├── SubtractCalculation
├── MultiplyCalculation
└── DivideCalculation
```

* All subclasses implement the abstract `execute()` method.
* The `__str__()` method of `Calculation` standardizes output formatting for all operations.

### Error Handling

* **Division by zero** is checked centrally in `Operation.division()`.
* REPL captures all **unexpected errors**, prints a friendly message, and continues running.

---

## Notes

* All **requirements.txt** and configuration files are reused from previous homework assignments.
* The project emphasizes **clean, modular design**, **error handling**, and **unit testing** best practices.
* The REPL interface is designed to be **user-friendly** and **extensible** for future operations.