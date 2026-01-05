# python
import os
import yaml
from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    CONFIG_DIR = BASE_DIR / 'config'
    REPORTS_DIR = BASE_DIR / 'reports'
    LOGS_DIR = BASE_DIR / 'logs'
    DATA_DIR = BASE_DIR / 'data'

    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'

    # Timeout settings
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30

    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True

    # Environment
    ENV = os.getenv('ENV', 'dev')

    @classmethod
    def load_environment_config(cls):
        """Load environment-specific configuration"""
        env_file = cls.CONFIG_DIR / 'environments' / f'{cls.ENV}.yaml'
        if env_file.exists():
            with env_file.open('r') as f:
                return yaml.safe_load(f) or {}
        return {}

    @classmethod
    def get_base_url(cls):
        env_config = cls.load_environment_config()
        return env_config.get('base_url', 'https://vineetkr.com')

    @classmethod
    def get_api_base_url(cls):
        env_config = cls.load_environment_config()
        return env_config.get('api_base_url', "https://api.vineetkr.com")
