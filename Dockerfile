FROM python:latest

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "modelAPI.py"]