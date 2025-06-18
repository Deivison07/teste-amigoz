from dotenv import load_dotenv
import os
def running_in_docker():
    return os.path.exists('/.dockerenv') or os.getenv("IN_DOCKER") == "1"

if running_in_docker():
    load_dotenv(".env.container")
else:
    load_dotenv(".env.local")

database_url = os.getenv("DATABASE_URL")
max_retry = int(os.getenv("MAX_RETRY"))
callback_endpoint = os.getenv("CALLBACK_ENDPOINT")
cotacoes_endpoint = os.getenv("COTACOES_ENDPOINT")



