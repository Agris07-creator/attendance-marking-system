# Multi-Subject Attendance Tracker

> A modular Python utility for tracking subject-wise attendance, computing real-time percentages, and providing predictive insights on safe skips or recovery streaks.

---

## Overview

In many academic institutions, students are required to maintain a mandatory minimum attendance threshold (typically 75% or 80%) to remain eligible for examinations. Mental calculations or static logs often fail to answer the most critical operational questions:

- *"How many classes can I miss without dropping below the requirement?"*
- *"If I'm in the shortage zone, how many consecutive classes must I attend to recover?"*

The **Multi-Subject Attendance Tracker** solves this problem by combining routine attendance logging with dynamic predictive simulation algorithms. The application operates via an intuitive command-line interface (CLI) and is engineered into four decoupled modules separating configuration, core mathematical logic, subject data management, and the application lifecycle.

---

## Features

- **Multi-Subject Management:** Add and manage any number of courses with baseline records (classes held and classes attended).
- **Daily Attendance Logging:** Mark real-time attendance session-by-session using simple affirmative (`y`/`n`) prompts.
- **Accurate Percentage Computation:** Calculates fractional attendance with zero-division safeguards when no classes have occurred yet.
- **Predictive Buffer Calculator (`classes_can_skip`):** Simulates upcoming absences to determine the maximum number of classes a student can safely skip while staying at or above the threshold.
- **Remediation Planner (`classes_must_attend`):** Calculates the exact consecutive attendance streak needed to pull an attendance percentage back up to the required cutoff.
- **Tabular Status Dashboard:** Displays subject statistics in an easy-to-read table with color/text flags (`OK` vs. `LOW`).
- **Modular Codebase:** Cleanly divided into `config.py`, `calculator.py`, `tracker.py`, and `main.py` for maintainability and extensibility.

---

## Technologies & Tools Used

| Component / Tool | Technology / Purpose |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Paradigm** | Procedural / Modular Architecture |
| **Dependencies** | Pure Python Standard Library (No external third-party packages required) |
| **Testing** | Python `unittest` framework |
| **Version Control** | Git / GitHub |

---

## Project Structure

```text
attendance-tracker/
│
├── config.py       # Global constants (e.g., minimum percentage threshold)
├── calculator.py   # Pure math functions (percentages, skips, attendance targets)
├── tracker.py      # Console input/output, subject list mutation, tabular reports
├── main.py         # Entry point and interactive menu loop
├── test_tracker.py # Automated test suite for calculations and edge cases
└── README.md       # Project documentation
```

---

## Installation & Setup

### Prerequisites

Ensure you have **Python 3.8 or higher** installed on your system. You can verify your installation by running:

```bash
python --version
# or
python3 --version
```

### Steps to Run

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/your-username/attendance-tracker.git
   cd attendance-tracker
   ```

2. **Verify File Placement:**
   Make sure all modules (`config.py`, `calculator.py`, `tracker.py`, and `main.py`) reside in the same directory.

3. **Execute the Application:**
   Run the entry module using the Python interpreter:
   ```bash
   python main.py
   # or on macOS/Linux:
   python3 main.py
   ```

---

## Usage Guide

Upon launching the application, you are presented with the interactive menu:

```text
===== Attendance Tracker (Min: 75%) =====
1. Add subject
2. Mark today's attendance
3. View summary (all subjects)
4. Exit
=========================================
Enter choice (1-4):
```

### Example Workflow:
1. **Option 1 (Add Subject):** Input the course name (e.g., `Mathematics`), the total classes held so far (`20`), and the classes attended (`18`).
2. **Option 2 (Mark Today's Attendance):** Select the subject by index and confirm attendance with `y` (attended) or `n` (absent).
3. **Option 3 (View Summary):** View the aggregated dashboard:
   ```text
   Subject         Attended   Total      Percentage   Status
   -------------------------------------------------------
   Mathematics     18         20         90.0%        OK    
      -> Can safely skip 4 more classes and stay above 75%.
   Digital Elect.  13         20         65.0%        LOW   
      -> Must attend next 8 classes in a row to reach 75%.
   ```
4. **Option 4 (Exit):** Terminate the session.

---

## Testing Instructions

### 1. Running Automated Unit Tests

A test script validating mathematical boundary conditions and edge cases can be run using Python's built-in test runner:

```bash
python -m unittest test_tracker.py
```

#### Test Suite Implementation (`test_tracker.py`):
Create this file in the root folder to execute tests:

```python
import unittest
from calculator import attendence_percentage, classes_can_skip, classes_must_attend


class TestAttendanceCalculator(unittest.TestCase):

    def test_zero_total_classes(self):
        """Test zero-division protection when no lectures have taken place."""
        self.assertEqual(attendence_percentage(0, 0), 0.0)

    def test_percentage_calculation(self):
        """Test baseline percentage formula precision."""
        self.assertAlmostEqual(attendence_percentage(18, 20), 90.0)
        self.assertAlmostEqual(attendence_percentage(13, 20), 65.0)

    def test_safe_skip_calculation(self):
        """18/20 = 90%. Skipping 4 classes -> 18/24 = 75.0%."""
        skips = classes_can_skip(attended=18, total=20, min_percentage=75)
        self.assertEqual(skips, 4)

    def test_must_attend_calculation(self):
        """13/20 = 65%. Attending next 8 in a row -> 21/28 = 75.0%."""
        needed = classes_must_attend(attended=13, total=20, min_percentage=75)
        self.assertEqual(needed, 8)


if __name__ == "__main__":
    unittest.main()
```

### 2. Manual Verification Matrix

| Test Scenario | Input Data | Expected Output | Pass / Fail |
| :--- | :--- | :--- | :---: |
| **Zero Classes Held** | `attended = 0`, `total = 0` | Percentage displays `0.0%` without crash | Pass |
| **Exact Threshold** | `attended = 15`, `total = 20` | Percentage `75.0%`, `OK`, 0 safe skips | Pass |
| **Deficit Recovery** | `attended = 12`, `total = 20` (60%) | Percentage `60.0%`, `LOW`, must attend 12 | Pass |
| **Invalid Menu Option** | Choice input `9` or `abc` | Re-prompts menu with `"Invalid choice"` message | Pass |

---

## Author & Academic Information

- **Author:** Anurag
- **Registration No.:** 26BEC10124
- **Course:** Introduction to Problem Solving
- **Slot Allotment:** B11+B12+B13+C14+E11+E12
