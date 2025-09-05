from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, auth
import os

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
BASE_DIR = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "users": users
    })

@app.post("/register")
def register(username: str = Form(...), email: str = Form(...), password: str = Form(...),
             db: Session = Depends(database.get_db)):
    user_in_db = crud.get_user_by_username(db, username)
    if user_in_db:
        return HTMLResponse(f"Username '{username}' already exists")
    user = schemas.UserCreate(username=username, email=email, password=password)
    crud.create_user(db, user)
    return RedirectResponse(url=f"/profile/{username}", status_code=303)

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, username, password)
    if not user:
        return HTMLResponse("Invalid credentials")
    return RedirectResponse(url=f"/profile/{username}", status_code=303)

@app.get("/profile/{username}", response_class=HTMLResponse)
def profile(request: Request, username: str, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_username(db, username)
    if not user:
        return HTMLResponse("User not found", status_code=404)
    return templates.TemplateResponse("profile.html", {"request": request, "username": user.username, "email": user.email})
