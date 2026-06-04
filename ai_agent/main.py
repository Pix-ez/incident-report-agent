from fastapi import FastAPI

from api.webhook import router


app = FastAPI(
    title="Incident Service"
)

app.include_router(router)


@app.get("/health")
def health():

    return {
        "status": "ok"
    }