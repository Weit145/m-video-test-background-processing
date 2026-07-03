from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    file_path: str = Field(
        "data.text",
        validation_alias="FILE_PATH",
    )
    url: str = Field(
        "http://localhost:8000/api/data",
        validation_alias="URL",
    )
    timer: int = Field(
        1000,
        ge=1,
        validation_alias="TIMER",
    )
    log_level: str = Field(
        "INFO",
        validation_alias="LOG_LEVEL",
    )


settings = Settings()
