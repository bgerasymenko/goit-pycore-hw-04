# Функція для розбору команди користувача
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Команду приводимо до нижнього регістру
    return cmd, *args

# Додаємо новий контакт до словника
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Змінюємо номер телефону для існуючого контакту
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Показуємо номер телефону за іменем
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Виводимо всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

# Основна функція
def main():
    contacts = {}  # Порожній словник контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

# Запускаємо бот
if __name__ == "__main__":
    main()