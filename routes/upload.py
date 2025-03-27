from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal
from models import Resume
from ai_processor import process_resume
import shutil
import config

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/")
async def upload_resume(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    """Handles resume upload, processes it, and saves results in DB."""
    file_path = f"{config.UPLOAD_FOLDER}/{file.filename}"
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Read file content
    content = open(file_path, "r", encoding="utf-8").read()

    # Process resume with AI
    skills, summary = await process_resume(content)

    # Save to DB
    resume_entry = Resume(filename=file.filename, content=content, skills=skills, summary=summary)
    db.add(resume_entry)
    await db.commit()

    return {"message": "Resume processed successfully!", "skills": skills, "summary": summary}
