# from pydantic import BaseModel
# from typing import Dict, List, Any


# class AlertmanagerWebhook(BaseModel):
#     version: str
#     status: str
#     receiver: str
#     groupLabels: Dict[str, str]
#     commonLabels: Dict[str, str]
#     commonAnnotations: Dict[str, str]
#     alerts: List[Dict[str, Any]]
#     externalURL: str


from pydantic import BaseModel


class Alert(BaseModel):

    status: str
    labels: dict
    annotations: dict


class AlertManagerPayload(BaseModel):

    receiver: str
    status: str
    alerts: list[Alert]