import os

from dotenv import dotenv_values, load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
ENVFILE = ".development.env"


class Config:
    def __init__(self):
        envfile_path = f"{BASEDIR}/{ENVFILE}"
        for key, value in dotenv_values(envfile_path).items():
            setattr(self, key, value)
        load_dotenv(envfile_path, override=True, verbose=True)


env = Config()
