import uuid

from fastapi import FastAPI
import httpx
import time
from utils.logging_config import setup_logger
from utils.event_repository import create_event
from prometheus_client import make_asgi_app

logger = setup_logger("api-service")
app = FastAPI()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


PAYMENT_URL = "http://payment-service:8001"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
async def checkout():

    # start = time.time()
    logger.info(
        "checkout_processing",
        extra={
            "service": "api-service",
            "severity": "info"
        }
    )
    create_event(
        service_name="api-service",
        event_type="checkout_processing",
        severity="info",
        message="checkout processing"
    )

    request_id = str(uuid.uuid4())

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYMENT_URL}/process-payment",
            headers = {
                "X-Request-ID": request_id
            }
        )

    # duration = time.time() - start
    logger.info(
        "checkout_completed",
        extra={
            "service": "api-service",
            "severity": "info"
        }
    )

    if response.status_code != 200:
        logger.error(
            "checkout_failed",
            extra={
                "service": "api-service",
                "reason": "payment_service_failure",
                "severity": "critical"
            }
        )

        create_event(
            service_name="api-service",
            event_type="checkout-failure",
            severity="critical",
            message="payment service timeout",
            event_metadata={
                "failure_mode":True
            }
        )

    return response.json()  