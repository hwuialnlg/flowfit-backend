from fastapi import FastAPI
from app.template_user.router import template_user_router
from app.template_user.createUser import create_user

app = FastAPI()

# Start FastAPI server
# Open cmd terminal in VSC
# cd Scripts
# .\activate
# fastapi dev main.py

# HTTP Request Testing
# Open up the swagger/local server docs

# include routers here

app.include_router(template_user_router)