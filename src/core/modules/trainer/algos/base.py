from pydantic import BaseModel
from transformers.trainer import Trainer

from src.utils.enums.algos import Algorithms


class BaseAlgorithm(BaseModel):
    trainer: Trainer
    algorithm: Algorithms
