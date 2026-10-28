from src.core.modules.trainer.models.base import Model


class Models:
    def __init__(self, default_models: dict[str, Model]):
        self.list: dict[str, Model] = default_models | (self._get_models())

    def _get_models(self):
        """
        Use this as a retreiver of model catalogue from db
        """
        return {}

    def get_model(self, name: str):
        return self.list[name]

    @property
    def models(self) -> dict[str, Model]:
        return self.list
