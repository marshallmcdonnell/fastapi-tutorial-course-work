import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "0.0.1"

    SQLITE_DB: str = os.getenv("SQLITE_DB", "test.db")
    DATABASE_URL: str = f"sqlite:///./{SQLITE_DB}"


settings = Settings()
