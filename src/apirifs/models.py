from pydantic import BaseModel, Field, ValidationError, validator, Extra

class Run(BaseModel):
    """Run Model"""

    run_id: str
    start_time: str
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
    step: int
    pred_str: str
    target_str: str
