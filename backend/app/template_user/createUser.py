from .router import template_user_router as router
from .response_models import TemplateUser

@router.post("/createUser")
async def create_user(user: TemplateUser) -> TemplateUser:
    return user