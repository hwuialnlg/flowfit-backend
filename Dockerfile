FROM python:3.12

COPY /app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

# not sure what this quite does
RUN useradd app
USER app

# add exposure to ports when necessary
# EXPOSE PORT

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# build image into docker desktop
# docker build -t fastapi-app .
# docker run -d -p 8080:8080 fastapi-app