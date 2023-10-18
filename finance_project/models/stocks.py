"""class for stocks model."""
from dataclasses import dataclass

@dataclass
class Stock():
    name: str
    price: int
    code: str
    
