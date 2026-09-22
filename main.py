import os

from models import Achievement, Confirmation, Student
from storage import load_data, save_data
from utils import validate_non_empty

STUDENTS_FILE = os.path.join("data", "students.json")
ACHIEVEMENTS_FILE = os.path.join("data", "achievements.json")
CONFIRMATIONS_FILE = os.path.join("data", "confirmations.json")


def main():
    students = load_data(STUDENTS_FILE, Student)
    achievements = load_data(ACHIEVEMENTS_FILE, Achievement)
    confirmations = load_data(CONFIRMATIONS_FILE, Confirmation)

    while True:
        print("\n=== СИСТЕМА УЧЕТА ДОСТИЖЕНИЙ СТУДЕНТОВ ===")
        print("1. Посмотреть всех студентов")
        print("2. Добавить студента")
        print("3. Добавить достижение")
        print("4. Посмотреть достижения студента")
        print("5. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            if not students:
                print("Список студентов пуст.")
            for s in students:
                print(s)

        elif choice == "2":
            try:
                name = validate_non_empty(
                    input("Имя студента: "), "Имя"
                )
                group = validate_non_empty(
                    input("Группа: "), "Группа"
                )
                new_id = len(students) + 1
                student = Student(new_id, name, group)
                students.append(student)
                save_data(STUDENTS_FILE, students)
                print("Студент успешно добавлен!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            if not students:
                print("Сначала добавьте хотя бы одного студента!")
                continue
            try:
                s_id = int(input("Введите ID студента: "))
                if not any(s.id == s_id for s in students):
                    print("Студент с таким ID не найден.")
                    continue
                title = validate_non_empty(
                    input("Название достижения: "), "Название"
                )
                category = validate_non_empty(
                    input("Категория (Наука/Спорт): "), "Категория"
                )

                a_id = len(achievements) + 1
                achievement = Achievement(a_id, s_id, title, category)
                achievements.append(achievement)
                save_data(ACHIEVEMENTS_FILE, achievements)

                # Добавляем подтверждение
                c_id = len(confirmations) + 1
                confirmation = Confirmation(
                    c_id, a_id, status="Подтверждено", points=10
                )
                confirmations.append(confirmation)
                save_data(CONFIRMATIONS_FILE, confirmations)

                print("Достижение добавлено!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            try:
                s_id = int(input("Введите ID студента: "))
                user_achievements = [
                    a for a in achievements if a.student_id == s_id
                ]
                if not user_achievements:
                    print("У этого студента нет достижений.")
                for a in user_achievements:
                    conf = next(
                        (
                            c
                            for c in confirmations
                            if c.achievement_id == a.id
                        ),
                        None,
                    )
                    print(f"{a} | {conf if conf else 'Без статуса'}")
            except ValueError:
                print("Некорректный ID.")

        elif choice == "5":
            print("Завершение работы.")
            break


if __name__ == "__main__":
    main()
