

#start normal app

from fastapi import Depends, FastAPI, Request
import time
import uuid
from utils.logging_config import setup_logger
from db.database import SessionLocal
from db.models import Transaction
from sqlalchemy.orm import Session
from utils.metrics import REQUEST_COUNT, REQUEST_LATENCY, PAYMENT_FAILURES
from prometheus_client import make_asgi_app
from utils.event_repository import create_event

logger = setup_logger("payment-service")
app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

FAILURE_MODE = False
LATENCY_MODE = False

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process-payment")
async def process_payment(request: Request, db: Session = Depends(get_db)):

    request_id = request.headers.get("X-Request-ID")
    create_event(
        service_name="payment-service",
        event_type="payment_processing",
        severity="info",
        message="payment processing"
    )

    logger.info(
        "payment_processing",
        extra={
            "request_id": request_id,
            "service": "payment-service",
            "severity": "info"
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
                transaction_id=str(uuid.uuid4()),
                status="failed",
                amount=100
            )

            db.add(txn)
            db.commit()
            db.refresh(txn)
            PAYMENT_FAILURES.inc()

            logger.error(
                "payment_failed",
                extra={
                    "service": "payment-service",
                    "reason": "database_timeout",
                    "severity": "critical"
                }
            )

            create_event(
                service_name="payment-service",
                event_type="payment-failure",
                severity="critical",
                message="database timeout",
                event_metadata={
                    "request_id": request_id,
                    "transaction_id": txn.id,
                    "failure_mode":True
                }
            )
            return {
                "status": "failed",
                "reason": "database timeout"
            }

        txn = Transaction(
            transaction_id=str(uuid.uuid4()),
            status="success",
            amount=100
        )

        db.add(txn)
        db.commit()
        db.refresh(txn)

        create_event(
            service_name="payment-service",
            event_type="payment_success",
            severity="info",
            message="payment processed",
        )
        logger.info(
            "payment_completed",
            extra={
                "request_id": request_id,
                "service": "payment-service",
                "severity": "info"
            }
        )
        return {
            "status": "success",
            "transaction_id": txn.transaction_id
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
