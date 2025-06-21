from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def testar_endpoint(self):
        self.client.get("/cotacoes")

# Teste de carga
# locust -f locustfile.py
