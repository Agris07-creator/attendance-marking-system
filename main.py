"""Main entry point. Coordinates config, calculator, and tracker modules."""

import config
import calculator
import tracker

MENU = f"""
===== Attendance Tracker (Min: {config.MIN_PERCENTAGE}%) =====
1. Add subject
2. Mark today's attendance
3. View summary (all subjects)
4. Exit
===============================================
"""


def main():
    subjects = []

    while True:
        print(MENU)
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            tracker.add_subject(subjects)
        elif choice == "2":
            tracker.mark_attendence(subjects)
        elif choice == "3":
            tracker.show_summary(subjects)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()