from fastapi import FastAPI
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.openapi.docs import (
#     get_redoc_html,
#     get_swagger_ui_html,
#     get_swagger_ui_oauth2_redirect_html,
# )

from .database import engine, Base
from . import routes
from .authenticator import AuthenticationError, authenticator, user_dep



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.main_router)

app.include_router(
    routes.admin_router, prefix="/admin", dependencies=[Depends(user_dep)]
)

app.include_router(
    routes.machine_router, prefix="/machine"
)

app.include_router(
    routes.machine_admin_router, prefix="/machine"
)

app.include_router(
    routes.job_router, prefix="/job"
)

app.include_router(
    routes.jobCategory_router, prefix="/jobCategory"
)

app.include_router(
    routes.checkpointMethod_router, prefix="/checkpointMethod"
)

app.include_router(
    routes.record_router, prefix="/record"
)

app.include_router(
    routes.subdivisionA_router, prefix="/subdivisionA"
)

app.include_router(
    routes.subdivisionB_router, prefix="/subdivisionB"
)

app.include_router(
    routes.subdivisionC_router, prefix="/subdivisionC"
)

app.include_router(
    routes.subdivisionSpecial_router, prefix="/subdivisionSpecial"
)

# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     openapi_url = app.openapi_url if app.openapi_url is not None else "/openapi.json"
#     return get_swagger_ui_html(
#         openapi_url=openapi_url,
#         title=app.title + " - Swagger UI",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_js_url="/static/swagger-ui-bundle.js",
#         swagger_css_url="/static/swagger-ui.css",
#     )


# @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
# async def swagger_ui_redirect():
#     return get_swagger_ui_oauth2_redirect_html()


# @app.get("/redoc", include_in_schema=False)
# async def redoc_html():
#     openapi_url = app.openapi_url if app.openapi_url is not None else "/openapi.json"
#     return get_redoc_html(
#         openapi_url=openapi_url,
#         title=app.title + " - ReDoc",
#         redoc_js_url="/static/redoc.standalone.js",
#     )