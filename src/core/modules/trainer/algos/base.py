from pydantic import BaseModel
from transformers.trainer import Trainer
from transformers.training_args import TrainingArguments

from src.utils.enums.algos import Algorithms


class BaseAlgorithm(BaseModel):
    trainer: type[Trainer]
    algorithm: Algorithms
    args: TrainingArguments
