from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from src.db.database import get_session
from src.domains.links import links_service

router = APIRouter()

@router.get('/{pathname}')
def get_my_profile(
    pathname: str,
    db: Session = Depends(get_session),
):
    original_url = links_service.get_original_link(db, pathname)
    return RedirectResponse(url=original_url)