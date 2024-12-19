Backend for Flowfit: JWT auth logins, weekly schedules, tracking of exercises (such as dates + weights)

Virtual environment --> install postgresql
New packages, make a new requirements.txt before commit (pip freeze > requirements.txt)

template env, fill out according to dbs
docker compose up
TYPE= ("" OR DOCKER)
DB_NAME=postgres (whatever you named your db)
DB_TYPE=postgresql
DB_DRIVER=psycopg2
DB_PORT=5432
DB_SERVER=localhost
DB_USER=
DB_PASSWORD=
DOCKER_LINK=flowfit-postgres
SECRET_KEY=
ALGORITHM=
