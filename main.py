from achievements import add_achievement, filter_by_student
from storage import load_achievements, save_achievements


def main():
    records = load_achievements()

    while True:
        print("\n--- Система учета достижений студентов ---")
        print("1. Посмотреть все достижения")
        print("2. Добавить новое достижение")
        print("3. Найти достижения студента")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            if not records:
                print("Список достижений пуст.")
            else:
                for r in records:
                    status = (
                        "Подтверждено"
                        if r["is_confirmed"]
                        else "На проверке"
                    )
                    print(
                        f"[{r['id']}] {r['student']} — {r['title']} "
                        f"({r['category']}) [{status}]"
                    )

        elif choice == "2":
            try:
                student = input("Введите имя студента: ")
                title = input("Введите название достижения: ")
                category = input(
                    "Введите категорию (Наука/Спорт/Культура): "
                )
                confirmed_input = (
                    input("Подтверждено? (да/нет): ").strip().lower()
                )
                is_confirmed = confirmed_input == "да"

                add_achievement(
                    records, student, title, category, is_confirmed
                )
                save_achievements(records)
                print("Достижение успешно добавлено!")
            except ValueError as err:
                print(f"Ошибка ввода: {err}")

        elif choice == "3":
            student_name = input("Введите имя студента для поиска: ")
            found = filter_by_student(records, student_name)
            if not found:
                print("Достижения не найдены.")
            else:
                for r in found:
                    print(f"- {r['title']} ({r['category']})")

        elif choice == "4":
            print("Завершение работы.")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()
