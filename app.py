from fastapi import FastAPI

from src.domains.links import links_router

app = FastAPI()

app.include_router(links_router.router)