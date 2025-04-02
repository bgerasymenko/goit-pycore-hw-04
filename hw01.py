# Функція для обчислення загальної та середньої зарплати
def total_salary(path):
    try:
        # Відкриваємо файл
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            # Читаємо кожен рядок
            for line in file:
                # Розділяємо ім'я і зарплату
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

            average = total / count if count > 0 else 0
            return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return 0, 0


# Створюємо тестовий файл з даними про зарплати
with open('salary_file.txt', 'w', encoding='utf-8') as file:
    file.write("Alex Korp,3000\n")
    file.write("Nikita Borisenko,2000\n")
    file.write("Sitarama Raju,1000\n")

print("Файл salary_file.txt успішно створено!")

# Викликаємо функцію та виводимо результат
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
