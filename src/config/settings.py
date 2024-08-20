from pydantic import Field
from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    user: str = Field("postgres", env="POSTGRES_USER")
    password: str = Field("postgres", env="POSTGRES_PASS")
    database: str = Field("postgres", env="POSTGRES_DB")
    host: str = Field("localhost", env="POSTGRES_HOST")
    port: int = Field(5433, env="POSTGRES_PORT")

    @property
    def uri(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class AppSettings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    title: str = "Alter Jira"
    version: str = "1.0.1"


settings = AppSettings()
