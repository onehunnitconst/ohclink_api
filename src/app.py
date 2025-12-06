from fastapi import FastAPI

from domains.links import links_router

app = FastAPI()

app.include_router(links_router.router)