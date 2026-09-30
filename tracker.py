"""UI operations for subject management and summary views."""

from config import MIN_PERCENTAGE
from calculator import attendence_percentage, classes_can_skip, classes_must_attend


def add_subject(subjects: list) -> None:
    name = input("Enter subject name: ").strip()
    total = int(input(f"Total classes held so far for {name}: "))
    attended = int(input(f"Classes attended for {name}: "))
    subjects.append({"subject": name, "attended": attended, "total": total})
    print(f"'{name}' added.\n")


def show_subject_list(subjects: list) -> None:
    for idx, s in enumerate(subjects, start=1):
        print(f"{idx} - {s['subject']}")


def mark_attendence(subjects: list) -> None:
    if not subjects:
        print("No subjects added yet.\n")
        return

    show_subject_list(subjects)
    idx = int(input("Enter subject number to mark today's attendance: ")) - 1
    if idx < 0 or idx >= len(subjects):
        print("Invalid subject number.\n")
        return

    status = input("Were you present today? (y/n): ").strip().lower()
    subjects[idx]["total"] += 1
    if status == "y":
        subjects[idx]["attended"] += 1
    print(f"Attendance updated for {subjects[idx]['subject']}.\n")


def show_summary(subjects: list) -> None:
    if not subjects:
        print("No subjects added yet.\n")
        return

    print()
    print(f"{'Subject':<15} {'Attended':<10} {'Total':<10} {'Percentage':<12} {'Status':<6}")
    print("-" * 55)

    for s in subjects:
        pct = round(attendence_percentage(s["attended"], s["total"]), 1)
        status = "OK" if pct >= MIN_PERCENTAGE else "LOW"

        print(f"{s['subject']:<15} {s['attended']:<10} {s['total']:<10} {pct:<12} {status:<6}")

        if pct >= MIN_PERCENTAGE:
            skip = classes_can_skip(s["attended"], s["total"])
            print(f"   -> Can safely skip {skip} more classes and stay above {MIN_PERCENTAGE}%.")
        else:
            attend = classes_must_attend(s["attended"], s["total"])
            print(f"   -> Must attend next {attend} classes in a row to reach {MIN_PERCENTAGE}%.")
    print()