from pydantic import BaseModel, Field
from models.moedas.abstract_base_moeda import AbstractBaseMoeda

class EuroModel(AbstractBaseMoeda):
    currency_price: float = Field(alias="valor_comercial")
    currency_name: str = Field(alias="moeda")
    currency_kind: str = Field(alias="sigla")
    
