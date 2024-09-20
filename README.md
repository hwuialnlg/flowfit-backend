template env

# LEAVE EMPTY IF USING VENV
TYPE=
# specify db type + driver used to establish conn to db
DB_NAME=postgres
DB_TYPE=postgres
DB_DRIVER=psycopg2
# modify based on host and port of db conn
DB_PORT=5432
DB_SERVER=localhost

# modify based on your user 
DB_USER=
DB_PASSWORD=

# no need to modify
DOCKER_LINK=flowfit-postgres
