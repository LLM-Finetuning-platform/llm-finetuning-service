from peft.config import PeftConfig
from pydantic import BaseModel

from src.utils.enums.peft import PEFTMethods


class BasePEFT(BaseModel):
    method: PEFTMethods
    peft_config: PeftConfig
