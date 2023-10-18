"""schemes for stock api"""


from pydantic import BaseModel, Field

class StockSchema(BaseModel):
    name: str = Field(max_lenght=20)
    price: int = Field(gt=0)
    code: int = Field(max_length=7)

