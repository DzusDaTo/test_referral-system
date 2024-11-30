# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем все файлы в контейнер
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Django
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
