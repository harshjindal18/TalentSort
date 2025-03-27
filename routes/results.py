from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import SessionLocal
from models import Resume

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/")
async def get_results(db: AsyncSession = Depends(get_db)):
    """Fetch all resume screening results."""
    result = await db.execute(select(Resume))
    resumes = result.scalars().all()
    return [{"id": r.id, "filename": r.filename, "skills": r.skills, "summary": r.summary} for r in resumes]
