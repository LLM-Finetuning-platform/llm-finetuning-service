from typing import Literal

from ray.data import Dataset
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
        dataset: Dataset,
        algorithm: BaseAlgorithm,
        peft_method: BasePEFT,
        model: Model,
    ):
        self.algorithm = algorithm
        self.peft_method = peft_method
        self.model = model
        self.dataset = dataset

    def _initialse_trainer(
        self,
        callback_fn: TrainerCallback,
        test_size: float,
        seed: int,
        split_type: Literal["hash", "random"],
        hash_column: str | None,
        **kwargs,
    ) -> Trainer:
        _train, _test = self.dataset.streaming_train_test_split(
            test_size=test_size,
            seed=seed,
            split_type=split_type,
            ray_remote_kwargs=kwargs,
            hash_column=hash_column,
        )
        trainer = self.algorithm.trainer(
            model=AutoModelForCausalLM.from_pretrained(self.model.model_id),
            args=self.algorithm.args,
        )
        trainer.add_callback(callback_fn)
        return prepare_trainer(trainer)

    def run(self):
        pass
