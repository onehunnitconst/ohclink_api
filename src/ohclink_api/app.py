from fastapi import FastAPI

from ohclink_api.domains.links import links_router

app = FastAPI()

app.include_router(links_router.router)