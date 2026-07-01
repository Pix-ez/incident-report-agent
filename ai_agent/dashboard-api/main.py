from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.incidents import router as incident_router
from api.investigations import router as investigation_router

app = FastAPI(
    title="Incident Dashboard API"
)


origins = [
    "http://localhost:5173",
    "http://dashboard-ui:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allows requests from specified origins
    allow_credentials=True,         # Allows cookies and credentials (like Bearer tokens)
    allow_methods=["*"],            # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Allows all request headers
)
app.include_router(
    incident_router
)

app.include_router(
    investigation_router)


@app.get("/health")
def health():

    return {
        "status": "ok"
    }