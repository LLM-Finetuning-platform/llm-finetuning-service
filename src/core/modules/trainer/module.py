from typing import Literal

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
    ):
        self.algorithm = algorithm
        self.peft_method = peft_method
        self.model = model

    def _initialse_trainer(
        self,
        callback_fn: TrainerCallback,
        test_size: float,
        seed: int,
        split_type: Literal["hash", "random"],
        hash_column: str | None,
        **kwargs,
    ) -> Trainer:
        trainer = self.algorithm.trainer(
            model=AutoModelForCausalLM.from_pretrained(self.model.model_id),
            args=self.algorithm.args,
            train_dataset=get_dataset_shard("train"),
            eval_dataset=get_dataset_shard("val"),
        )
        trainer.add_callback(callback_fn)
        return prepare_trainer(trainer)
