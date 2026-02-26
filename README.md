# IS601 Midterm Project

## Advanced Calculator Command-Line Application

Developed for IS601 -- Web Systems Development.

------------------------------------------------------------------------

## Project Overview

This advanced calculator application implements:

-   Advanced arithmetic operations
-   Factory, Memento, and Observer design patterns
-   Undo/Redo functionality
-   Logging and auto-save observers
-   CSV-based history persistence using pandas
-   Environment-based configuration management
-   Robust error handling with custom exceptions
-   Comprehensive unit testing (≥ 90% coverage)
-   GitHub Actions CI pipeline

------------------------------------------------------------------------

## Design Patterns Implemented

### Factory Pattern

Used to dynamically create operation objects.

### Memento Pattern

Implements undo and redo functionality.

### Observer Pattern

-   LoggingObserver → Logs calculation details\
-   AutoSaveObserver → Automatically saves history to CSV

------------------------------------------------------------------------

## Supported Operations

Each operation takes exactly two numerical inputs:

-   add
-   subtract
-   multiply
-   divide
-   power
-   root
-   modulus
-   int_divide
-   percent
-   abs_diff

------------------------------------------------------------------------

## Command-Line Interface (REPL)

Supported Commands:

-   add, subtract, multiply, divide
-   power
-   root
-   modulus
-   int_divide
-   percent
-   abs_diff
-   history
-   clear
-   undo
-   redo
-   save
-   load
-   help
-   exit

------------------------------------------------------------------------

## Installation & Setup

### 1. Clone Repository

git clone <repository-url>\
cd <repository-directory>\

### 2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows

### 3. Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## Configuration (.env Setup)

Create a `.env` file in the project root:

CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=4 
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8

------------------------------------------------------------------------

## Testing & Coverage

Run tests:

pytest

Run with coverage:

pytest --cov=app --cov-report=term

CI enforces minimum 90% coverage.

------------------------------------------------------------------------

## Continuous Integration

GitHub Actions automatically:

-   Installs dependencies
-   Runs tests
-   Enforces coverage threshold

Workflow file:

.github/workflows/python-app.yml

------------------------------------------------------------------------

## Error Handling

Custom exceptions implemented:

-   OperationError
-   ValidationError

Handles:

-   Division by zero
-   Invalid inputs
-   Out-of-range values
-   Malformed CSV files

------------------------------------------------------------------------

## Author

Kundan Singh\
IS601 -- Python for Web API Development\
Spring 2026
