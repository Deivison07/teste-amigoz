from fastapi import FastAPI, status
from contextlib import asynccontextmanager
import asyncio
from config.database import engine, Base, async_session
from config.loadObjct import list_moedas
from config.logger import logger
from models.webhook.libraWebhook import LibraWebhook, LibraWebhookModel



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        logger.info("Criando banco de dados local se necessario")
        await conn.run_sync(Base.metadata.create_all)
    yield logger.info("Aplicação pronta.") 
    logger.info("finalizando Aplicação")


app = FastAPI(lifespan=lifespan,
    title="Documentação",
    description="Consulta cotações de moedas (Dólar, Euro e Libra)",
    version="1.0.0",
    contact={
        "name": "Deivison alcantara santos",
        "email": "deivisonalc02@gmail.com",
        "github": "https://github.com/Deivison07"
    }
    )

@app.get("/cotacoes",status_code=status.HTTP_200_OK) 
async def make_async_calls():
    '''
    Endpoint assincrono, chamadas a serviços distintos de cotação de moedas.
    Consulta cotações de moedas (Dólar, Euro e Libra)
    '''
    results = await asyncio.gather(*(item.exec() for item in list_moedas))
    results = min(results)
    logger.info("retornando menor cotação")
    return results

@app.post("/callback",status_code=status.HTTP_201_CREATED, response_model=None)
async def callback(callback: LibraWebhookModel):
    '''
    função callback para retorno de cotação
    '''
    async with async_session() as session:
        row = LibraWebhook(request_id = callback.request_id, data = callback.data)
        session.add(row)
        await session.commit()


    # sudo docker run -p 3000:3000 --rm --network=host --name desafio-cotacoes mostela/desafiocotacoes
