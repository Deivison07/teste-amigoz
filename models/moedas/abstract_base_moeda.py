from pydantic import BaseModel

class AbstractBaseMoeda(BaseModel):
    currency_price: float
    
    def __gt__(self, other):
        return self.currency_price > other.currency_price
    
    def __lt__(self, other):
        return self.currency_price < other.currency_price