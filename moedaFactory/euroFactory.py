from pydantic import BaseModel
from moedaFactory.abstract_moeda import AbstractMoeda
import httpx
from models.moedas.euroModel import EuroModel
from config.setings import cotacoes_endpoint


class EuroFactory(AbstractMoeda):   
    url = f"{cotacoes_endpoint}/cotacao/euro"
    async def exec (self):
            data = await self.fetch_data()
            return EuroModel(**data["cotacao"])
        