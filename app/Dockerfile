FROM python:3.12

WORKDIR /

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN useradd -m app
USER app

# CMD ["fastapi", "dev", "main.py"]

EXPOSE 8080

# Command to run the FastAPI server using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
