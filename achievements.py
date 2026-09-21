from typing import Any, Dict, List


def add_achievement(
    records: List[Dict[str, Any]],
    student: str,
    title: str,
    category: str,
    is_confirmed: bool,
) -> Dict[str, Any]:
    if not student.strip() or not title.strip():
        raise ValueError(
            "Имя студента и название достижения не могут быть пустыми."
        )

    new_record = {
        "id": len(records) + 1,
        "student": student,
        "title": title,
        "category": category,
        "is_confirmed": is_confirmed,
    }
    records.append(new_record)
    return new_record


def filter_by_student(
    records: List[Dict[str, Any]], student_name: str
) -> List[Dict[str, Any]]:
    return [r for r in records if r["student"].lower() == student_name.lower()]
