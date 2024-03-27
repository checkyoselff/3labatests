import subprocess

def create_requirements_file(file_path="requirements.txt"):
    subprocess.run(["pip", "freeze"], stdout=open(file_path, "w"))

def install_requirements(file_path="requirements.txt"):
    subprocess.run(["pip", "install", "-r", file_path])

if __name__ == "__main__":
    # Создание файла requirements.txt
    create_requirements_file()

    # Установка модулей из requirements.txt
    install_requirements()

    # Запуск тестов и генерация отчета
