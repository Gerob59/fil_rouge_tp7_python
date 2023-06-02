from pydantic import BaseSettings


class Settings(BaseSettings):
    '''
        cette class contient les informations de connexion a la bdd :
            database_hostname : str
            database_port : str
            database_password : str
            database_name : str
            database_username : str
            secret_key : str
            algorithm : str
            access_token_expire_minutes : int

        les informations sont enregistrés dans le fichier de configuration ".env"
    '''
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
