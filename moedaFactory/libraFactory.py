import asyncio
import httpx
import uuid
from fastapi import HTTPException
from sqlalchemy import select
from config.database import async_session
from config.setings import max_retry, callback_endpoint, cotacoes_endpoint


from models.moedas.libraModel import LibraModel
from moedaFactory.abstract_moeda import AbstractMoeda
from models.webhook.libraWebhook import LibraWebhook


class LibraFactory(AbstractMoeda):
    url = f"{cotacoes_endpoint}/cotacao/libra?callback_url={callback_endpoint}/callback"
    
    async def exec (self):
        response = await self.fetch_data()
        async with async_session() as session:
            for _ in range(max_retry):
                result = await session.execute(select(LibraWebhook).where(LibraWebhook.request_id == uuid.UUID(response.get("request_id"))))
                db_obj = result.scalar_one_or_none()
                if not db_obj:
                    await asyncio.sleep(0.010)
                    continue
                return LibraModel(**db_obj.data)
            raise HTTPException(status_code=404, detail="Registro não encontrado")
