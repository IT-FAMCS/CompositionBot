import uvicorn
from constants.tags import Tags
from dotenv import load_dotenv
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.params import Depends
from routers.user import user_router
from routers.admin import admin_router

app = FastAPI(debug=True)

origins = [
    # "http://localhost:8000",
    "http://localhost:3000",
]



def custom_openapi():
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get("paths").items():
            for _, param in method_item.items():
                responses = param.get("responses")
                if "422" in responses:
                    del responses["422"]
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(admin_router, tags=Tags.admin.value)
app.include_router(user_router, tags=Tags.user.value)


@app.get("/health_check", status_code=200)
def health_check():
    return "OK"



if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="127.0.0.1", port=8000)