# Укажите базовый образ
FROM python:3.10

# Установите необходимые зависимости
RUN pip install -r requirements.txt

# Скопируйте файлы проекта в контейнер
COPY . /
WORKDIR /

# Укажите переменные окружения
ENV BOT_TOKEN=597743VykYUuQXfMPxwsqXY

# Запустите команду для запуска бота
CMD ["python", "main.py"]
