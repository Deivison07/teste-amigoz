from pydantic import field_validator
from models.moedas.abstract_base_moeda import AbstractBaseMoeda

class DolarModel(AbstractBaseMoeda):
    currency_name: str   # Exemplo: "dollar"
    currency_kind: str   # Exemplo: "USD"
    currency_formatter: str  # Exemplo: "int"

    @field_validator('currency_price', mode='before')
    @classmethod
    def dividir_por_100(cls, v):
        try:
            return float(v) / 100
        except (TypeError, ValueError):
            raise ValueError("currency_price deve ser um número divisível por 100")
    
