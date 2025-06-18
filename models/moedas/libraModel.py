from typing import Optional
import uuid
from pydantic import Field, field_validator
from models.moedas.abstract_base_moeda import AbstractBaseMoeda

class LibraModel(AbstractBaseMoeda):
    currency_price: float = Field(alias="price")
    currency_name: str = Field(alias="name")
    currency_kind: str = Field(alias="currency_kind")
    

    
    
