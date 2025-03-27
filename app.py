from fastapi import FastAPI
from routes import upload, results
from database import init_db

app = FastAPI(title="AI Resume Screener")

# Include API routes
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(results.router, prefix="/results", tags=["Results"])

# Initialize database
@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def home():
    return {"message": "Welcome to AI Resume Screener!"}
