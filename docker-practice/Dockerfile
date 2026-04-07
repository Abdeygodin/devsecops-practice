# Базовый образ
FROM python:3.11-alpine

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем код
COPY app.py .

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
