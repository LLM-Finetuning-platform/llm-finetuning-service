from pydantic import BaseModel, Field


class Model(BaseModel):
    name: str = Field(default="smolLM2-135", description="Model name")
    model_id: str = Field(
        default="HuggingFaceTB/SmolLM2-135M-Instruct",
        description="""Model ID compatible with hugging face""",
    )
    context_length_window: int | None = Field(
        default=1024, description="Max sequence length of the model"
    )
