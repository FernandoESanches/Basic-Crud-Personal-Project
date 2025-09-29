import os

class DbConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_ENV = os.getenv("APP_ENV", "local")

    if APP_ENV == "docker":
        with open("/run/secrets/docker_db_uri.txt") as file:
            SQLALCHEMY_DATABASE_URI = file.read().strip()
    else:
        with open("./secrets/local_db_uri.txt") as file:
            SQLALCHEMY_DATABASE_URI = file.read().strip()

