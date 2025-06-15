from locust import task,HttpUser, between


class PetLoadTest(HttpUser):
    wait_time = between(1,2)

    @task
    def create_pet(self):
        body = {
            "id": 10,
            "category": {"id": 10, "name": "deneme"},
            "name": "deneme",
            "photoUrls": ["string"],
            "tags": [{"id": 10, "name": "deneme"}],
            "status": "available"
        }
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

        self.client.post("/v2/pet",json=body,headers=headers)

    @task
    def get_pet_id(self):
        self.client.get("/v2/pet/10")

    @task
    def get_status_sold(self):
        params={
            "status":"sold"
        }
        self.client.get("/v2/pet/findByStatus",params=params)

    @task
    def get_status_pending(self):
        params = {
            "status": "pending"
        }
        self.client.get("/v2/pet/findByStatus",params=params)

    @task
    def get_status_available(self):
        params = {
            "status": "available"
        }
        self.client.get("/v2/pet/findByStatus",params=params)

    @task
    def update_pet(self):
        body = {
            "id": 10,
            "category": {"id": 10, "name": "update1"},
            "name": "update1",
            "photoUrls": ["string"],
            "tags": [{"id": 10, "name": "update1"}],
            "status": "placed"
        }
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }
        self.client.put("/v2/pet",headers=headers,json=body)

    @task
    def delete_id(self):
        self.client.delete("/v2/pet/10")
