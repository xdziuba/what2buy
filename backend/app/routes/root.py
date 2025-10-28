from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root_page():
    return {"message": "What2Buy API is running 🚀"}