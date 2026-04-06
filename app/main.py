from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.database import Base, engine
from app.models import requirement, review, signoff, user

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Friday SDLC Accelerator")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {"message": "AI Friday App is Running ✅"},
    )


@app.get("/health")
def health_check():
    return {"status": "OK"}
