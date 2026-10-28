from transformers.trainer import Trainer

from src.core.modules.trainer.algos.base import BaseAlgorithm
from src.core.modules.trainer.models.base import Model
from src.core.modules.trainer.peft.base import BasePEFT


class TrainerModule:
    def __init__(self, algorithm: BaseAlgorithm, peft_method: BasePEFT, model: Model):
        self.algorithm = algorithm
        self.peft_method = peft_method
        self.model = model

    def _initialse_trainer(self) -> Trainer:
        return Trainer()
