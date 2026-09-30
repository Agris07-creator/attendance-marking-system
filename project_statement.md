# Project Statement: Multi-Subject Attendance Tracker

## 1. Problem Statement
Academic institutions frequently mandate a minimum attendance threshold (typically 75%) to qualify for examinations and maintain good academic standing. However, students often encounter several difficulties in managing their attendance:
- **Lack of Visibility:** Manual calculation across multiple concurrent subjects is error-prone, tedious, and rarely maintained consistently.
- **Unclear Margin for Absence:** Students struggle to calculate how many upcoming sessions they can safely afford to miss without falling below the required percentage.
- **Absence of Recovery Pathways:** When attendance dips below the threshold, students lack clear, quantitative insight into how many consecutive sessions they must attend to restore their eligibility.

The **Multi-Subject Attendance Tracker** solves this by centralizing subject attendance data, automating percentage tracking, and providing proactive decision support.

---

## 2. Scope of the Project

### In-Scope
- **Subject Management:** Dynamic addition of course/subject profiles with initial baseline records (held vs. attended sessions).
- **Daily Attendance Marking:** Fast daily logging workflow to record presence or absence for any tracked subject.
- **Metric Computation:** Accurate calculation of percentage metrics based on cumulative class data.
- **Predictive Guidance:**
  - Calculation of "safe skips" when above the minimum threshold ($75\%$).
  - Calculation of "mandatory attendance streaks" when below the threshold.
- **Console Interface:** Interactive command-line interface (CLI) for data input and tabular reporting.

### Out-of-Scope (Future Enhancements)
- Persistent file or database storage (e.g., SQLite, JSON exports).
- Time-table scheduling and automated notification/alarm integrations.
- Graphical User Interface (GUI) or mobile/web applications.
- Multi-user authentication and role-based permissions.

---

## 3. Target Users
- **College and University Students:** Students balancing multiple courses with strict institutional attendance criteria.
- **High School Students:** Learners seeking to monitor attendance compliance across varied academic subjects.
- **Academic Mentors & Counselors:** Mentors who need a lightweight tool to quickly evaluate a student's risk profile and provide concrete recovery advice.

---

## 4. High-Level Features

| Feature | Description |
| :--- | :--- |
| **Multi-Subject Management** | Register subjects individually with custom initial states for total classes conducted and classes attended. |
| **Interactive Daily Logging** | Prompt-driven interface enabling users to pick a subject and quickly increment attendance records (`y` for present, `n` for absent). |
| **Live Metric & Status Evaluation** | Computes current attendance percentage per subject and flags the subject status as either `OK` or `LOW` against the minimum threshold ($75\%$). |
| **Safe-Skip Estimator** | Calculates the maximum number of upcoming classes that can be skipped consecutively without violating the minimum percentage target. |
| **Recovery Streak Calculator** | Computes the exact number of consecutive upcoming classes a student must attend to elevate their percentage back to the target threshold. |
| **Comprehensive Summary Dashboard** | Displays an aggregated, formatted overview of all subjects, attendances, rates, and contextual action items in a single view. |