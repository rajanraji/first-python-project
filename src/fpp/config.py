from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import Optional

class Settings(BaseSettings):
    # directories
    data_base: Path = Path("./data")
    raw_dir: Path = Path("./data/raw")
    processed_dir: Path = Path("./data/processed")
    reports_dir: Path = Path("./reports")

    # example for later: API keys (optional)
    openai_api_key: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    def ensure_dirs(self) -> None:
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)
