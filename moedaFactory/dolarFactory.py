
from config.logger import logger
from moedaFactory.abstract_moeda import AbstractMoeda
from models.moedas.dolarModel import DolarModel
from config.setings import cotacoes_endpoint

class DolarFactory(AbstractMoeda):
    url = f"{cotacoes_endpoint}/cotacao/dolar"
    
    async def exec (self):
        logger.info("Acessando endpoint cotação Dolar")
        data = await self.fetch_data()
        return DolarModel(**data)            

        