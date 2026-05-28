

#start normal app
from fastapi import FastAPI
import random
import time
from utils.logging_config import setup_logger
from db.database import SessionLocal
from db.models import Transaction
from utils.metrics import REQUEST_COUNT, REQUEST_LATENCY, PAYMENT_FAILURES
from prometheus_client import make_asgi_app

db = SessionLocal()

logger = setup_logger("payment-service")
app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

FAILURE_MODE = False
LATENCY_MODE = False

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process-payment")
async def process_payment():

    logger.info(
    "payment_processing_started",
    extra={
        "service": "payment-service",
        "event_type": "payment_processing"
        }
    )

    REQUEST_COUNT.labels(
        service="payment-service",
        endpoint="/process-payment"
        ).inc()

    with REQUEST_LATENCY.labels(
    service="payment-service",
    endpoint="/process-payment"
    ).time():

        # processing logic
        if LATENCY_MODE:
            time.sleep(5)

        if FAILURE_MODE:
            txn = Transaction(
            status="failed",
            amount=100
            )

            db.add(txn)
            db.commit()

            logger.error(
                    "payment_processing_failed",
                    extra={
                        "service": "payment-service",
                        "reason": "database_timeout",
                        "severity": "critical"
                        }
                    )
            return {
                "status": "failed",
                "reason": "database timeout"
            }

        txn = Transaction(
        status="success",
        amount=100
        )

        db.add(txn)
        db.commit()
        return {
            "status": "success",
            "transaction_id": random.randint(1000, 9999)
        }

@app.post("/simulate/failure")
def simulate_failure():
    global FAILURE_MODE
    FAILURE_MODE = True
    return {"failure_mode": True}

@app.post("/simulate/recover")
def recover():
    global FAILURE_MODE
    FAILURE_MODE = False
    return {"failure_mode": False}

@app.post("/simulate/latency")
def simulate_latency():
    global LATENCY_MODE
    LATENCY_MODE = True
    return {"latency_mode": True}