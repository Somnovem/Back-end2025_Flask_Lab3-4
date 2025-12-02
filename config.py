import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", "postgresql://postgres:1234@localhost:5432/lab3-4_db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

API_TITLE = "Expense Tracker LAB3-4 API"
API_VERSION = "v3"
OPENAPI_VERSION = "3.0.3"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/docs"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"