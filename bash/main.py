
import subprocess

print("Запускаємо Bash-скрипт...")

result = subprocess.run(
    ["bash", "hello.sh"],
    capture_output=True,
    text=True,
    check=True
)

print(result.stdout)
print("Скрипт завершив роботу.")
