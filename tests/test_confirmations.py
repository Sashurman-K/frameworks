from models.confirmations import Confirmation


def test_confirmation_creation():
    conf = Confirmation(1, 10, "Подтверждено", 50)
    assert conf.id == 1
    assert conf.status == "Подтверждено"
    assert conf.points == 50
