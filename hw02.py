# Функція для читання даних про котів з файлу
def get_cats_info(path):
    try:
        cats = []  # Список для зберігання словників з інформацією про котів

        # Відкриваємо файл у режимі читання
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо кожен рядок з файлу
            for line in file:
                # Видаляємо символ нового рядка та розділяємо дані по комі
                parts = line.strip().split(',')

                # Перевіряємо, чи в рядку є рівно 3 частини
                if len(parts) == 3:
                    cat_id, name, age = parts

                    # Створюємо словник з інформацією про кота
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }

                    # Додаємо словник до списку
                    cats.append(cat_dict)

        return cats  # Повертаємо список словників

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []



# Створюємо тестовий файл з інформацією про котиків
with open('cats_file.txt', 'w', encoding='utf-8') as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    file.write("60b90c2413067a15887e1ae2,Vika,1\n")
    file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    file.write("60b90c4613067a15887e1ae5,Tessi,5\n")

print("Файл cats_file.txt успішно створено!")

# Викликаємо функцію та виводимо результат
cats_info = get_cats_info("cats_file.txt")
print("Список котиків:")
print(cats_info)
