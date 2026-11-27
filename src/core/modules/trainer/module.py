from ray.train import get_dataset_shard
from ray.train.huggingface.transformers import prepare_trainer
from transformers import AutoModelForCausalLM
from transformers.trainer import Trainer
from transformers.trainer_callback import TrainerCallback

from src.core.modules.trainer.algos.base import BaseAlgorithm
from src.core.modules.trainer.models.base import Model
from src.core.modules.trainer.peft.base import BasePEFT


class TrainerModule:
    def __init__(
        self,
        algorithm: BaseAlgorithm,
        peft_method: BasePEFT,
        model: Model,
        callback_fn: TrainerCallback,
        **kwargs,
    ):
        self.algorithm = algorithm
        self.peft_method = peft_method
        self.model = model
        self.trainer: Trainer = self._initialse_trainer(
            callback_fn=callback_fn, **kwargs
        )

    def _initialse_trainer(
        self,
        callback: TrainerCallback,
        **kwargs,
    ) -> Trainer:
        trainer = self.algorithm.trainer(
            model=AutoModelForCausalLM.from_pretrained(self.model.model_id),
            args=self.algorithm.args,
            train_dataset=get_dataset_shard("train"),
            eval_dataset=get_dataset_shard("val"),
        )
        trainer.add_callback(callback=callback)
        return prepare_trainer(trainer)

    @property
    def trainer(self):
        return self.trainer
