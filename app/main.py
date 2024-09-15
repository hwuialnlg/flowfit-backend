from fastapi import FastAPI
from template_user.router import template_user_router
from template_user.createUser import create_user

app = FastAPI()

# HTTP Request Testing
# Open up the swagger/local server docs
# or use Insomnia/Postman

# include routers here

app.include_router(template_user_router)