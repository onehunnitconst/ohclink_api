from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.db.models import Link

def get_original_link(db: Session, pathname: str):
    link = db.query(Link).where(Link.pathname == pathname).first()

    if not link:
        raise HTTPException(status_code=404, detail="Link not found")

    return link.original_url
