
def create_achievement(student_name: str, title: str, category: str) -> str:
    return f"Студент: {student_name} | Достижение: '{title}' | Категория: {category}"


def verify_achievement(points: int, has_document: bool) -> str:
    if points > 0 and has_document:
        return "Подтверждено"
    elif points > 0 and not has_document:
        return "Ожидает загрузки подтверждающего документа"
    else:
        return "Отклонено (неверное количество баллов)"


def generate_report(student_name: str, achievement_info: str, status: str) -> str:
    return f"=== Отчет о достижениях ===\n{achievement_info}\nСтатус: {status}"


def main():
    # Начальный тестовый сценарий
    student = "Иванов Иван"
    title = "1 место в хакатоне по Python"
    category = "Наука и образование"
    points = 50
    has_doc = True

    achievement_info = create_achievement(student, title, category)
    status = verify_achievement(points, has_doc)
    report = generate_report(student, achievement_info, status)

    print(report)


if __name__ == "__main__":
    main()