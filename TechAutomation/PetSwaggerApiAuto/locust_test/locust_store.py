from locust import task,HttpUser, between


class StoreLoadTest(HttpUser):
    wait_time = between(1,2)

    @task
    def create_order(self):
        body = {
            "id": 1,
            "petId": 1,
            "quantity": 10,
            "shipDate": "2025-05-30T13:58:54.647Z",
            "status": "available",
            "complete": "true"
        }
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }
        self.client.post("/v2/store/order",json=body,headers=headers)

    @task
    def get_order_id(self):
        self.client.get("/v2/store/order/1")

    @task
    def delete_order(self):
        self.client.delete("/v2/store/order/1")

    @task
    def get_inventory(self):
        self.client.get("/v2/store/inventory")