import os
import subprocess
import sys
from pathlib import Path

# 1. Створюємо віртуальне оточення
def create_venv():
    venv_dir = Path("venv")
    if not venv_dir.exists():
        print("📦 Створюю віртуальне оточення...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    else:
        print("✅ Віртуальне оточення вже існує.")

# 2. Встановлюємо colorama
def install_colorama():
    print("📥 Встановлюю colorama...")
    # Використовуємо pip з віртуального оточення
    pip_path = Path("venv") / "Scripts" / "pip.exe" if os.name == 'nt' else Path("venv") / "bin" / "pip"
    subprocess.run([str(pip_path), "install", "colorama"])

# 3. Створюємо тестову файлову структуру
def create_test_files():
    base = Path("picture")
    logo = base / "Logo"
    files = [
        base / "bot-icon.png",
        base / "mongodb.jpg",
        logo / "IBM+Logo.png",
        logo / "ibm.svg",
        logo / "logo-tm.png",
    ]
    for f in files:
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(f"Файл: {f.name}", encoding="utf-8")
    print("📁 Тестова структура створена!")

# 4. Виводимо структуру з кольорами
def display_tree(path: Path, prefix=""):
    from colorama import Fore, init
    init(autoreset=True)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"❌ Шлях не існує або це не директорія: {path}")
        return

    entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    total = len(entries)

    for i, entry in enumerate(entries):
        connector = "┗━ " if i == total - 1 else "┣━ "
        new_prefix = "   " if i == total - 1 else "┃  "
        if entry.is_dir():
            print(prefix + Fore.BLUE + connector + entry.name)
            display_tree(entry, prefix + new_prefix)
        else:
            print(prefix + Fore.GREEN + connector + entry.name)

# Головна функція
def main():
    create_venv()
    install_colorama()
    create_test_files()
    print("\n🎨 Виводжу структуру директорії 'picture':\n")
    display_tree(Path("picture"))

if __name__ == "__main__":
    main()
