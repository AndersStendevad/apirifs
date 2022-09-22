from pydantic import BaseModel, Field, ValidationError, validator, Extra

from datetime import datetime

class Run(BaseModel):
    """Run Model"""
    run_id: str

    class Config:
        """Example for FastAPI"""
        schema_extra = {"example": {"run_id": "e75780f0-3a7b-11ed-a261-0242ac120002"}}


class Metric(BaseModel):
    """Metric Model"""
    run_id: str
    epoch: int
    loss: float
    eval_loss: float
    eval_wer: float
    learning_rate: float

    class Config:
        """Example for FastAPI"""
        schema_extra = {"example": {"run_id":'07dc5c6e-973e-482d-aada-9b19f5055e2a', "epoch":1, "loss":30.3637, "eval_loss":40.32535171508789, "eval_wer":1.0, "learning_rate": 0.0003}}

