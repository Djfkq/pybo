import os
from config.default import BASE_DIR

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'pybo.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe5\x96\xc3;\xcau\n\xc9$\xda\x99`\xa9\xe9\xdc\xe2'

