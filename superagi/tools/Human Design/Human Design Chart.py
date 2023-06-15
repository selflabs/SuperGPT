from typing import Callable, Type
from pydantic import Field, BaseModel
import requests

class BaseTool:
    # Define your base tool class here if required
    pass

def print_func(text: str) -> None:
    print("\n")
    print(text)

class HumanInputSchema(BaseModel):
    query: str = Field(
        ...,
        description="Question for the human",
    )

class HumanDesign(BaseTool):
    name = "Human Design"
    description = (
        "You can use this tool to create a Human Design Chart. "
        "Simply provide the necessary information and it will generate the chart for you."
    )
    args_schema: Type[HumanInputSchema] = HumanInputSchema
    prompt_func: Callable[[str], None] = Field(default_factory=lambda: print_func)
    input_func: Callable = Field(default_factory=lambda: input)

    def _execute(
        self,
        query: str
    ) -> str:
        self.prompt_func(query)
        response = requests.get("https://rolemodel.ai/humandesign")
        return response.text
