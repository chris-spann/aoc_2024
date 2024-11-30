## Advent of Code 2024 🎄✨

Welcome to Advent of Code 2024! This repository contains my solutions to the daily programming challenges hosted on Advent of Code.

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/chris-spann/aoc_2024/main.svg)](https://results.pre-commit.ci/latest/github/chris-spann/aoc_2024/main)

### 📊 Progress

| Day  | Part 1 | Part 2 |


---

### 🚀 Project Setup

This project is written in Python and uses [Poetry](https://python-poetry.org/) for dependency management. It also includes a `Makefile` to simplify common tasks like testing, linting, and running solutions.

#### Prerequisites

Ensure the following are installed:
- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation)
- Make (optional but recommended for automation)

---

### 🛠 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chris-spann/aoc_2024.git
   cd aoc_2024
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

---

### 📜 Usage

#### Running Solutions

Each day’s solution can be run using a Makefile command or directly via Python.

##### Option 1: Using Make
Run the solution for a specific day:
```bash
make run_day day=1
```
Replace `1` with the desired day number.


##### Option 2: Using Python
Run the solution directly:
```bash
poetry run python -m solutions.day_1
```

---
### 🛠 Makefile Commands
This project includes a Makefile with the following commands:


| Command        | Description           |
| :------------- |:-------------|
| make test      | Run the test suite using pytest. |
| make lint      | Run code linting and autofix issues with ruff.|
| make format    | Auto-format the codebase using ruff. |
| make generate_day | Generate boilerplate code for a new day.|
| make format    | Auto-format the codebase using ruff. |
| make run_day day=X    | Run the solution for a specific day. |
| make update_progress | Update progress in README.md |


#### Generating a New Day's Solution
To generate boilerplate for a new day:
```bash
make generate_day
```
This runs the `utils/generate_day.py` script to create the necessary files.

---

### 🧪 Testing and Linting

#### Run Tests
Tests are written using `pytest`. Run them with:
```bash
make test
```

#### Lint and Fix Code
Use `ruff` to lint and fix issues:
```bash
make lint
```

Format the code:
```bash
make format
```

---

### 🌟 Contributions

Feel free to fork this repository, open issues, or submit pull requests if you have ideas or improvements. Happy coding! 🎄✨

---
