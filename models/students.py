class Student:
    """Модель студента."""

    def __init__(self, student_id: int, name: str, group: str):
        self.id = student_id
        self.name = name
        self.group = group

    def to_dict(self) -> dict:
        """Преобразует объект в словарь."""
        return {
            "id": self.id,
            "name": self.name,
            "group": self.group,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """Создает объект Student из словаря."""
        return cls(
            student_id=data["id"],
            name=data["name"],
            group=data["group"],
        )

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} (Группа: {self.group})"
