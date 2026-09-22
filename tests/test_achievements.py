from models.students import Student


def test_student_creation():
    student = Student(1, "Иванов Александр", "ИВТ-101")
    assert student.id == 1
    assert student.name == "Иванов Александр"
    assert student.group == "ИВТ-101"


def test_student_serialization():
    student = Student(1, "Иванов Александр", "ИВТ-101")
    data = student.to_dict()
    assert data["name"] == "Иванов Александр"

    restored = Student.from_dict(data)
    assert restored.id == student.id
    assert restored.name == student.name
