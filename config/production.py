import os
from config.default import BASE_DIR
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'pybo.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe5\x96\xc3;\xcau\n\xc9$\xda\x99`\xa9\xe9\xdc\xe2'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

