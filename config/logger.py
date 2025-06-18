import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",  # ou "json" se quiser JSON
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    },
}

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")
