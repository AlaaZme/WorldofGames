FROM python:3.7

WORKDIR /app
COPY ./ ./

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "./load_game.py"]