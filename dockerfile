# Imagem base leve
FROM python:3.12-slim

# Atualiza pip e instala dependências do projeto
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Cria usuário não-root
RUN useradd -m appuser

# Cria diretório da aplicação e ajusta permissões
WORKDIR /app
COPY . /app
RUN chown -R appuser:appuser /app

# Troca para usuário seguro
USER appuser

# Expõe a porta padrão do FastAPI/Uvicorn
EXPOSE 8001

# Comando padrão para iniciar a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
