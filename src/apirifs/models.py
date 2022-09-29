from pydantic import BaseModel, Field, ValidationError, validator, Extra

from datetime import datetime

class Run(BaseModel):
    """Run Model"""
    run_id: str
    start_time: datetime
    model: str
    lr: float
    batch_size: int

class Metric(BaseModel):
    """Metric Model"""
    run_id: str
    epoch: int
    loss: float
    eval_loss: float
    eval_wer: float
    learning_rate: float

