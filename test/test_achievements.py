import pytest

from achievements import add_achievement, filter_by_student


def test_add_achievement_success():
    records = []
    record = add_achievement(
        records, "Иванов Александр", "Победа в олимпиаде", "Наука", True
    )
    assert len(records) == 1
    assert record["student"] == "Иванов Александр"
    assert record["is_confirmed"] is True


def test_add_achievement_validation_error():
    records = []
    with pytest.raises(ValueError):
        add_achievement(records, "", "Победа в олимпиаде", "Наука", True)


def test_filter_by_student():
    records = [
        {
            "id": 1,
            "student": "Иванов Александр",
            "title": "Статья",
            "category": "Наука",
            "is_confirmed": True,
        },
        {
            "id": 2,
            "student": "Петров Петр",
            "title": "Забег",
            "category": "Спорт",
            "is_confirmed": False,
        },
    ]
    results = filter_by_student(records, "Иванов Александр")
    assert len(results) == 1
    assert results[0]["title"] == "Статья"
