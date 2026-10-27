from src.core.modules.trainer.peft.base import BasePEFT


class Methods:
    def __init__(self, defaults: list[BasePEFT]):
        self.methods: dict[str, BasePEFT] = self._get_methods(defaults)

    def _get_methods(self, defaults: list[BasePEFT]) -> dict[str, BasePEFT]:
        methods = {}
        for default in defaults:
            methods[default.method.name] = default
        return methods

    @property
    def peft_methods(self):
        return self.methods
