import os

DATABASE_URL = "sqlite+aiosqlite:///./resumes.db"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
UPLOAD_FOLDER = "static/uploads"
