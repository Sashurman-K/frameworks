class Achievement:
    """Модель достижения."""

    def __init__(
        self,
        achievement_id: int,
        student_id: int,
        title: str,
        category: str,
    ):
        self.id = achievement_id
        self.student_id = student_id
        self.title = title
        self.category = category

    def to_dict(self) -> dict:
        """Преобразует объект в словарь."""
        return {
            "id": self.id,
            "student_id": self.student_id,
            "title": self.title,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Achievement":
        """Создает объект Achievement из словаря."""
        return cls(
            achievement_id=data["id"],
            student_id=data["student_id"],
            title=data["title"],
            category=data["category"],
        )

    def __str__(self) -> str:
        return f"[{self.id}] '{self.title}' (Категория: {self.category})"
