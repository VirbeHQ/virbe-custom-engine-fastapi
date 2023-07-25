import enum

from pydantic import BaseSettings


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings powered by pydantic BaseSettings.

    These parameters can be configured
    with environment variables. You need to make sure
    that Uppercase is used for the variable names
    defined in the system.

    They can be also configured with a .env file.

    Additionally, they can be overriden via call to ConfigMS.
    """

    host: str = "0.0.0.0"  # noqa: S104
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "prod"

    log_level: LogLevel = LogLevel.INFO

    # this values can be overriden by .env file use UPPER_CASE for respective env variables
    virbe_dashbord_api_prefix: str = "https://your-dashboard-name.virbe.app"
    virbe_room_actions_api_key: str = "your-actions-api-key"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
