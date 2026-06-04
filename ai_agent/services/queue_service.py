import json

import redis

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True,
    health_check_interval=30,
    socket_timeout=None,
    socket_connect_timeout=30
)

def enqueue_incident(
    incident_id: str
):

    payload = {
        "incident_id": incident_id
    }

    redis_client.lpush(
        "incident-investigation-queue",
        json.dumps(payload)
    )