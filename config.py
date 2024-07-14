import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()

class ApplicationConfig:
  JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
  SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
    