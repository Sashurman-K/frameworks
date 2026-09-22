import json
import os
from typing import Any, List, Type, TypeVar

T = TypeVar("T")


def load_data(filepath: str, model_cls: Type[T]) -> List[T]:
    """Загружает список объектов из JSON-файла."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            return [model_cls.from_dict(item) for item in raw_data]
    except (json.JSONDecodeError, OSError, KeyError):
        return []


def save_data(filepath: str, items: List[Any]) -> None:
    """Сохраняет список объектов в JSON-файл."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(
            [item.to_dict() for item in items],
            f,
            ensure_ascii=False,
            indent=4,
        )
