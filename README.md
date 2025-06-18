# Desafio Cotação - API Assíncrona

Este projeto é uma API RESTful totalmente assíncrona construída com **FastAPI**, utilizando **Pydantic** para validação de dados, **SQLAlchemy** e **aiosqlite** para acesso assíncrono ao banco de dados SQLite, e servida com **Uvicorn**.

---

## Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web assíncrono  
- [Pydantic](https://pydantic.dev/) - Validação e parsing de dados  
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para manipulação do banco  
- [aiosqlite](https://github.com/jreese/aiosqlite) - Driver assíncrono SQLite  
- [Uvicorn](https://www.uvicorn.org/) - Server ASGI rápido e leve  

---
## Padrão de projeto usado (Factory)


## Endpoints

### `GET /cotacao`

Realiza a cotação de preços em diversas fontes externas e retorna a menor cotação encontrada.

- **Parâmetros:** Nenhum  
- **Resposta:** JSON com a menor cotação  

### `POST /callback`

Recebe um callback com as informações de cotação.

- **Payload esperado:**

```json
{
  "request_id": "uuid",
  "data": { "qualquer": "json" }
}
```

- **request_id:** UUID da requisição  
- **data:** Objeto JSON com dados adicionais  

### `GET /docs`

Documentação automática da API gerada pelo FastAPI (Swagger UI).

---

## Como usar
### Requisitos
- Ter o **Docker** instalado na sua máquina para rodar os containers.
  
### Rodando localmente com Docker Compose

 - Para construir e subir o projeto localmente:

```bash
sudo docker-compose up --build
```

### Usando a imagem pronta do Docker Hub

Para rodar diretamente com a imagem já pronta:

```bash
sudo docker run -p 3000:3000 --rm --network=host --name desafio-cotacoes deivisonalc/teste-amigoz
```

---

## Observações

- O projeto é totalmente assíncrono para melhor performance em chamadas I/O, como acesso a bancos de dados e requisições HTTP externas.  
- A documentação da API está disponível em `/docs` após a aplicação estar rodando.  

---

## Contato

- Para dúvidas ou contribuições, abra uma issue ou entre em contato com o desenvolvedor.

---

*Desenvolvido por Deivison Alcantara*
