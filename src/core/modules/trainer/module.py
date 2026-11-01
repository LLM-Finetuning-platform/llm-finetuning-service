from ray.data import Dataset
from transformers import AutoModelForCausalLM
from transformers.trainer import Trainer
from transformers.trainer_callback import TrainerCallback
from transformers.training_args import TrainingArguments

from src.core.modules.trainer.algos.base import BaseAlgorithm
from src.core.modules.trainer.models.base import Model
from src.core.modules.trainer.models.models import Models
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
        self, callback_fn: TrainerCallback, args: TrainingArguments, models: Models
    ) -> Trainer:
        model = AutoModelForCausalLM.from_pretrained(self.model.model_id)  # type: ignore
        trainer = self.algorithm.trainer(model=model, args=args)
        trainer.add_callback(callback_fn)
        return trainer
