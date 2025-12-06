from sqlalchemy.orm import Session

from ohclink_api.db.models import Link

def get_original_link(db: Session, pathname: str):
    link = db.query(Link).where(Link.pathname == pathname).first()

    return link.original_url
