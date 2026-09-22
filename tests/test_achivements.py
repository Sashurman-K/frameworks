from models.achievements import Achievement


def test_achievement_creation():
    ach = Achievement(1, 101, "Победа в хакатоне", "Наука")
    assert ach.id == 1
    assert ach.student_id == 101
    assert ach.title == "Победа в хакатоне"


def test_achievement_to_dict():
    ach = Achievement(1, 101, "Победа в хакатоне", "Наука")
    d = ach.to_dict()
    assert d["student_id"] == 101
    assert d["category"] == "Наука"
