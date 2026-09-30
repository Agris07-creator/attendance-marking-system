"""Mathematical logic for attendance calculations."""

from config import MIN_PERCENTAGE


def attendence_percentage(attended: int, total: int) -> float:
    """Return attendance percentage for given attended/total classes."""
    if total == 0:
        return 0.0
    return (attended / total) * 100.0


def classes_can_skip(attended: int, total: int, min_percentage: float = MIN_PERCENTAGE) -> int:
    """
    Calculate how many upcoming classes can be skipped
    while remaining at or above min_percentage.
    """
    skip = 0
    while True:
        new_total = total + skip + 1
        new_percentage = attendence_percentage(attended, new_total)
        if new_percentage < min_percentage:
            break
        skip += 1
    return skip


def classes_must_attend(attended: int, total: int, min_percentage: float = MIN_PERCENTAGE) -> int:
    """
    Calculate how many consecutive upcoming classes must be
    attended to reach min_percentage.
    """
    attend = 0
    while attendence_percentage(attended + attend, total + attend) < min_percentage:
        attend += 1
    return attend