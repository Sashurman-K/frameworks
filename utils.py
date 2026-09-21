def validate_non_empty(value: str, field_name: str) -> str:
    """Проверяет, что введенное значение не пустое."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"Поле '{field_name}' не может быть пустым.")
    return cleaned