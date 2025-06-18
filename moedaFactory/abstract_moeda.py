from abc import ABC, abstractmethod
from fastapi import HTTPException
import httpx

class AbstractMoeda(ABC):
    url: str
    
    @abstractmethod
    async def exec (self): ...

    async def fetch_data(self) -> dict:
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(self.url)
                response.raise_for_status()
                return response.json()
        except httpx.TimeoutException:
            raise HTTPException(status_code=504, detail="Tempo de resposta excedido")

        except httpx.HTTPStatusError as exc:
            raise HTTPException(
            status_code=exc.response.status_code,
            detail=f"Erro na resposta da requisição: {exc.response.text}"
            )

        except httpx.RequestError as exc:
            raise HTTPException(status_code=502, detail=f"Erro na conexão: {exc}")

        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Erro inesperado: {exc}")

