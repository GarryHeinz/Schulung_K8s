import os
from dataclasses import dataclass


@dataclass
class Config:
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8080"))
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "development-secret-key")
