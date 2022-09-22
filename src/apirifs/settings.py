from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    security_admin_password: SecretStr

    class Config:
        env_prefix = 'GF_'
        env_file = '.env'
        env_file_encoding = 'utf-8'
