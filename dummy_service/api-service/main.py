from fastapi import FastAPI
import httpx
import time
from utils.logging_config import setup_logger

logger = setup_logger("api-service")
app = FastAPI()



PAYMENT_URL = "http://payment-service:8001"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
async def checkout():

    # start = time.time()

    logger.info(
    "checkout_processing_started",
    extra={
        "service": "api-service",
        "event_type": "checkout_processing"
        }
    )

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYMENT_URL}/process-payment"
        )

    # duration = time.time() - start

    logger.error(
    "checkout_processing_failed",
    extra={
        "service": "api-service",
        "reason": "database_timeout",
        "severity": "critical"
        }
    )

    return response.json()  