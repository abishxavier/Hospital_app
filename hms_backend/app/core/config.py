import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    app_name = os.getenv("APP_NAME", "Hospital Management API")
    database_url = os.getenv("DATABASE_URL", "sqlite:///./hms.db")
    secret_key = os.getenv("SECRET_KEY", "dev-secret-key")


settings = Settings()
