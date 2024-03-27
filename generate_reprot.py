import subprocess

def run_tests():
    try:
        subprocess.run(['pytest', '-vv', '--html=report.html', 'summ.py'])
    except Exception as e:
        print(f"Ошибка при запуске тестов: {e}")

if __name__ == "__main__":
    run_tests()
