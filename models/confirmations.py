class Confirmation:
    """Модель подтверждения достижения."""

    def __init__(
        self,
        confirmation_id: int,
        achievement_id: int,
        status: str,
        points: int,
    ):
        self.id = confirmation_id
        self.achievement_id = achievement_id
        self.status = status  # 'Подтверждено', 'На проверке', 'Отклонено'
        self.points = points

    def to_dict(self) -> dict:
        """Преобразует объект в словарь."""
        return {
            "id": self.id,
            "achievement_id": self.achievement_id,
            "status": self.status,
            "points": self.points,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Confirmation":
        """Создает объект Confirmation из словаря."""
        return cls(
            confirmation_id=data["id"],
            achievement_id=data["achievement_id"],
            status=data["status"],
            points=data["points"],
        )

    def __str__(self) -> str:
        return f"Статус: {self.status} | Баллы: {self.points}"
